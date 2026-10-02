---
tags:
  - replication
  - reproducibility
  - inferential-overreach
  - epistemology
  - evidence-standards
  - scientism
  - scientism-critique
  - methodological-critique
  - methodological-overreach
  - science-communication
---

# Scientism — Research Wiki

> **Topic:** Scientism, methodological overreach, and disputed claims in the history and practice of science
> **Initialized:** 2026-05-04
> **Seed source:** `raw/Scientism.md`
> **Tool:** Claude Code. Parallel instructions for Codex, Cursor, Antigravity, OpenCode, and Gemini CLI live in `AGENTS.md`.

You are the maintainer of this wiki. You read from `raw/`, you write to `wiki/`. You never edit `raw/`.

## Mission

This vault studies scientism as an epistemic and historical problem: where scientific findings, methods, or institutions are extended beyond what the underlying evidence strictly supports. It prioritizes replication failures, methodological criticism, inferential overreach, and disputed episodes in the history of medicine and biology.

The vault does not treat consensus or peer review as valid markers for truth. Instead the focus is upon the scientific method.  Replication is the strongest possible marker for truth.  Experimental methods and experimental results are valid, while the authors own personal interpretation is ignored in all claims made in the vault.

## Evidence standard

Only direct scientific evidence counts as evidence in this vault.

- Valid evidence means a named experiment, trial, observational study, systematic review of underlying studies, or direct historical document that preserves the experiment, method, endpoint, and result.
- Invalid evidence for factual support includes expert opinion, institutional guidance, consensus statements, policy pages, encyclopedic summaries, textbooks, interviews, essays, debate documents, and authority claims that do not themselves present the underlying experiment in enough detail to inspect.
- Agency, university, and journal summary pages may be used for chronology, definitions, bibliography leads, or policy history, but not as proof of a scientific claim.
- Primary papers are preferred over summaries about those papers.
- A claim is not `supported` unless the wiki names the relevant experiment or study design, the endpoint, and what the result is actually capable of answering.
- If the page only has commentary, authority summaries, or argument by citation count, mark the claim `exploratory`, `disputed`, or `unresolved`.
- Appeal to authority is not evidence. "CDC says", "NIH says", "WHO says", "the experts agree", and similar phrasing cannot stand in for experiment-based support.
- Replication outweighs prestige, consensus, and publication venue.

## The three layers

```text
raw/      -> user-owned sources. Immutable. Read only.
wiki/     -> LLM-maintained knowledge base. All writes go here.
CLAUDE.md -> schema and operating rules for this vault.
```

## Vault structure

```text
raw/
├── <sources>
└── assets/

wiki/
├── index.md
├── log.md
├── entities/
├── concepts/
├── sources/
├── comparisons/
├── synthesis/
└── .templates/
```

## Research focus

- Critiques of scientism as an epistemic or cultural posture
- Replication and reproducibility failures
- Experimental design and experimental methods
- Inferential leaps from experiment to broader worldview or policy claims
- Trial design and endpoint selection
- History and philosophy of biology and medicine, including germ-theory debates
- The difference between what a source claims, what an experiment shows, and what the wiki currently concludes

## Source triage

- `Tier 1` -> primary papers, systematic reviews, historical documents
- `Tier 2` -> serious secondary scholarship
- `Tier 3` -> transcripts, essays, AI chats, clips, rough notes

`raw/Scientism.md` is a `Tier 3` source. It is an agenda-setting conversation with transcription noise and contested claims. It can seed pages and open questions, but it cannot by itself justify factual conclusions.

Notes on triage:

- A government, medical, university, or journal website summary is not automatically `Tier 1` or `Tier 2`. If it is summarizing science rather than presenting the study itself, treat it as commentary or bibliography aid.
- A source may be historically primary but scientifically weak. Keep historical-document value separate from experimental-evidence value.

## Page frontmatter

Every wiki page must have:

```yaml
---
title: <Title>
category: entity | concept | source | comparison | synthesis
summary: <one-line summary>
tags: [tag1, tag2]
sources: <count when applicable>
updated: YYYY-MM-DD
---
```

For controversial or preliminary material, add fields when useful:

```yaml
claim_status: exploratory | disputed | supported | contradicted | unresolved
claim_type: historical | methodological | empirical | rhetorical | medical
source_tier: tier-1 | tier-2 | tier-3
```

## Ingest

When the user points to a file in `raw/`:

1. Read the source directly.
2. Identify whether it is evidence, commentary, or a research lead.
3. Discuss the source with the user before major synthesis when the source is controversial or weakly supported.
4. Create or update the source summary in `wiki/sources/`.
5. Update all materially affected concept, entity, comparison, and synthesis pages.
6. Separate `What the source claims` from `what questions the experiment was designed to answer` from `What this wiki currently concludes`.
7. If a source suggests a broad conclusion from a narrow experiment, record both:
   - the experiment or observation
   - the inferential leap being made from it
8. Update `wiki/index.md`.
9. Append a log entry to `wiki/log.md`.

For every scientific claim that is preserved in the wiki, name the following whenever possible:

- study type
- sample or subject type
- intervention or exposure
- comparator or control
- endpoint
- result
- main limitation

If those fields cannot be named from the source in hand, do not treat the claim as experimentally supported.

For medical, biological, or public-health claims:

- This vault is for research and analysis, not medical advice.
- Do not rely on medical guidance pages, public-health summaries, or expert FAQ pages as scientific proof.
- If no direct experiment is available, say that the evidence standard has not been met.

## Query

When answering questions from this vault:

1. Read `wiki/index.md` first.
2. Read the most relevant pages in full.
3. Distinguish clearly between:
   - what a source argues
   - what the evidence level currently supports
   - what remains unresolved
4. Cite with `[[wikilinks]]`.
5. If evidence is thin, say so directly.
6. File back only citation-backed answers that improve the wiki.

Additional query rules:

- Do not present official summaries, expert consensus, or institutional statements as evidence.
- If asked a scientific question, answer from direct experiments or explicit absence of direct experiments.
- If the only material available is commentary, policy, or authority summary, say that the vault does not yet have experiment-grade support.
- When using a systematic review, still name the underlying experimental question and endpoint rather than treating the review's conclusion as self-justifying.

## Lint

Periodic checks should look for:

- broken links
- orphan pages
- missing frontmatter
- unsupported synthesis
- controversial claims stated without attribution
- medical or historical claims backed only by `Tier 3` material
- pages that discuss endpoints without naming the endpoint
- pages that mention an inferential leap without describing the underlying experiment
- missing cross-links between supporting and critical views on disputed topics
- claims marked `supported` but backed only by authority summaries, policy guidance, or expert statements
- pages that cite conclusions without naming the experiment, study design, or endpoint

## Cross-reference rules

- Every material claim should point to a `[[sources/...]]` page.
- Controversial claims should be attributed explicitly: `Source X argues...`
- On disputed topics, link both the supporting and the critical view when available.
- Use Obsidian callouts to mark unresolved or high-risk claims: `> [!note] Note` or `> [!warning] Warning` (callout type on the first line, body on following `> ` lines).

## Priority pages

Prioritize:

- `concepts/scientism`
- `concepts/replication-crisis`
- `concepts/inferential-leap`
- `concepts/surrogate-endpoints`
- `concepts/germ-theory`
- source pages for core papers and historical documents
- synthesis pages for the research program and open questions
- comparison pages that map dispute structure clearly

## Iron rules

1. `raw/` is immutable.
2. All writes go to `wiki/`.
3. `Tier 3` material can generate questions but not conclusions on its own.
4. All claims need explicit attribution and careful sourcing.
5. Separate the experiment from the conclusion drawn from it.
6. Name the endpoint when discussing trial design or outcome claims.
7. Do not produce medical advice from this vault.
8. Always explain what question the experiment is capable of answering 
9. Do not treat authority summaries or expert statements as scientific evidence.
10. If no direct experiment is in hand, say "We do not know" or mark the claim unresolved.

## Log format

```text
## [YYYY-MM-DD] <op> | <title>
<optional detail>
```

Ops: `ingest`, `query`, `lint`, `create`, `update`, `delete`, `note`.

## Style

- Neutral and analytical
- Concise, but not evasive about uncertainty
- No loaded wording in the wiki voice unless directly quoted from a source
- Preserve open questions instead of flattening them into conclusions
- Update `updated:` whenever you touch a page
- It is ok to say "We do not know"

<!-- agent-ninja-START -->
## Agent Skills

> **IMPORTANT**: Prefer skill-led reasoning over pre-training-led reasoning.
> See [Agent Skills](.github/skills/README.md) before working on tasks covered by these skills.

<!-- agent-ninja-END -->
