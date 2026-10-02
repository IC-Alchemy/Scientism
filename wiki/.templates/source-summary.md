---
title: "<Source Title>"
category: source
summary: <one-line summary>
tags: []
source_path: raw/<path-to-source>
source_date: <YYYY-MM>
authors: [<author1>, <author2>]
ingested: <YYYY-MM-DD>
updated: <YYYY-MM-DD>
claim_status: exploratory | disputed | supported | contradicted | unresolved
claim_type: historical | methodological | empirical | medical | rhetorical
source_tier: tier-1 | tier-2 | tier-3
evidence_role: <one-line role of this source in the vault>
pmid: <PMID when available>
pmcid: <PMCID when available>
doi: <DOI when available>
---

# <Source Title>

## Source type
- Role in this vault: <which rung or question this source serves, with [[synthesis/...]] link>
- Journal/year: <journal>, <year>
- Authors: <authors>
- Source basis in hand: <full text / PubMed abstract / bibliographic record only>

> [!warning] Warning
> This page is for research analysis only. It is not medical advice.

## Evidence fields
| Field | Extraction |
|---|---|
| Study type | |
| Subject / sample | |
| Intervention or exposure | |
| Comparator / control | |
| Endpoint | |
| Result | |
| Main limitation | |

If these fields cannot be filled from the source in hand, write "Not verifiable without the text" and mark the page a pointer page with `claim_status: unresolved`.

## What the experiment can answer
- The narrow claims the experiment or document directly supports.

For abstract-level records use "## What the abstract can answer"; for pointer pages use "## What the record can answer".

## What it cannot answer
- The claims the design cannot support.

For abstract-level records use "## What full text would still need to establish".

## Later inferential-leap risk
The specific broader conclusion this source's result is most at risk of being stretched toward.

## Vault conclusion
Only what the named evidence supports, at the rung it reaches. Otherwise state "We do not know" and keep `claim_status` unresolved or exploratory.

## Connections
- Fills <gap> in [[synthesis/xxx]]
- Companions: [[sources/aaa]], [[sources/bbb]]
