"""Normalize bare-basename wikilinks to full-path wikilinks.

Obsidian resolves [[page]] by basename, but the vault convention (and
lint_wiki.py) uses full-path links like [[sources/page]] so links stay
unambiguous outside Obsidian. This script rewrites bare links to the
full path of the unique page carrying that basename. Bare names that
match more than one page (currently: empirical-evidence) are reported
and left untouched for manual disambiguation.

Dry run by default; pass --write to apply.
"""

from __future__ import annotations

import argparse
import re
from collections import defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
WIKI_DIR = ROOT / "wiki"
WIKILINK_RE = re.compile(r"\[\[([^\]|#]+)(#[^\]|]+)?(?:\|[^\]]*)?\]\]")


def collect_pages() -> dict[str, list[str]]:
    by_basename: dict[str, list[str]] = defaultdict(list)
    for path in sorted(WIKI_DIR.rglob("*.md")):
        rel = path.relative_to(WIKI_DIR)
        if rel.parts[0] == ".templates":
            continue
        by_basename[path.stem].append(rel.with_suffix("").as_posix())
    return by_basename


def normalize_text(text: str, by_basename: dict[str, list[str]]) -> tuple[str, list[str], int]:
    changes: list[str] = []
    skipped: list[str] = []

    def replace(match: re.Match) -> str:
        target, anchor = match.group(1), match.group(2) or ""
        stripped = target.strip()
        if stripped.startswith(("http://", "https://")) or "/" in stripped:
            return match.group(0)
        candidates = by_basename.get(stripped, [])
        if len(candidates) == 1:
            full = candidates[0]
            if full == stripped:
                return match.group(0)
            changes.append(f"{stripped} -> {full}")
            return match.group(0).replace(f"[[{target}", f"[[{full}", 1)
        skipped.append(stripped)
        return match.group(0)

    new_text = WIKILINK_RE.sub(replace, text)
    return new_text, skipped, len(changes)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--write", action="store_true", help="Rewrite files in place.")
    args = parser.parse_args()

    by_basename = collect_pages()
    ambiguous = {name for name, paths in by_basename.items() if len(paths) > 1}
    total_changes = 0
    all_skipped: defaultdict[str, int] = defaultdict(int)

    for path in sorted(WIKI_DIR.rglob("*.md")):
        rel = path.relative_to(WIKI_DIR)
        if rel.parts[0] == ".templates" or rel.name in {"index.md", "log.md"}:
            continue
        text = path.read_text(encoding="utf-8")
        new_text, skipped, n = normalize_text(text, by_basename)
        total_changes += n
        for name in skipped:
            all_skipped[name] += 1
        if args.write and new_text != text:
            path.write_text(new_text, encoding="utf-8", newline="\n")

    mode = "rewrote" if args.write else "would rewrite"
    print(f"{mode} {total_changes} bare links across wiki/")
    if ambiguous:
        print(f"ambiguous basenames (untouched): {sorted(ambiguous)}")
    if all_skipped:
        for name, count in sorted(all_skipped.items()):
            print(f"  skipped {count}x [[{name}]] — no unique page match")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
