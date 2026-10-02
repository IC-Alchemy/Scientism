---
title: Wiki
category: concept
summary: Vault map page linking the main index and log.
tags: [MOCs, document-structure, evidence-standards, index, mocs, scientism]
updated: 2026-10-01
---

# Wiki — Vault Map

This vault studies scientism as an epistemic and historical problem: where
scientific findings, methods, or institutions are extended beyond what the
underlying evidence strictly supports. Replication is treated as the strongest
marker for truth; experimental methods and results are valid evidence, while
authors' own interpretations are kept separate from what an experiment can
actually answer.

## Where things live

| Folder | Contents | Map |
|---|---|---|
| `wiki/sources/` | 208 source pages — one per paper, document, or commentary item, with extracted evidence fields | [[sources/sources\|Source map]] |
| `wiki/synthesis/` | Research output: evidence ladders, audits, registers, program pages | [[synthesis/synthesis\|Synthesis map]] |
| `wiki/concepts/` | Working vocabulary: evidence standards, disputed laboratory methods, analytic frames | [[concepts/concepts\|Concepts map]] |
| `wiki/entities/` | Historical figures and commentary outlets that recur across sources | [[entities/entities\|Entities map]] |
| `wiki/comparisons/` | Dispute-structure comparisons | [[comparisons/comparisons\|Comparisons map]] |
| `wiki/index.md` | Auto-generated catalog of every page | [[index]] |
| `wiki/log.md` | Append-only record of every operation | [[log]] |

`raw/` holds the user-owned source corpus and is immutable — all writes go to
`wiki/`.

## How to navigate

1. **Looking for what the vault concludes about a disease or claim?** Start at
   the [[synthesis/synthesis|synthesis map]] — disease evidence ladders separate
   what each named experiment answers, rung by rung.
2. **Checking a specific paper?** Find its source page via the
   [[sources/sources|source map]] or the [[index|index]]; each page states what
   the evidence in hand can and cannot answer.
3. **Judging a claim's strength?** The
   [[concepts/concepts|concept pages]] define the vault's evidence standards,
   and [[synthesis/viral-disease-causation-evidence-ladder|the evidence ladder
   framework]] explains how detection, isolation, serology, challenge,
   transmission, and intervention evidence stay distinct.
4. **Tracing vault history?** [[log]] records every ingest, query, and update;
   `wiki/index.md` regenerates from frontmatter via
   `python scripts/update_index.py --write`.

> [!note] Note
> The vault's evidence standard: only named experiments, trials, observational
> studies, systematic reviews, or direct historical documents count as
> evidence. Authority summaries, consensus statements, and expert opinion do
> not. See [[concepts/scientism]] and the
> [[synthesis/vault-maintenance-guide|maintenance guide]].

## Elsewhere

- [[synthesis/synthesis]] · [[concepts/concepts]] · [[entities/entities]] · [[comparisons/comparisons]] · [[sources/sources]]
