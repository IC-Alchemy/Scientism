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

## [2026-05-04] ingest | Scobey polio article and AIDS congressional letter

Added attributed source pages for the Scobey poliomyelitis-poisoning article and the 1995 Gutknecht-to-Fauci AIDS letter, updated related polio/AIDS and inferential-leap pages, refreshed synthesis triage/overview, and regenerated `wiki/index.md`.

## [2026-05-04] query | Gutknecht letter questions 7-9

Added a narrow synthesis page answering questions 7-9 with primary and official sources only, linked it from the 1995 Gutknecht letter source page, and prepared the vault for regenerated indexing.

## [2026-05-04] query | Gutknecht letter questions 1-12

Added a consolidated synthesis page answering all 12 questions from the March 24, 1995 Gutknecht letter, keeping 1995 framing separate from stronger current evidence and marking the unresolved funding-total question explicitly.

## [2026-05-04] update | Tightened evidence standard against appeal to authority

Updated `CLAUDE.md` and `AGENTS.md` to require experiment-first support, explicitly reject authority summaries as scientific evidence, and downgrade the Gutknecht evidence-check page to unresolved pending direct study-level reconstruction.

## [2026-05-04] update | Removed authority-style evidence from Gutknecht notes

Reworked the Gutknecht synthesis pages so the consolidated page is now only a research worklist and the 7-9 detail page keeps only direct-study support where available.

## [2026-05-04] update | Vault-wide experiment-first evidence cleanup

Updated wiki templates, synthesis pages, concept/entity pages, and flagged source pages to enforce direct method, endpoint, result, and limitation requirements; added lint checks for authority-as-evidence phrasing and unsupported `claim_status: supported` pages.

## [2026-05-04] ingest | ViroLIEgy method page, Rosenau influenza page, and Leverson germ-theory critique

Added three Tier 3 source pages from `raw/`, updated germ-theory and scientism-related concept/entity/synthesis pages, kept all conclusions attribution-bound, and flagged the new material as dispute-mapping and follow-up research leads rather than closure.
