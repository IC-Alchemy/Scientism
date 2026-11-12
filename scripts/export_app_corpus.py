#!/usr/bin/env python3
"""Export wiki/ and raw/ markdown into JSON bundles for the Scientism web app."""

from __future__ import annotations

import json
import re
import sys
from datetime import date
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
WIKI = ROOT / "wiki"
RAW = ROOT / "raw"
OUT = ROOT / "app" / "public" / "data"

FRONTMATTER_RE = re.compile(r"\A---\r?\n(.*?)\r?\n---\r?\n", re.DOTALL)
YAML_LINE = re.compile(r"^([A-Za-z0-9_-]+):\s*(.*)$")


def parse_simple_yaml(block: str) -> dict:
    meta: dict = {}
    key: str | None = None
    for line in block.splitlines():
        if not line.strip():
            continue
        if line.startswith("  - ") and key == "tags":
            tags = meta.get("tags")
            if not isinstance(tags, list):
                tags = [] if not tags else [str(tags)]
                meta["tags"] = tags
            tags.append(line.strip()[2:].strip())
            continue
        m = YAML_LINE.match(line)
        if not m:
            continue
        key, val = m.group(1), m.group(2).strip()
        if val.startswith("[") and val.endswith("]"):
            inner = val[1:-1].strip()
            meta[key] = [p.strip().strip("'\"") for p in inner.split(",") if p.strip()] if inner else []
        elif val in ("true", "false"):
            meta[key] = val == "true"
        else:
            meta[key] = val.strip("'\"")
    return meta


def split_frontmatter(text: str) -> tuple[dict, str]:
    m = FRONTMATTER_RE.match(text)
    if not m:
        return {}, text
    return parse_simple_yaml(m.group(1)), text[m.end() :]


def wiki_slug(rel: Path) -> str:
    return rel.as_posix().removesuffix(".md")


def export_wiki() -> list[dict]:
    pages: list[dict] = []
    for path in sorted(WIKI.rglob("*.md")):
        if ".templates" in path.parts:
            continue
        rel = path.relative_to(WIKI)
        text = path.read_text(encoding="utf-8", errors="replace")
        meta, body = split_frontmatter(text)
        category = meta.get("category") or _infer_category(rel)
        pages.append(
            {
                "id": wiki_slug(rel),
                "path": rel.as_posix(),
                "layer": "wiki",
                "title": meta.get("title") or rel.stem.replace("-", " ").title(),
                "category": category,
                "summary": meta.get("summary", ""),
                "tags": meta.get("tags", []) if isinstance(meta.get("tags"), list) else [],
                "updated": meta.get("updated", ""),
                "claim_status": meta.get("claim_status", ""),
                "claim_type": meta.get("claim_type", ""),
                "source_tier": meta.get("source_tier", ""),
                "sources": meta.get("sources", ""),
                "body": body.strip(),
            }
        )
    return pages


def _infer_category(rel: Path) -> str:
    if not rel.parts:
        return "meta"
    mapping = {
        "concepts": "concept",
        "entities": "entity",
        "sources": "source",
        "synthesis": "synthesis",
        "comparisons": "comparison",
    }
    return mapping.get(rel.parts[0], "meta")


def export_raw() -> list[dict]:
    items: list[dict] = []
    for path in sorted(RAW.rglob("*")):
        if not path.is_file():
            continue
        rel = path.relative_to(RAW)
        ext = path.suffix.lower()
        entry: dict = {
            "id": f"raw/{rel.as_posix()}",
            "path": rel.as_posix(),
            "layer": "raw",
            "title": path.stem.replace("-", " ").replace("_", " "),
            "category": "raw",
            "summary": "",
            "kind": ext.lstrip(".") or "file",
            "size_bytes": path.stat().st_size,
        }
        if ext in (".md", ".html") and path.stat().st_size < 2_000_000:
            text = path.read_text(encoding="utf-8", errors="replace")
            meta, body = split_frontmatter(text) if ext == ".md" else ({}, text)
            if meta.get("title"):
                entry["title"] = meta["title"]
            entry["summary"] = meta.get("summary", "")[:300]
            entry["body"] = body.strip()
        items.append(entry)
    return items


def main() -> int:
    OUT.mkdir(parents=True, exist_ok=True)
    wiki_pages = export_wiki()
    raw_items = export_raw()

    vault_map = ROOT / "scientism-vault-map.data.json"
    if vault_map.is_file():
        (OUT / "vault-map.json").write_text(vault_map.read_text(encoding="utf-8"), encoding="utf-8")

    index_path = WIKI / "index.md"
    index_blurb = ""
    if index_path.is_file():
        _, body = split_frontmatter(index_path.read_text(encoding="utf-8"))
        index_blurb = body[:4000]

    manifest = {
        "generated": date.today().isoformat(),
        "title": "Scientism Research Wiki",
        "description": (
            "A research vault on scientism, evidence standards, replication, "
            "and disputed virus-disease attribution claims."
        ),
        "stats": {
            "wiki_pages": len(wiki_pages),
            "raw_items": len(raw_items),
            "raw_markdown": sum(1 for r in raw_items if r.get("body")),
        },
        "index_excerpt": index_blurb,
        "categories": _category_counts(wiki_pages),
    }

    (OUT / "manifest.json").write_text(json.dumps(manifest, indent=2), encoding="utf-8")
    (OUT / "wiki-pages.json").write_text(json.dumps(wiki_pages, separators=(",", ":")), encoding="utf-8")
    (OUT / "raw-items.json").write_text(json.dumps(raw_items, separators=(",", ":")), encoding="utf-8")

    print(
        f"Exported {len(wiki_pages)} wiki pages and {len(raw_items)} raw items → {OUT}",
        file=sys.stderr,
    )
    return 0


def _category_counts(pages: list[dict]) -> dict[str, int]:
    counts: dict[str, int] = {}
    for p in pages:
        cat = p.get("category") or "other"
        counts[cat] = counts.get(cat, 0) + 1
    return dict(sorted(counts.items(), key=lambda x: (-x[1], x[0])))


if __name__ == "__main__":
    raise SystemExit(main())
