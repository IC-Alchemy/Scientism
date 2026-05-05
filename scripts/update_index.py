from __future__ import annotations

import argparse
import datetime as dt
from dataclasses import dataclass
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
WIKI_DIR = ROOT / "wiki"

CATEGORY_ORDER = [
    ("synthesis", "Synthesis"),
    ("concept", "Concept"),
    ("entity", "Entity"),
    ("source", "Source"),
    ("comparison", "Comparison"),
]


@dataclass
class Page:
    path: Path
    title: str
    category: str
    summary: str
    updated: str
    sources: str | None


def parse_frontmatter(text: str) -> dict[str, str]:
    if not text.startswith("---\n"):
        return {}

    end = text.find("\n---\n", 4)
    if end == -1:
        return {}

    frontmatter = text[4:end].splitlines()
    data: dict[str, str] = {}
    key: str | None = None
    buffer: list[str] = []

    def flush() -> None:
        nonlocal key, buffer
        if key is None:
            return
        value = "\n".join(buffer).strip()
        if value.startswith('"') and value.endswith('"'):
            value = value[1:-1]
        data[key] = value
        key = None
        buffer = []

    for line in frontmatter:
        if not line.strip():
            continue
        if line.startswith(" ") or line.startswith("\t"):
            if key is not None:
                buffer.append(line.strip())
            continue
        if ":" not in line:
            continue
        flush()
        raw_key, raw_value = line.split(":", 1)
        key = raw_key.strip()
        buffer = [raw_value.strip()]
    flush()
    return data


def collect_pages() -> list[Page]:
    pages: list[Page] = []
    for path in sorted(WIKI_DIR.rglob("*.md")):
        rel = path.relative_to(WIKI_DIR)
        if rel.parts[0] == ".templates":
            continue
        if rel.name in {"index.md", "log.md"}:
            continue
        frontmatter = parse_frontmatter(path.read_text(encoding="utf-8"))
        if not frontmatter:
            continue
        pages.append(
            Page(
                path=rel,
                title=frontmatter.get("title", path.stem),
                category=frontmatter.get("category", "unknown"),
                summary=frontmatter.get("summary", "").strip(),
                updated=frontmatter.get("updated", ""),
                sources=frontmatter.get("sources"),
            )
        )
    return pages


def link_for(page: Page) -> str:
    target = page.path.with_suffix("").as_posix()
    return f"[[{target}|{page.title}]]"


def render_index(pages: list[Page], stamp: str) -> str:
    by_category: dict[str, list[Page]] = {}
    for page in pages:
        by_category.setdefault(page.category, []).append(page)

    lines = [
        "# Index — Scientism",
        "",
        f"_Auto-generated {stamp} • {len(pages)} pages_",
        "",
        "> Content-oriented catalog of every page in `wiki/`. Updated by",
        "> `scripts/update_index.py` or during `/wiki-ingest`. Answer queries",
        "> by reading this file first, then drilling into relevant pages.",
        "",
    ]

    for category_key, category_label in CATEGORY_ORDER:
        items = sorted(by_category.get(category_key, []), key=lambda page: page.title.lower())
        if not items:
            continue
        lines.append(f"## {category_label} ({len(items)})")
        lines.append("")
        for page in items:
            suffix_parts: list[str] = []
            if page.sources:
                suffix_parts.append(f"{page.sources} sources")
            if page.updated:
                suffix_parts.append(f"upd {page.updated}")
            suffix = ""
            if suffix_parts:
                suffix = f" _({' · '.join(suffix_parts)})_"
            lines.append(f"- {link_for(page)} — {page.summary}{suffix}")
        lines.append("")

    return "\n".join(lines).rstrip() + "\n"


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
        (WIKI_DIR / "index.md").write_text(rendered, encoding="utf-8")
    else:
        print(rendered, end="")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
