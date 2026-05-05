# Log — Scientism

> Append-only timeline. Every LLM operation leaves an entry here.
>
> Format: `## [YYYY-MM-DD] <op> | <title>` followed by an optional detail line.
> Valid ops: `ingest`, `query`, `lint`, `create`, `update`, `delete`, `note`.
>
> Grep the last 10 entries: `grep "^## \[" log.md | tail -10`

## [2026-05-04] note | Vault initialized
Topic: **Scientism**. Layers created: `raw/`, `wiki/{entities,concepts,sources,comparisons,synthesis}`.
Schema loader: `CLAUDE.md` + `AGENTS.md` + `.cursorrules`.

## [2026-05-04] update | Scientism seed source ingested and schema specialized

Updated AGENTS.md and CLAUDE.md. Added source, concept, entity, comparison, and synthesis starter pages from raw/Scientism.md. Regenerated wiki/index.md.

## [2026-05-04] ingest | Raw corpus batch ingested into wiki

Batch-ingested the broader `raw/` corpus into `wiki/sources/` with evidence-quality triage, added new methodology and history concept/entity pages, expanded synthesis, and regenerated `wiki/index.md`. Out-of-scope or low-signal notes were preserved but marked explicitly rather than forced into conclusions.

## [2026-05-04] create | Vault maintenance guide

Added a meta synthesis page describing how to maintain the vault, including ingest, query, lint, triage, and local script usage.
