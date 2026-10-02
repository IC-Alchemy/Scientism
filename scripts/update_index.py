"""Regenerate wiki/index.md from page frontmatter.

The index is the vault's primary navigation surface:
- every page is listed under its category with a one-line summary;
- source pages (200+) are grouped into topic clusters by tag so the list is
  browsable rather than one flat alphabetical wall;
- a short Entry points section links the vault map, section maps, and log.

--write replaces only the body of wiki/index.md; its frontmatter is preserved.
"""
from __future__ import annotations

import argparse
import datetime as dt
from dataclasses import dataclass
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[1]
WIKI_DIR = ROOT / "wiki"
INDEX_PATH = WIKI_DIR / "index.md"

CATEGORY_ORDER = [
    ("synthesis", "Synthesis"),
    ("concept", "Concept"),
    ("entity", "Entity"),
    ("comparison", "Comparison"),
]

# Topic clusters for source pages. First match wins; a page joins the first
# cluster whose keyword appears in one of its tags. Anything unmatched falls
# through to "Other sources".
SOURCE_CLUSTERS: list[tuple[str, tuple[str, ...]]] = [
    (
        "Herpesviruses: HSV, VZV, EBV, Kaposi sarcoma",
        (
            "hsv", "herpes-simplex", "genital-herpes", "cold-sore", "labialis",
            "varicella", "zoster", "vzv", "chickenpox", "shingles",
            "ebv", "epstein-barr", "burkitt", "mononucleosis",
            "kaposi", "hhv-8", "kshv", "herpesvirus",
        ),
    ),
    (
        "HIV, AIDS, and antiretroviral therapy",
        (
            "aids", "hiv", "azt", "zidovudine", "didanosine", "lamivudine",
            "hemophilia", "haemophilia", "transfusion", "cd4", "t4", "lav",
            "htlv", "antiretroviral", "pneumocystis",
        ),
    ),
    (
        "HPV and cervical cancer",
        ("hpv", "papillomavirus", "cervical", "cervix", "cin", "p16", "hc2", "tumor-dna"),
    ),
    (
        "Hepatitis A, B, and C",
        (
            "hepatitis", "hav", "hbv", "hcv", "non-a-non-b", "australia-antigen",
            "willowbrook", "cr326", "ms-1", "ms-2", "hbag", "hbsag",
        ),
    ),
    (
        "SARS, MERS, and coronaviruses",
        ("sars", "covid", "coronavirus", "mers", "ncov"),
    ),
    ("Rabies", ("rabies", "negri")),
    ("Poliomyelitis", ("polio",)),
    ("Measles", ("measles", "rubeola")),
    ("Influenza", ("influenza", "spanish-flu", "flu")),
    (
        "Smallpox, variola, and vaccinia",
        ("smallpox", "variola", "vaccinia", "cowpox", "variolation"),
    ),
    (
        "Respiratory and enteric viruses",
        (
            "rsv", "respiratory", "bronchiolitis", "coryza", "cca",
            "norovirus", "norwalk", "rotavirus", "gastroenteritis",
            "coxsackie", "enterovirus", "ev71", "hand-foot-mouth", "hfmd",
        ),
    ),
    (
        "Germ theory and historical debate",
        (
            "germ-theory", "koch", "pasteur", "jenner", "viroliegy",
            "revisionist", "leverson", "scobey", "history",
        ),
    ),
    (
        "Replication, methods, and evidence standards",
        (
            "replication", "reproducibility", "methodology", "placebo",
            "endpoint", "trial-design", "evidence-standard", "scientific-method",
            "sequencing", "contamination",
        ),
    ),
    ("Vaccines", ("vaccine", "vaccination", "immunization")),
]


@dataclass
class Page:
    path: Path
    title: str
    category: str
    summary: str
    updated: str
    sources: str | None
    tags: list[str]


def clean_date(value) -> str:
    if isinstance(value, dt.date):
        return value.isoformat()
    return str(value).split("T", 1)[0]


def clean_text(value) -> str:
    return " ".join(str(value).split())


def collect_pages() -> list[Page]:
    pages: list[Page] = []
    for path in sorted(WIKI_DIR.rglob("*.md")):
        rel = path.relative_to(WIKI_DIR)
        if rel.parts[0] == ".templates" or rel.name in {"index.md", "log.md"}:
            continue
        text = path.read_text(encoding="utf-8")
        if not text.startswith("---\n"):
            continue
        end = text.find("\n---\n", 4)
        if end == -1:
            continue
        try:
            fm = yaml.safe_load(text[4:end])
        except yaml.YAMLError:
            continue
        if not isinstance(fm, dict):
            continue
        pages.append(
            Page(
                path=rel,
                title=clean_text(fm.get("title") or path.stem),
                category=str(fm.get("category", "unknown")),
                summary=clean_text(fm.get("summary") or ""),
                updated=clean_date(fm.get("updated")) if fm.get("updated") else "",
                sources=fm.get("sources"),
                tags=[str(t) for t in (fm.get("tags") or [])],
            )
        )
    return pages


def link_for(page: Page) -> str:
    target = page.path.with_suffix("").as_posix()
    safe_title = page.title.replace("|", "/")
    return f"[[{target}|{safe_title}]]"


def entry_for(page: Page, show_source_count: bool) -> str:
    line = f"- {link_for(page)}"
    if page.summary:
        line += f" — {page.summary}"
    suffix_parts: list[str] = []
    if show_source_count and page.sources and int(page.sources) > 1:
        suffix_parts.append(f"{page.sources} sources")
    if page.updated:
        suffix_parts.append(f"upd {page.updated}")
    if suffix_parts:
        line += f" _({' · '.join(suffix_parts)})_"
    return line


def cluster_for(page: Page) -> str:
    for name, keywords in SOURCE_CLUSTERS:
        for tag in page.tags:
            if any(kw in tag for kw in keywords):
                return name
    return "Other sources"


def render_index(pages: list[Page], stamp: str) -> str:
    by_category: dict[str, list[Page]] = {}
    for page in pages:
        by_category.setdefault(page.category, []).append(page)

    lines = [
        "# Index — Scientism",
        "",
        f"_Auto-generated {stamp} • {len(pages)} pages_",
        "",
        "> Content-oriented catalog of every page in `wiki/`, grouped by category.",
        "> Source pages are grouped by topic cluster. Regenerate with",
        "> `python scripts/update_index.py --write`. Answer queries by reading",
        "> this file first, then drilling into relevant pages.",
        "",
        "## Entry points",
        "",
        "- [[wiki|Vault map]] — what each folder holds and where to start.",
        "- [[synthesis/synthesis|Synthesis map]] · [[concepts/concepts|Concepts]] · [[entities/entities|Entities]] · [[comparisons/comparisons|Comparisons]] · [[sources/sources|Source map]]",
        "- [[synthesis/viral-disease-causation-evidence-ladder|Viral Disease Causation Evidence Ladder]] — the vault's core rung-by-rung framework.",
        "- [[synthesis/vault-maintenance-guide|Vault Maintenance Guide]] — ingest, triage, and lint conventions.",
        "- [[log|Operation log]] — append-only record of every operation.",
        "",
    ]

    for category_key, category_label in CATEGORY_ORDER:
        items = sorted(by_category.get(category_key, []), key=lambda p: p.title.lower())
        if not items:
            continue
        lines.append(f"## {category_label} ({len(items)})")
        lines.append("")
        show_count = category_key == "synthesis"
        for page in items:
            lines.append(entry_for(page, show_source_count=show_count))
        lines.append("")

    sources = sorted(by_category.get("source", []), key=lambda p: p.title.lower())
    if sources:
        lines.append(f"## Source ({len(sources)})")
        lines.append("")
        clusters: dict[str, list[Page]] = {}
        for page in sources:
            clusters.setdefault(cluster_for(page), []).append(page)
        for name, _ in SOURCE_CLUSTERS:
            members = clusters.pop(name, None)
            if members:
                lines.append(f"### {name} ({len(members)})")
                lines.append("")
                for page in members:
                    lines.append(entry_for(page, show_source_count=False))
                lines.append("")
        if clusters:
            other = [page for members in clusters.values() for page in members]
            lines.append(f"### Other sources ({len(other)})")
            lines.append("")
            for page in sorted(other, key=lambda p: p.title.lower()):
                lines.append(entry_for(page, show_source_count=False))
            lines.append("")

    return "\n".join(lines).rstrip() + "\n"


def write_index(rendered: str) -> None:
    """Replace only the body of index.md, preserving its frontmatter."""
    text = INDEX_PATH.read_text(encoding="utf-8")
    if text.startswith("---\n"):
        end = text.find("\n---\n", 4)
        if end != -1:
            INDEX_PATH.write_text(text[: end + 5] + rendered, encoding="utf-8")
            return
    INDEX_PATH.write_text(rendered, encoding="utf-8")


def main() -> int:
    parser = argparse.ArgumentParser(description="Regenerate wiki/index.md from page frontmatter.")
    parser.add_argument("--write", action="store_true", help="Write the rendered index back to wiki/index.md.")
    parser.add_argument(
        "--date",
        default=dt.date.today().isoformat(),
        help="Date stamp to embed in the index header (default: today).",
    )
    args = parser.parse_args()

    pages = collect_pages()
    rendered = render_index(pages, args.date)
    if args.write:
        write_index(rendered)
    else:
        print(rendered, end="")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
