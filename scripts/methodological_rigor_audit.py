#!/usr/bin/env python3
"""
Reproducible random sample of PubMed primary-research papers and methodological
rigor scoring framework (vaccinology vs chemistry).
"""
from __future__ import annotations

import json
import math
import random
import re
import ssl
import time
import urllib.error
import urllib.parse
import urllib.request
import xml.etree.ElementTree as ET
from dataclasses import dataclass, field, asdict
from pathlib import Path
from typing import Any

try:
    from scipy import stats
except ImportError:
    stats = None  # type: ignore

import matplotlib.pyplot as plt
import numpy as np

WORKDIR = Path("/workspace/tmp/rigor-audit")
WORKDIR.mkdir(parents=True, exist_ok=True)

DB = "PubMed (NCBI E-utilities: esearch, efetch, elink)"
DATE_WINDOW = ("2015/01/01", "2024/12/31")
DATE_LABEL = "2015-01-01 to 2024-12-31"
RANDOM_SEED = 20251111
SAMPLE_N = 12

VACCINOLOGY_QUERY = (
    '(vaccines[MeSH] OR vaccine[tiab] OR vaccination[tiab] OR immunization[tiab]) '
    f'AND ("{DATE_WINDOW[0]}"[PDAT] : "{DATE_WINDOW[1]}"[PDAT]) '
    "AND (Journal Article[pt] OR Clinical Trial[pt] OR Randomized Controlled Trial[pt]) "
    'NOT (Review[pt] OR "Systematic Review"[pt] OR Meta-Analysis[pt] OR Editorial[pt] '
    'OR Comment[pt] OR "Case Reports"[pt] OR "Clinical Trial Protocol"[pt] OR News[pt])'
)

CHEMISTRY_QUERY = (
    '(chemistry[MeSH] OR "chemical synthesis"[tiab] OR catalysis[tiab] OR '
    '"organic synthesis"[tiab] OR "reaction kinetics"[tiab]) '
    f'AND ("{DATE_WINDOW[0]}"[PDAT] : "{DATE_WINDOW[1]}"[PDAT]) '
    "AND (Journal Article[pt]) "
    'NOT (Review[pt] OR "Systematic Review"[pt] OR Meta-Analysis[pt] OR Editorial[pt] '
    'OR Comment[pt] OR "Case Reports"[pt] OR News[pt])'
)

DIMENSIONS = [
    "pre_specification",
    "randomisation",
    "blinding",
    "comparator_adequacy",
    "outcome_selection",
    "power",
    "reporting_completeness",
    "independence_replicability",
]

DIMENSION_LABELS = {
    "pre_specification": "Pre-specification",
    "randomisation": "Randomisation",
    "blinding": "Blinding",
    "comparator_adequacy": "Comparator adequacy",
    "outcome_selection": "Outcome selection",
    "power": "Power",
    "reporting_completeness": "Reporting completeness",
    "independence_replicability": "Independence and replicability",
}

NCBI_BASE = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/"
EMAIL = "rigor-audit@example.com"
TOOL = "scientism_rigor_audit"


def vault_pmids() -> set[str]:
    """Collect PMIDs already documented in wiki/sources."""
    root = Path("/workspace/wiki/sources")
    found: set[str] = set()
    pat = re.compile(
        r"PMID[:\s]+(\d{7,8})|pubmed\.ncbi\.nlm\.nih\.gov/(\d{7,8})",
        re.I,
    )
    for p in root.glob("*.md"):
        text = p.read_text(encoding="utf-8", errors="replace")
        for m in pat.finditer(text):
            found.add(m.group(1) or m.group(2))
    return found


def ncbi_get(params: dict[str, str], endpoint: str = "esearch.fcgi", retries: int = 5) -> bytes:
    params = {**params, "tool": TOOL, "email": EMAIL}
    url = NCBI_BASE + endpoint + "?" + urllib.parse.urlencode(params)
    ctx = ssl.create_default_context()
    for attempt in range(retries):
        try:
            with urllib.request.urlopen(url, timeout=120, context=ctx) as resp:
                return resp.read()
        except (urllib.error.HTTPError, urllib.error.URLError, TimeoutError):
            time.sleep(0.5 * (2**attempt))
    raise RuntimeError(f"NCBI request failed: {params.get('term', '')[:80]}")


def _esearch_page(query: str, retstart: int, retmax: int) -> tuple[int, list[str]]:
    raw = ncbi_get(
        {
            "db": "pubmed",
            "term": query,
            "retstart": str(retstart),
            "retmax": str(retmax),
            "retmode": "xml",
        }
    )
    root = ET.fromstring(raw)
    total = int(root.findtext("Count") or "0")
    ids = [el.text for el in root.findall("IdList/Id") if el.text]
    return total, ids


def esearch_all_pmids(query: str) -> tuple[int, list[str]]:
    """Return total count and all PMIDs for query (paginated)."""
    total, first_ids = _esearch_page(query, 0, 10000)
    pmids: list[str] = list(first_ids)
    retmax = 10000
    for start in range(retmax, total, retmax):
        _, ids = _esearch_page(query, start, retmax)
        pmids.extend(ids)
        time.sleep(0.34)
    return total, pmids


def uniform_random_pmids(
    query: str,
    total_hits: int,
    exclude: set[str],
    n: int,
    seed: int,
    max_attempts: int = 800,
) -> tuple[list[str], list[int]]:
    """
    Uniform draws from PubMed result positions 0..total_hits-1 (PubMed default sort order).
    Each index maps to esearch retstart with retmax=1.
    """
    rng = random.Random(seed)
    chosen: list[str] = []
    indices: list[int] = []
    seen: set[str] = set()
    attempts = 0
    while len(chosen) < n and attempts < max_attempts:
        idx = rng.randrange(0, total_hits)
        attempts += 1
        _, ids = _esearch_page(query, idx, 1)
        if not ids:
            continue
        pmid = ids[0]
        if pmid in exclude or pmid in seen:
            continue
        chosen.append(pmid)
        indices.append(idx)
        seen.add(pmid)
        time.sleep(0.11)
    if len(chosen) < n:
        raise RuntimeError(f"Only drew {len(chosen)}/{n} papers after {attempts} attempts")
    return chosen, indices


def efetch_pubmed_xml(pmids: list[str]) -> ET.Element:
    ids = ",".join(pmids)
    raw = ncbi_get(
        {
            "db": "pubmed",
            "id": ids,
            "retmode": "xml",
        },
        endpoint="efetch.fcgi",
    )
    return ET.fromstring(raw)


def parse_article(article: ET.Element) -> dict[str, Any]:
    medline = article.find("MedlineCitation")
    pmid = medline.findtext("PMID") if medline is not None else ""
    art = medline.find("Article") if medline is not None else None
    title = ""
    abstract_parts: list[str] = []
    journal = ""
    year = ""
    pub_types: list[str] = []
    if art is not None:
        title = "".join(art.findtext("ArticleTitle") or "")
        abst = art.find("Abstract")
        if abst is not None:
            for t in abst.findall("AbstractText"):
                label = t.get("Label", "")
                seg = "".join(t.itertext())
                abstract_parts.append(f"{label}: {seg}" if label else seg)
        j = art.find("Journal")
        if j is not None:
            journal = j.findtext("Title") or j.findtext("ISOAbbreviation") or ""
        pd = art.find("Journal/JournalIssue/PubDate")
        if pd is not None:
            year = pd.findtext("Year") or (pd.findtext("MedlineDate") or "")[:4]
        for pt in art.findall("PublicationTypeList/PublicationType"):
            pub_types.append(pt.text or "")
    auth_list = medline.findall(".//AuthorList/Author") if medline else []
    authors = []
    for a in auth_list[:12]:
        ln = a.findtext("LastName") or ""
        ini = a.findtext("Initials") or ""
        if ln:
            authors.append(f"{ln} {ini}".strip())
    if len(auth_list) > 12:
        authors.append("et al.")

    # DOI
    doi = ""
    for idn in article.findall(".//ArticleId"):
        if idn.get("IdType") == "doi":
            doi = idn.text or ""
            break

    mesh_terms = [
        d.findtext("DescriptorName") or ""
        for d in medline.findall(".//MeshHeadingList/MeshHeading")
    ] if medline is not None else []

    return {
        "pmid": pmid,
        "title": title,
        "abstract": " ".join(abstract_parts),
        "journal": journal,
        "year": year,
        "authors": authors,
        "doi": doi,
        "publication_types": pub_types,
        "mesh": mesh_terms,
    }


def pmc_full_text(pmid: str) -> str:
    """Try to fetch PMC OA full text body as plain text."""
    try:
        link = ncbi_get(
            {"dbfrom": "pubmed", "db": "pmc", "id": pmid, "retmode": "json"},
            endpoint="elink.fcgi",
        )
        ldata = json.loads(link.decode())
        linksets = ldata.get("linksets", [])
        pmc_ids = []
        for ls in linksets:
            for ldb in ls.get("linksetdbs", []):
                if ldb.get("linkname") == "pubmed_pmc":
                    pmc_ids.extend(ldb.get("links", []))
        if not pmc_ids:
            return ""
        pmcid = pmc_ids[0]
        time.sleep(0.34)
        raw = ncbi_get({"db": "pmc", "id": str(pmcid), "retmode": "xml"}, endpoint="efetch.fcgi")
        root = ET.fromstring(raw)
        parts: list[str] = []
        for el in root.iter():
            if el.tag.endswith("p") or el.tag.endswith("sec"):
                t = (el.text or "") + "".join((c.tail or "") for c in el)
                if t.strip():
                    parts.append(t.strip())
        return "\n".join(parts)
    except Exception:
        return ""


def combined_corpus(meta: dict[str, Any], body: str) -> str:
    return f"{meta.get('title','')}\n{meta.get('abstract','')}\n{body}".lower()


def infer_design(field: str, corpus: str, pub_types: list[str]) -> str:
    pts = " ".join(pub_types).lower()
    if "randomized controlled trial" in pts or "randomised controlled trial" in corpus:
        return "Randomized controlled trial"
    if "clinical trial" in pts:
        return "Clinical trial"
    if "observational study" in pts or "cohort" in corpus:
        return "Observational cohort"
    if field == "chemistry":
        if "spectroscop" in corpus or "nmr" in corpus or "crystallograph" in corpus:
            return "Characterization / spectroscopy study"
        if "synthesis" in corpus or "catalyst" in corpus:
            return "Experimental synthesis or catalysis study"
        return "Laboratory experimental study"
    if "immunogenicity" in corpus or "efficacy" in corpus:
        return "Clinical or immunogenicity trial"
    return "Primary research (design not fully classified from metadata)"


def extract_sample_size(corpus: str) -> str:
    patterns = [
        r"n\s*=\s*([\d,]+)",
        r"(\d[\d,]*)\s+participants",
        r"(\d[\d,]*)\s+patients",
        r"(\d[\d,]*)\s+subjects",
        r"(\d[\d,]*)\s+healthy adults",
        r"(\d[\d,]*)\s+volunteers",
        r"(\d[\d,]*)\s+mice",
        r"(\d[\d,]*)\s+samples",
    ]
    for pat in patterns:
        m = re.search(pat, corpus, re.I)
        if m:
            return m.group(1).replace(",", "")
    return "Not stated in abstract/full-text excerpt searched"


@dataclass
class Score:
    value: float
    justification: str


def quote_snippet(corpus: str, needles: list[str], width: int = 90) -> str:
    low = corpus.lower()
    for needle in needles:
        idx = low.find(needle.lower())
        if idx >= 0:
            start = max(0, idx - width // 3)
            end = min(len(corpus), idx + width)
            frag = re.sub(r"\s+", " ", corpus[start:end]).strip()
            return f'"{frag}"'
    return ""


def score_paper(field: str, meta: dict[str, Any], corpus: str) -> dict[str, Score]:
    """Evidence-quoted scoring from full text or abstract; field-aware anchors."""
    is_vacc = field == "vaccinology"
    has_random_allocation = any(
        p in corpus
        for p in (
            "randomly assigned",
            "randomly allocated",
            "randomized",
            "randomised",
            "cluster-random",
            "block random",
            "computer-generated random",
        )
    )
    is_experimental = has_random_allocation or any(
        w in corpus
        for w in (
            "placebo-controlled",
            "controlled trial",
            "in vivo",
            "in vitro",
            "mice were",
            "participants were",
        )
    )
    is_observational = any(
        w in corpus
        for w in ("cross-sectional", "survey", "questionnaire", "retrospective cohort", "registry study")
    ) and not has_random_allocation
    is_lab = field == "chemistry" or any(
        w in corpus for w in ("synthesis", "catalyst", "reaction", "nmr", "spectroscop", "chromatograph")
    )

    def has(*words: str) -> bool:
        return any(w in corpus for w in words)

    def clip(x: float) -> float:
        return max(0.0, min(10.0, round(x, 1)))

    def j_base(text: str, needles: list[str]) -> str:
        q = quote_snippet(corpus, needles)
        return f"{text} {q}".strip()

    scores: dict[str, Score] = {}

    # 1 Pre-specification
    if has("clinicaltrials.gov", " nct", "anzctr", "isrctn") or re.search(r"nct\d{8}", corpus):
        if has("registered before", "prior to enrolment", "prior to enrollment", "before recruitment"):
            v = 8.5
            j = j_base(
                "Trial registration is cited with timing language indicating registration before recruitment.",
                ["clinicaltrials.gov", "nct"],
            )
        else:
            v = 6.5
            j = j_base(
                "A public trial registry number appears, but pre-locking of the analysis plan is not explicit.",
                ["clinicaltrials.gov", "nct"],
            )
    elif has("osf.io", "aspredicted", "pre-registered", "preregistered"):
        v, j = 6.0, j_base("Preregistration on OSF or similar is mentioned.", ["osf", "preregistered"])
    elif has("ethics committee", "institutional review", "irb", "prospective"):
        v = 4.5 if is_observational else 4.0
        j = j_base(
            "Ethics or prospective protocol approval is noted without public analysis preregistration.",
            ["ethics", "irb", "prospective"],
        )
    elif is_lab and has("experimental section", "general procedure", "supporting information"):
        v, j = 4.0, j_base(
            "Bench protocols are narrated in methods/supplement, but no formal preregistration is stated.",
            ["experimental", "supporting information"],
        )
    else:
        v, j = 1.5, "No registry, preregistration, or explicit prespecification appears in the indexed text."
    scores["pre_specification"] = Score(clip(v), j)

    # 2 Randomisation
    if has_random_allocation:
        if has("allocation concealment", "sequential numbered", "computer-generated"):
            v = 9.0
        else:
            v = 7.5
        j = j_base(
            "Units are randomly allocated to comparison conditions, consistent with experimental design.",
            ["randomly assigned", "randomized", "randomised"],
        )
    elif is_observational:
        v, j = 6.0, j_base(
            "Observational design: treatment randomisation is not applicable; score is anchored to field-appropriate conduct.",
            ["cross-sectional", "survey", "cohort"],
        )
    elif is_lab and has("technical replicate", "independent experiment", "biological replicate", "triplicate"):
        v, j = 6.5, j_base(
            "Experimental units include independent or technical replicates rather than clinical randomisation.",
            ["replicate", "triplicate", "independent experiment"],
        )
    elif is_lab:
        v, j = 3.5, j_base(
            "Laboratory comparisons lack explicit randomisation of run order or batch assignment.",
            ["synthesis", "reaction"],
        )
    else:
        v, j = 2.0, "No random allocation language is present in the available text."
    scores["randomisation"] = Score(clip(v), j)

    # 3 Blinding
    if has("double-blind", "double blind", "triple-blind", "single-blind", "observer-blind", "assessor blind"):
        v, j = 8.5, j_base("Blinding of participants and/or assessors is stated.", ["double-blind", "single-blind", "blinded"])
    elif has("masked", "blinded") and not has("unblinded"):
        v, j = 7.0, j_base("Masking/blinding terminology is used for at least one study role.", ["masked", "blinded"])
    elif is_lab:
        v, j = 4.5, "Bench chemistry seldom uses participant blinding; omission is scored as neutral for the field, not as malpractice."
    elif is_experimental and has_random_allocation:
        v, j = 3.0, j_base(
            "Randomised experiment without explicit blinding of participants or outcome assessment.",
            ["randomly assigned", "randomized"],
        )
    elif is_observational:
        v, j = 5.0, "Blinding is typically not applicable to observational surveys; neutral anchor applied."
    else:
        v, j = 1.5, "No blinding procedures are reported."
    scores["blinding"] = Score(clip(v), j)

    # 4 Comparator adequacy
    if has("placebo", "vehicle control", "sham", "untreated control", "negative control"):
        v = 8.0 if has("dose", "vehicle", "saline") else 6.5
        j = j_base("Named placebo, vehicle, or negative control arm.", ["placebo", "vehicle", "sham", "negative control"])
    elif has("active control", "standard of care", "positive control", "comparator vaccine"):
        v, j = 7.0, j_base("Active or standard-of-care comparator is identified.", ["active control", "standard of care", "comparator"])
    elif is_lab and has("without catalyst", "blank", "reference compound", "internal standard", "control experiment"):
        v, j = 7.5, j_base(
            "Chemistry-appropriate reference/blank/uncatalyzed controls are described.",
            ["control", "reference", "without catalyst"],
        )
    elif is_observational and has("adjusted for", "propensity", "matched"):
        v, j = 6.0, j_base("Analytic comparators use matching or adjustment rather than experimental arms.", ["adjusted", "matched"])
    else:
        v, j = 3.0, j_base(
            "Comparator arms or negative controls are weak or not named.",
            ["control", "comparator"],
        )
    scores["comparator_adequacy"] = Score(clip(v), j)

    # 5 Outcome selection
    if has("primary endpoint", "primary outcome", "primary efficacy"):
        v = 8.5 if has("secondary outcome", "secondary endpoint") else 7.5
        j = j_base("Primary outcome is declared.", ["primary outcome", "primary endpoint"])
    elif is_lab and has("yield", "selectivity", "conversion", "turnover frequency", "ee "):
        v, j = 7.0, j_base("Chemical performance metrics (yield/selectivity/rate) serve as declared readouts.", ["yield", "selectivity"])
    elif has("immunogenicity", "neutralizing antibody", "seroconversion", "vaccine efficacy"):
        v, j = 6.0, j_base("Vaccine-relevant immunologic endpoints are named.", ["immunogenicity", "neutralizing", "efficacy"])
    else:
        v, j = 3.5, j_base(
            "Multiple endpoints appear without a clear primary/secondary hierarchy.",
            ["outcome", "endpoint"],
        )
    scores["outcome_selection"] = Score(clip(v), j)

    # 6 Power
    if has("sample size calculation", "power calculation", "power of 80", "power 90", "powered to detect"):
        v, j = 8.5, j_base("Formal sample-size or power calculation is reported.", ["power calculation", "sample size calculation"])
    elif has("power") and has("n=", "enrolled", "participants"):
        v, j = 5.5, j_base("Target enrollment and power language appear without full calculation detail.", ["power", "sample size"])
    elif is_lab and has("n=", "replicate", "independent experiments"):
        v, j = 5.5, j_base(
            "Replicate counts are given; formal power analysis is uncommon in bench chemistry.",
            ["replicate", "n="],
        )
    elif is_observational and has("n=", "participants", "respondents"):
        v, j = 4.0, j_base("Sample size is reported for observational data without a priori power analysis.", ["n=", "participants"])
    else:
        v, j = 2.0, "No power or sample-size justification appears in the available text."
    scores["power"] = Score(clip(v), j)

    # 7 Reporting completeness
    pts = 2.0
    notes = []
    if has("confidence interval", "95% ci", "95% confidence"):
        pts += 2.5
        notes.append("confidence intervals")
    if has("effect size", "odds ratio", "hazard ratio", "risk difference", "cohen"):
        pts += 2.0
        notes.append("effect sizes")
    if has("missing data", "imputation", "intention-to-treat", "itt analysis"):
        pts += 2.0
        notes.append("missing-data/ITT")
    if has("standard deviation", "mean ±", "error bars", "sem "):
        pts += 1.5
        notes.append("dispersion")
    if has("supplementary", "table s", "figure s"):
        pts += 1.0
    v = clip(pts)
    if notes:
        j = j_base(f"Reporting includes {', '.join(notes)}.", notes[:1])
    else:
        j = "Sparse quantitative reporting: limited CIs, dispersion, and missing-data handling in the indexed text."
    scores["reporting_completeness"] = Score(v, j)

    # 8 Independence and replicability
    disclosed_funding = has("funding", "supported by", "grant ", "sponsor")
    disclosed_ci = has("competing", "conflict of interest", "disclosure")
    shared = has("data availability", "code availability", "github", "deposited", "supplementary data", "materials available")
    if disclosed_funding and disclosed_ci and shared:
        v, j = 9.0, j_base("Funding, conflicts, and data/materials sharing are all addressed.", ["funding", "conflict", "data availability"])
    elif disclosed_funding and disclosed_ci:
        v, j = 7.0, j_base("Funding and conflicts are disclosed.", ["funding", "conflict"])
    elif disclosed_funding:
        v, j = 5.0, j_base("Funding is disclosed but competing-interest or sharing statements are thin.", ["funding", "supported"])
    elif shared:
        v, j = 5.5, j_base("Data or code sharing is mentioned without complete funding disclosure.", ["data availability", "github"])
    else:
        v, j = 1.0, "Funding source is not disclosed in the indexed text (flagged)."
    scores["independence_replicability"] = Score(clip(v), j)

    return scores


def mann_whitney(a: list[float], b: list[float]) -> dict[str, Any]:
    if stats is None:
        return {"p_value": None, "effect_size_r": None, "note": "scipy not installed"}
    u, p = stats.mannwhitneyu(a, b, alternative="two-sided", method="auto")
    n1, n2 = len(a), len(b)
    r = 1 - (2 * u) / (n1 * n2)  # rank-biserial correlation approximation
    return {"u_statistic": float(u), "p_value": float(p), "effect_size_r": float(r)}


def field_stats(values: list[float]) -> dict[str, float]:
    arr = np.array(values, dtype=float)
    return {
        "mean": float(np.mean(arr)),
        "sd": float(np.std(arr, ddof=1)) if len(arr) > 1 else 0.0,
        "median": float(np.median(arr)),
        "min": float(np.min(arr)),
        "max": float(np.max(arr)),
    }


def plot_dimensions(papers: list[dict], outdir: Path) -> None:
    vac_q = VACCINOLOGY_QUERY[:120] + "..."
    chem_q = CHEMISTRY_QUERY[:120] + "..."
    for dim in DIMENSIONS:
        fig, ax = plt.subplots(figsize=(12, 10))
        y = 0
        ticks: list[str] = []
        for field, color in (("vaccinology", "#c0392b"), ("chemistry", "#2980b9")):
            subset = [p for p in papers if p["field"] == field]
            means = [p["scores"][dim]["value"] for p in subset]
            mmean = np.mean(means) if means else 0
            for p in sorted(subset, key=lambda x: -x["scores"][dim]["value"]):
                val = p["scores"][dim]["value"]
                ax.barh(y, val, color=color, alpha=0.85, height=0.7)
                ticks.append(f"{p['pmid']}")
                y += 1
            ax.axvline(mmean, color=color, linestyle="--", linewidth=2, alpha=0.9)
            y += 0.5
        ax.set_xlim(0, 10)
        ax.set_xlabel("Score (0–10)")
        ax.set_title(
            f"{DIMENSION_LABELS[dim]}\nn=12 vaccinology + 12 chemistry | {DATE_LABEL}\n"
            f"Vac: {vac_q}\nChem: {chem_q}"
        )
        ax.set_yticks(range(len(ticks)))
        ax.set_yticklabels(ticks, fontsize=7)
        fig.tight_layout()
        fig.savefig(outdir / f"dimension_{dim}.png", dpi=150)
        plt.close(fig)

    # Totals chart
    fig, ax = plt.subplots(figsize=(12, 10))
    y = 0
    ticks = []
    for field, color in (("vaccinology", "#c0392b"), ("chemistry", "#2980b9")):
        subset = [p for p in papers if p["field"] == field]
        totals = [p["total"] for p in subset]
        mmean = np.mean(totals)
        for p in sorted(subset, key=lambda x: -x["total"]):
            ax.barh(y, p["total"], color=color, alpha=0.85, height=0.7)
            ticks.append(f"{p['pmid']}")
            y += 1
        ax.axvline(mmean, color=color, linestyle="--", linewidth=2)
        y += 0.5
    ax.set_xlim(0, 80)
    ax.set_xlabel("Total score (/80)")
    ax.set_title(f"Total methodological rigor\nn=12 per field | {DATE_LABEL}")
    ax.set_yticks(range(len(ticks)))
    ax.set_yticklabels(ticks, fontsize=7)
    fig.tight_layout()
    fig.savefig(outdir / "dimension_total.png", dpi=150)
    plt.close(fig)


def build_analysis(papers: list[dict]) -> dict[str, Any]:
    analysis: dict[str, Any] = {"by_field": {}, "by_dimension": {}, "tests": {}}
    for field in ("vaccinology", "chemistry"):
        subset = [p for p in papers if p["field"] == field]
        analysis["by_field"][field] = field_stats([p["total"] for p in subset])
    for dim in DIMENSIONS:
        analysis["by_dimension"][dim] = {
            f: field_stats([p["scores"][dim]["value"] for p in papers if p["field"] == f])
            for f in ("vaccinology", "chemistry")
        }
        va = [p["scores"][dim]["value"] for p in papers if p["field"] == "vaccinology"]
        ch = [p["scores"][dim]["value"] for p in papers if p["field"] == "chemistry"]
        analysis["tests"][dim] = mann_whitney(va, ch)
    va_t = [p["total"] for p in papers if p["field"] == "vaccinology"]
    ch_t = [p["total"] for p in papers if p["field"] == "chemistry"]
    analysis["tests"]["total"] = mann_whitney(va_t, ch_t)
    return analysis


def rescore_saved(draw_pmids: dict[str, list[str]]) -> list[dict]:
    papers: list[dict] = []
    for field, pmids in draw_pmids.items():
        root = efetch_pubmed_xml(pmids)
        for art in root.findall("PubmedArticle"):
            meta = parse_article(art)
            time.sleep(0.2)
            body = pmc_full_text(meta["pmid"])
            corpus = combined_corpus(meta, body)
            meta["full_text_chars"] = len(body)
            meta["study_design"] = infer_design(field, corpus, meta["publication_types"])
            meta["sample_size"] = extract_sample_size(corpus)
            sc = score_paper(field, meta, corpus)
            total = sum(s.value for s in sc.values())
            papers.append(
                {
                    "field": field,
                    "pmid": meta["pmid"],
                    "citation": {
                        "authors": meta["authors"],
                        "title": meta["title"],
                        "journal": meta["journal"],
                        "year": meta["year"],
                        "doi": meta["doi"],
                    },
                    "study_design": meta["study_design"],
                    "sample_size": meta["sample_size"],
                    "full_text_chars": meta["full_text_chars"],
                    "scores": {k: asdict(v) for k, v in sc.items()},
                    "total": total,
                    "flags": {
                        "missing_registered_protocol": sc["pre_specification"].value < 5.5,
                        "undisclosed_funding": sc["independence_replicability"].value <= 2.0,
                    },
                }
            )
    return papers


def main(rescore: bool = False) -> None:
    meta_path = WORKDIR / "sampling.json"
    if rescore and meta_path.exists():
        saved = json.loads(meta_path.read_text(encoding="utf-8"))
        papers = rescore_saved(
            {
                "vaccinology": saved["vaccinology"]["drawn_pmids"],
                "chemistry": saved["chemistry"]["drawn_pmids"],
            }
        )
    else:
        exclude = vault_pmids()
        vac_total, _ = _esearch_page(VACCINOLOGY_QUERY, 0, 0)
        chem_total, _ = _esearch_page(CHEMISTRY_QUERY, 0, 0)

        vac_draw, vac_indices = uniform_random_pmids(
            VACCINOLOGY_QUERY, vac_total, exclude, SAMPLE_N, RANDOM_SEED
        )
        chem_draw, chem_indices = uniform_random_pmids(
            CHEMISTRY_QUERY, chem_total, exclude, SAMPLE_N, RANDOM_SEED + 1
        )

        meta_path.write_text(
            json.dumps(
                {
                    "database": DB,
                    "date_window": DATE_LABEL,
                    "random_seed_vaccinology": RANDOM_SEED,
                    "random_seed_chemistry": RANDOM_SEED + 1,
                    "excluded_vault_pmids_count": len(exclude),
                    "randomisation_procedure": (
                        "Uniform random indices in [0, total_hits-1] using Python random.Random(seed); "
                        "each index retrieved via esearch retstart=index, retmax=1 (PubMed default relevance order); "
                        "vault PMIDs excluded and resampling continues until 12 unique papers."
                    ),
                    "vaccinology": {
                        "search_string": VACCINOLOGY_QUERY,
                        "total_hits": vac_total,
                        "random_seed": RANDOM_SEED,
                        "drawn_result_indices": vac_indices,
                        "drawn_pmids": vac_draw,
                    },
                    "chemistry": {
                        "search_string": CHEMISTRY_QUERY,
                        "total_hits": chem_total,
                        "random_seed": RANDOM_SEED + 1,
                        "drawn_result_indices": chem_indices,
                        "drawn_pmids": chem_draw,
                    },
                },
                indent=2,
            ),
            encoding="utf-8",
        )
        papers = rescore_saved(
            {"vaccinology": vac_draw, "chemistry": chem_draw}
        )

    analysis = build_analysis(papers)

    (WORKDIR / "papers.json").write_text(json.dumps(papers, indent=2), encoding="utf-8")
    (WORKDIR / "analysis.json").write_text(json.dumps(analysis, indent=2), encoding="utf-8")

    plot_dimensions(papers, WORKDIR)
    print(json.dumps({"sampling": str(meta_path), "n_papers": len(papers)}, indent=2))


if __name__ == "__main__":
    import sys

    main(rescore="--rescore" in sys.argv)
