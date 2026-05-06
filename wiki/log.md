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

## [2026-05-05] query | Pediatric vaccine placebo-control trial audit

Used Lens scholarly search and PubMed abstracts to check the 18 trial records cited by the CHD pediatric vaccine placebo-control source. Added a trial-record audit page, linked it from the CHD source page, and updated placebo-control and endpoint concept pages to distinguish active comparators, placebo-labeled comparators, and unresolved placebo composition.

## [2026-05-05] query | Vaccinated children more healthy question

Added a direct synthesis answer clarifying that the currently audited vaccine trials do not establish that vaccinated children are more healthy than not vaccinated children, because the measured endpoints are mostly narrower disease, immunogenicity, or short-term safety outcomes rather than broader overall-health comparisons.

## [2026-05-05] query | Lens shortlist for vaccinated-versus-unvaccinated health outcomes

Ran tighter Lens searches for vaccinated-versus-unvaccinated child health outcomes, including all-cause mortality, hospitalization, chronic disease, neurodevelopment, asthma, allergy, and development endpoints. Added the strongest candidate studies and search strings to the vaccinated-children synthesis page.

## [2026-05-05] update | Added results to vaccinated-children shortlist

Added abstract-level reported results for each shortlisted study in the vaccinated-versus-unvaccinated health-outcomes synthesis page, keeping the result separate from each study's design limits.

## [2026-05-05] update | Added interpretation boundary to vaccinated-children synthesis

Clarified that the current shortlist does not establish a broad overall-health benefit claim for childhood vaccination, while also requiring vaccine-specific and endpoint-specific support before converting harm associations into universal causal conclusions.

## [2026-05-05] update | Added parental messaging endpoint boundary

Updated the vaccinated-children synthesis, disease-prevention comparison, inferential-leap concept, and research-program overview to state that parents may hear disease-specific vaccine evidence presented as proof of overall child-health benefit. Marked that as an inferential leap unless broad health outcomes are directly measured.

## [2026-05-05] ingest | Effectiveness and Cost-Benefit of Influenza Vaccination of Healthy Working Adults

Added a Tier 1 source page for the Bridges et al. randomized saline-placebo influenza vaccine trial in healthy working adults. Updated clinical endpoints, placebo controls, inferential leap, disease-prevention versus health-outcomes, source-corpus triage, and regenerated `wiki/index.md`.

## [2026-05-05] update | Corrected 1997-1998 influenza vaccine trial endpoint summary

Revised the Bridges et al. source summary and related endpoint/comparison pages to preserve the paper's unfavorable 1997-1998 clinical-utilization finding: vaccine recipients reported significantly more ILI-related sick days, lost workdays, and physician-visit work hours than placebo recipients.

## [2026-05-05] update | Added warning-gap framing for Bridges influenza vaccine trial

Updated the Bridges et al. source page, scientism concept page, inferential-leap page, and research-program overview to treat the unfavorable 1997-1998 randomized clinical-utilization findings as a central author-conclusion versus endpoint-result case for the vault.
