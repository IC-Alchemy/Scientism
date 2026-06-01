---
title: Vault Maintenance Guide
category: synthesis
summary: >-
  Operating guide for maintaining this Obsidian research vault without blurring
  source quality, experimental scope, or wiki conclusions.
tags:
  - document-analysis
  - knowledge-management
  - maintenance
  - meta
  - obsidian
  - obsidian-vault
  - out-of-scope
  - source-triage
  - wiki-maintenance
  - workflow
sources: 3
updated: 2026-05-04T00:00:00.000Z
claim_status: supported
claim_type: methodological
---

# Vault Maintenance Guide

## Purpose
This page explains how to maintain the Scientism vault as a research wiki rather than a dumping ground for claims. The core rule is simple: read from `raw/`, write to `wiki/`, and keep source claims, experimental scope, and current wiki conclusions visibly separate.

## Operating model
- `raw/` is immutable source storage. Do not edit, normalize, or rewrite files there.
- `wiki/` is the maintained knowledge layer. All summaries, concept pages, comparisons, entities, synthesis pages, and maintenance notes belong here.
- `CLAUDE.md` and `AGENTS.md` are the local schema and workflow rules. They outrank generic wiki habits.

## Page standards
- Every wiki page needs frontmatter with `title`, `category`, `summary`, `tags`, and `updated`.
- Use `claim_status`, `claim_type`, and `source_tier` when a page is controversial, preliminary, medical, historical, or unresolved.
- Every material claim should point to a source page under `wiki/sources/`.
- On disputed topics, keep attribution explicit. Write `Source X argues...` instead of flattening the claim into wiki voice.

## Source triage rules
- `Tier 1`: primary papers, historical documents, systematic reviews.
- `Tier 2`: serious secondary scholarship.
- `Tier 3`: transcripts, essays, clips, AI summaries, advocacy material, rough notes.

The maintenance rule is not to discard weak sources, but to file them honestly. Tier 3 material can open questions, map disputes, and suggest follow-up ingestion. It cannot settle high-stakes conclusions on its own.

## Ingest workflow
1. Read the source in `raw/` directly.
2. Decide whether it is evidence, commentary, or only a research lead.
3. Create or update a `wiki/sources/` page first.
4. Separate three things inside that page:
   - what the source claims
   - what question the experiment or document is actually capable of answering
   - what this wiki currently concludes
5. Update the affected concept, entity, comparison, and synthesis pages.
6. Regenerate `wiki/index.md` with `python scripts/update_index.py --write --date YYYY-MM-DD`.
7. Append a log entry to `wiki/log.md`.

## Query workflow
- Read `wiki/index.md` first.
- Then read the most relevant concept, source, and synthesis pages in full.
- In answers, distinguish clearly between source argument, evidence level, and unresolved questions.
- If a useful answer adds durable value, file it back into `wiki/` as an updated page rather than leaving it only in chat.

## Lint workflow
Run:

```powershell
python scripts/lint_wiki.py
```

Current checks:
- missing frontmatter
- broken wikilinks
- orphan pages

Before considering the vault healthy, also scan for:
- controversial claims stated without attribution
- medical or historical claims backed only by Tier 3 material
- endpoint discussions that do not name the endpoint
- inferential-leap discussions that do not describe the underlying experiment

## Local scripts
- `python scripts/update_index.py --write --date YYYY-MM-DD` regenerates `wiki/index.md` from page frontmatter.
- `python scripts/lint_wiki.py` reports missing frontmatter, broken links, and orphans.

## What good maintenance looks like here
- The wiki stays neutral even when the raw source is polemical.
- Thin notes are labeled as thin notes.
- Out-of-scope material is preserved for traceability but marked as out of scope.
- Stronger primary sources are preferred when advancing a conclusion.
- Medical and historical disputes remain explicitly unresolved until better sourcing exists.

## Current maintenance priorities
- Replace pointer notes with direct ingestion of the underlying papers or historical texts.
- Strengthen replication-crisis coverage with direct primary or review material.
- Add paired supporting and critical sources on disputed germ-theory and virology topics.
- Keep methodology pages precise about controls, endpoints, and what an experiment can actually show.

## Related
- [[synthesis/scientism-research-program-overview]]
- [[synthesis/source-corpus-triage]]
- [[concepts/inferential-leap]]
- [[concepts/empirical-evidence]]
