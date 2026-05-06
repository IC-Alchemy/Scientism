from __future__ import annotations

import csv
import json
import time
import urllib.parse
import urllib.request
import xml.etree.ElementTree as ET
from dataclasses import dataclass
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
OUT_JSON = ROOT / "wiki" / "synthesis" / "gutknecht-letter-questions-7-9-api-lookups.json"
OUT_CSV = ROOT / "wiki" / "synthesis" / "gutknecht-letter-questions-7-9-api-lookups.csv"
PUBMED_EFETCH = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi"
PUBMED_ESEARCH = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esearch.fcgi"


@dataclass(frozen=True)
class Candidate:
    key: str
    question: str
    lookup: str
    lookup_type: str
    role_hint: str


CANDIDATES = [
    Candidate("larsson-1985-hemophilia-life-expectancy", "Q7", "3885998", "pmid", "primary-study"),
    Candidate("johnson-1985-hemophilia-treatment-centers", "Q7", "4014173", "pmid", "primary-study"),
    Candidate("chorba-1994-hemophilia-a-longevity-causes", "Q7", "8141117", "pmid", "primary-study"),
    Candidate("chorba-2001-hiv-age-cause-death-hemophilia-a", "Q7", "11279632", "pmid", "primary-study"),
    Candidate("darby-1995-mortality-before-after-hiv-hemophilia", "Q7/Q8", "7659168", "pmid", "primary-study"),
    Candidate("triemstra-1995-hemophilia-mortality-dutch", "Q7", "7486463", "pmid", "primary-study"),
    Candidate("kroner-1994-hiv-incidence-hemophilia", "Q7/Q8", "8106967", "pmid", "primary-study"),
    Candidate("goedert-1989-hiv-aids-hemophilia", "Q7", "2477702", "pmid", "primary-study"),
    Candidate("smit-1989-dutch-hemophiliacs-1972-85", "Q7", "2493872", "pmid", "primary-study"),
    Candidate("donegan-1990-transfusion-risk-aids", "Q8", "2240875", "pmid", "primary-study"),
    Candidate("ward-1989-transfusion-associated-hiv-natural-history", "Q8", "2779617", "pmid", "primary-study"),
    Candidate("giesecke-1988-swedish-hemophiliacs-transfusion-recipients", "Q8", "3165683", "pmid", "primary-study"),
    Candidate("darby-1989-aids-excess-mortality-hemophiliacs", "Q8", "2497891", "pmid", "primary-study"),
    Candidate("simmonds-1991-edinburgh-hemophilia-hiv-cohort", "Q8", "1682589", "pmid", "primary-study"),
    Candidate("schinaia-1994-italian-hiv-positive-hemophiliacs", "Q8", "7974372", "pmid", "primary-study"),
    Candidate("roosendaal-1998-clotting-product-consumption-aids", "Q8", "9873260", "pmid", "primary-study"),
    Candidate("european-collaborative-1991-children-born-hiv", "Q8", "1671109", "pmid", "primary-study"),
    Candidate("european-collaborative-1994-vertical-hiv-natural-history", "Q8", "7970995", "pmid", "primary-study"),
    Candidate("abrams-1998-hiv-load-infants-progression", "Q8", "9652428", "pmid", "primary-study"),
    Candidate("cardo-1997-occupational-seroconversion", "Q8", "9366579", "pmid", "primary-study"),
    Candidate("ippolito-1999-occupational-hiv-cases", "Q8", "10064256", "pmid", "case-series-review"),
    Candidate("cdc-1981-pneumocystis-los-angeles", "Q8 chronology", "6265753", "pmid", "primary-historical-document"),
    Candidate("cdc-1981-ks-pcp-homosexual-men", "Q8 chronology", "6789108", "pmid", "primary-historical-document"),
    Candidate("gottlieb-1981-pcp-candidiasis", "Q8 chronology", "6272109", "pmid", "clinical-case-series"),
    Candidate("cdc-1982-aids-update-united-states", "Q8 chronology", "6815471", "pmid", "primary-historical-document"),
    Candidate("cdc-1982-aids-hemophilia-a", "Q8 chronology", "6819439", "pmid", "primary-historical-document"),
    Candidate("yarchoan-1986-first-azt-administration", "Q8 chronology", "10.1016/S0140-6736(86)92808-4", "doi", "primary-study"),
    Candidate("fischl-1987-azt-efficacy", "Q9", "3299089", "pmid", "primary-study"),
    Candidate("richman-1987-azt-toxicity", "Q9", "3299090", "pmid", "primary-study"),
    Candidate("fischl-1990-actg-016", "Q9", "1970466", "pmid", "primary-study"),
    Candidate("volberding-1990-actg-019", "Q9", "1969115", "pmid", "primary-study"),
    Candidate("fischl-1992-actg-019-toxicity", "Q9", "1359846", "pmid", "primary-study"),
    Candidate("volberding-1994-actg-019-duration", "Q9", "7913730", "pmid", "primary-study"),
    Candidate("concorde-1994-immediate-deferred-zidovudine", "Q9", "7908356", "pmid", "primary-study"),
    Candidate("mulder-1994-european-australian-study-017", "Q9", "7913326", "pmid", "primary-study"),
    Candidate("connor-1994-pactg-076", "Q9", "7935654", "pmid", "primary-study"),
    Candidate("actg-116b-117-1995-zidovudine-didanosine", "Q9", "7726705", "pmid", "primary-study"),
    Candidate("daquila-1995-zidovudine-resistance", "Q9", "7538548", "pmid", "primary-study"),
    Candidate("delta-1996-combination-therapy", "Q9", "8709686", "pmid", "primary-study"),
    Candidate("actg-175-1996-monotherapy-combination", "Q9", "8813038", "pmid", "primary-study"),
    Candidate("lamivudine-1996-3tc-zidovudine", "Q9", "8656503", "pmid", "primary-study"),
]


def fetch_text(url: str, params: dict[str, str]) -> str:
    query = urllib.parse.urlencode(params)
    with urllib.request.urlopen(f"{url}?{query}", timeout=30) as response:
        return response.read().decode("utf-8", errors="replace")


def doi_to_pmid(doi: str) -> str | None:
    xml = fetch_text(
        PUBMED_ESEARCH,
        {"db": "pubmed", "term": f"{doi}[doi]", "retmode": "xml", "retmax": "1"},
    )
    root = ET.fromstring(xml)
    id_node = root.find(".//Id")
    return id_node.text if id_node is not None and id_node.text else None


def text_or_empty(node: ET.Element | None) -> str:
    if node is None:
        return ""
    return " ".join("".join(node.itertext()).split())


def pubmed_record(pmid: str) -> dict[str, object]:
    xml = fetch_text(
        PUBMED_EFETCH,
        {"db": "pubmed", "id": pmid, "retmode": "xml", "rettype": "abstract"},
    )
    root = ET.fromstring(xml)
    article = root.find(".//PubmedArticle")
    if article is None:
        return {"pmid": pmid, "lookup_status": "not_found", "raw_xml": xml}

    citation = article.find(".//MedlineCitation")
    article_node = citation.find("Article") if citation is not None else None
    journal = article_node.find("Journal") if article_node is not None else None
    journal_issue = journal.find("JournalIssue") if journal is not None else None
    pub_date = journal_issue.find("PubDate") if journal_issue is not None else None
    year = text_or_empty(pub_date.find("Year") if pub_date is not None else None)
    if not year and pub_date is not None:
        year = text_or_empty(pub_date.find("MedlineDate"))

    title = text_or_empty(article_node.find("ArticleTitle") if article_node is not None else None)
    abstract_parts = []
    for abstract in article.findall(".//Abstract/AbstractText"):
        label = abstract.attrib.get("Label")
        text = text_or_empty(abstract)
        if label and text:
            abstract_parts.append(f"{label}: {text}")
        elif text:
            abstract_parts.append(text)

    authors = []
    for author in article.findall(".//Author")[:8]:
        last = text_or_empty(author.find("LastName"))
        fore = text_or_empty(author.find("ForeName"))
        collective = text_or_empty(author.find("CollectiveName"))
        if collective:
            authors.append(collective)
        elif last:
            authors.append(f"{fore} {last}".strip())

    doi = ""
    for article_id in article.findall(".//ArticleId"):
        if article_id.attrib.get("IdType") == "doi":
            doi = text_or_empty(article_id)
            break

    pub_types = [text_or_empty(node) for node in article.findall(".//PublicationType") if text_or_empty(node)]
    mesh = [text_or_empty(node.find("DescriptorName")) for node in article.findall(".//MeshHeading")]
    mesh = [item for item in mesh if item]

    return {
        "pmid": pmid,
        "doi": doi,
        "title": title,
        "year": year,
        "journal": text_or_empty(journal.find("Title") if journal is not None else None),
        "journal_iso": text_or_empty(journal.find("ISOAbbreviation") if journal is not None else None),
        "publication_types": pub_types,
        "authors": authors,
        "abstract": " ".join(abstract_parts),
        "mesh_terms": mesh,
        "lookup_status": "ok",
        "api_source": "pubmed_efetch",
    }


def main() -> int:
    records: list[dict[str, object]] = []
    seen: set[tuple[str, str]] = set()
    for candidate in CANDIDATES:
        pmid = candidate.lookup if candidate.lookup_type == "pmid" else doi_to_pmid(candidate.lookup)
        time.sleep(0.12)
        if pmid:
            record = pubmed_record(pmid)
        else:
            record = {
                "pmid": "",
                "doi": candidate.lookup if candidate.lookup_type == "doi" else "",
                "lookup_status": "not_found",
                "api_source": "pubmed_esearch",
            }
        time.sleep(0.12)
        dedupe_key = (str(record.get("pmid", "")), str(record.get("doi", "")).lower())
        duplicate = dedupe_key in seen and dedupe_key != ("", "")
        seen.add(dedupe_key)
        record = {
            "candidate_key": candidate.key,
            "question": candidate.question,
            "lookup_type": candidate.lookup_type,
            "lookup": candidate.lookup,
            "role_hint": candidate.role_hint,
            "dedupe_duplicate": duplicate,
            **record,
        }
        records.append(record)

    OUT_JSON.write_text(json.dumps(records, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")

    fields = [
        "candidate_key",
        "question",
        "lookup_type",
        "lookup",
        "role_hint",
        "dedupe_duplicate",
        "lookup_status",
        "api_source",
        "pmid",
        "doi",
        "title",
        "year",
        "journal_iso",
        "publication_types",
        "authors",
        "abstract",
    ]
    with OUT_CSV.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=fields, extrasaction="ignore")
        writer.writeheader()
        for record in records:
            row = dict(record)
            row["publication_types"] = "; ".join(row.get("publication_types") or [])
            row["authors"] = "; ".join(row.get("authors") or [])
            writer.writerow(row)

    print(f"records: {len(records)}")
    print(f"json: {OUT_JSON}")
    print(f"csv: {OUT_CSV}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
