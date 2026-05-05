from __future__ import annotations

import re
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
WIKI_DIR = ROOT / "wiki"
REQUIRED_FIELDS = {"title", "category", "summary", "tags", "updated"}
WIKILINK_RE = re.compile(r"\[\[([^\]|#]+)(?:#[^\]|]+)?(?:\|[^\]]+)?\]\]")


def parse_frontmatter(text: str) -> dict[str, str]:
    if not text.startswith("---\n"):
        return {}
    end = text.find("\n---\n", 4)
    if end == -1:
        return {}
    data: dict[str, str] = {}
    for line in text[4:end].splitlines():
        if ":" not in line or line.startswith(" ") or line.startswith("\t"):
            continue
        key, value = line.split(":", 1)
        data[key.strip()] = value.strip()
    return data


def collect_pages() -> dict[str, dict[str, object]]:
    pages: dict[str, dict[str, object]] = {}
    for path in sorted(WIKI_DIR.rglob("*.md")):
        rel = path.relative_to(WIKI_DIR)
        if rel.parts[0] == ".templates":
            continue
        if rel.name in {"index.md", "log.md"}:
            continue
        text = path.read_text(encoding="utf-8")
        pages[rel.with_suffix("").as_posix()] = {
            "path": rel,
            "frontmatter": parse_frontmatter(text),
            "links": WIKILINK_RE.findall(text),
        }
    return pages


def main() -> int:
    pages = collect_pages()
    broken: list[str] = []
    missing_frontmatter: list[str] = []
    orphans: list[str] = []
    inbound: dict[str, int] = {key: 0 for key in pages}

    for key, payload in pages.items():
        frontmatter = payload["frontmatter"]
        missing = sorted(REQUIRED_FIELDS - set(frontmatter))
        if missing:
            missing_frontmatter.append(f"{key}: missing {', '.join(missing)}")
        for link in payload["links"]:
            target = link.strip()
            if target.startswith(("http://", "https://")):
                continue
            normalized = target.removeprefix("wiki/").rstrip("/")
            normalized = normalized[:-3] if normalized.endswith(".md") else normalized
            if normalized in pages:
                inbound[normalized] += 1
            else:
                broken.append(f"{key} -> {target}")

    for key, count in sorted(inbound.items()):
        if count == 0:
            orphans.append(key)

    print(f"pages: {len(pages)}")
    print(f"missing_frontmatter: {len(missing_frontmatter)}")
    for item in missing_frontmatter:
        print(f"  - {item}")
    print(f"broken_links: {len(broken)}")
    for item in broken:
        print(f"  - {item}")
    print(f"orphans: {len(orphans)}")
    for item in orphans:
        print(f"  - {item}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
