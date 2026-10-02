"""Normalize formatting across wiki/ pages.

Fixes, without changing page content:
- Frontmatter: folded scalars (``title: >-`` blocks) become single-line values,
  ISO timestamps (``2026-05-31T00:00:00.000Z``) become plain dates, invalid
  unquoted values containing ": " get quoted, null-valued keys are dropped,
  tags are sorted/deduped, and keys are emitted in a canonical order.
- Doubled frontmatter: pages where a tagger plugin prepended its own block in
  front of the original one are merged (original values win; tags are unioned
  and the duplicate block is removed from the body).
- Body: ``> Note:`` / ``> Warning:`` blockquotes become Obsidian callouts
  (``> [!note] Note``), a few heading variants are unified, 3+ blank-line runs
  collapse to two, and trailing whitespace is stripped.

``updated:`` dates are reformatted but not changed to today: this pass is
formatting-only, and the date records when page content last changed.

Dry run by default; pass --write to apply.
"""
from __future__ import annotations

import argparse
import datetime as dt
import re
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[1]
WIKI_DIR = ROOT / "wiki"

KEY_ORDER = [
    "title",
    "category",
    "summary",
    "tags",
    "sources",
    "updated",
    "claim_status",
    "claim_type",
    "source_tier",
    "evidence_role",
    "source_path",
    "source_date",
    "authors",
    "ingested",
    "pmid",
    "pmcid",
    "doi",
]

# Exact H2 lines that mean the same thing but were written several ways.
HEADING_RENAMES = {
    "Related pages": "Related",
    "What this wiki can conclude": "What this wiki currently concludes",
    "What this source can answer": "What the source can answer",
    "What question the source is capable of answering": "What the source can answer",
    "API abstract": "Indexed abstract",
    "Source type and scope": "Source type",
}

CALLOUT_RE = re.compile(r"^(>+[ \t]*)(Note|Warning|Tip|Caution):[ \t]+(.*)$")


def split_frontmatter(text: str) -> tuple[str | None, str]:
    """Return (raw_frontmatter, body), or (None, text) if there is no block."""
    if not text.startswith("---\n"):
        return None, text
    end = text.find("\n---\n", 4)
    if end == -1:
        return None, text
    return text[4:end], text[end + 5 :]


def parse_block(raw: str) -> dict | None:
    """Parse one raw frontmatter block, quoting invalid values if needed."""
    try:
        data = yaml.safe_load(raw)
    except yaml.YAMLError:
        fixed: list[str] = []
        for line in raw.splitlines():
            m = re.match(r"^([A-Za-z][\w-]*):[ \t]+(.+)$", line)
            if m and ": " in m.group(2) and not re.match(r'^["\'>\[\{-]', m.group(2)):
                line = f'{m.group(1)}: "{m.group(2).replace(chr(34), chr(92) + chr(34))}"'
            fixed.append(line)
        try:
            data = yaml.safe_load("\n".join(fixed))
        except yaml.YAMLError:
            return None
    return data if isinstance(data, dict) else None


def load_page(text: str) -> tuple[dict | None, str]:
    """Parse frontmatter, merging a doubled (plugin-prepended) block if present."""
    raw, body = split_frontmatter(text)
    if raw is None:
        return None, body
    first = parse_block(raw)

    stripped = body.lstrip("\n")
    if first is not None and stripped.startswith("---\n"):
        end2 = stripped.find("\n---\n", 4)
        if end2 != -1:
            second = parse_block(stripped[4:end2])
            if second is not None and ("category" in second or "title" in second):
                merged = {**first, **second}
                merged["tags"] = list((first.get("tags") or []) + (second.get("tags") or []))
                return merged, stripped[end2 + 5 :]
    return first, body


def scalar(value: str) -> str:
    """Emit a YAML scalar on one line, quoted only when required."""
    out = yaml.dump(value, width=10**6, allow_unicode=True, default_flow_style=False)
    if out.endswith("\n...\n"):
        out = out[: -len("\n...\n")]
    return out.strip("\n")


def normalize_date(value) -> str:
    text = value.isoformat() if isinstance(value, (dt.date, dt.datetime)) else str(value)
    return text.split("T", 1)[0]


def build_frontmatter(data: dict) -> str:
    seen: set[str] = set()
    keys = [k for k in KEY_ORDER if k in data and not (k in seen or seen.add(k))]
    keys += [k for k in data if k not in keys]

    lines: list[str] = []
    for key in keys:
        value = data[key]
        if value is None:
            continue
        if key in {"updated", "ingested", "source_date"}:
            lines.append(f"{key}: {normalize_date(value)}")
        elif key in {"tags", "authors"} and isinstance(value, list):
            items = sorted({str(t).strip().lower() for t in value if str(t).strip()})
            if not items:
                lines.append(f"{key}: []")
            else:
                lines.append(f"{key}:")
                lines.extend(f"  - {item}" for item in items)
        elif isinstance(value, bool):
            lines.append(f"{key}: {'true' if value else 'false'}")
        elif isinstance(value, (int, float)):
            lines.append(f"{key}: {value}")
        elif isinstance(value, str):
            lines.append(f"{key}: {scalar(' '.join(value.split()))}")
        else:
            lines.append(f"{key}: {scalar(str(value))}")
    return "\n".join(lines)


def transform_body(body: str) -> tuple[str, int, int]:
    callouts = headings = 0
    out: list[str] = []
    for line in body.splitlines():
        if not CALLOUT_RE.match(line) and re.match(r"^## .+$", line):
            name = line[3:].strip()
            if name in HEADING_RENAMES:
                line = f"## {HEADING_RENAMES[name]}"
                headings += 1
        m = CALLOUT_RE.match(line)
        if m:
            prefix, kind, rest = m.groups()
            line = f"{prefix}[!{kind.lower()}] {kind}\n{prefix}{rest}"
            callouts += 1
        out.append(line.rstrip())
    text = "\n".join(out)
    text = re.sub(r"\n{3,}", "\n\n", text)
    return text, callouts, headings


def process(path: Path, write: bool) -> tuple[bool, str]:
    text = path.read_text(encoding="utf-8")
    data, body = load_page(text)
    if data is None:
        return False, "no/invalid frontmatter"

    fm = build_frontmatter(data)
    body, callouts, headings = transform_body(body)
    new_text = f"---\n{fm}\n---\n{body}"

    if new_text != text:
        if write:
            path.write_text(new_text, encoding="utf-8")
        note = []
        if any(not line.startswith(("tags:", "  - ")) for line in fm.splitlines()):
            note.append("frontmatter")
        if callouts:
            note.append(f"{callouts} callouts")
        if headings:
            note.append(f"{headings} headings")
        return True, ", ".join(note) or "whitespace"
    return False, "clean"


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--write", action="store_true", help="Apply changes (default: dry run).")
    args = parser.parse_args()

    changed = 0
    for path in sorted(WIKI_DIR.rglob("*.md")):
        rel = path.relative_to(WIKI_DIR)
        if rel.parts[0] == ".templates" or rel.name in {"index.md", "log.md"}:
            continue
        touched, note = process(path, args.write)
        if touched:
            changed += 1
            print(f"{rel}: {note}")
    print(f"\n{'Wrote' if args.write else 'Would change'} {changed} pages.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
