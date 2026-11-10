---
title: Source Verification Queue
category: synthesis
summary: Work queue for moving the virology corpus toward the vault's evidence standard by fetching and verifying candidate papers end to end.
tags:
  - evidence-standards
  - evidence-synthesis
  - source-corpus-inventory
  - vault-governance
  - inferential-discipline
sources: 0
updated: 2026-11-10
---

# Source Verification Queue

> [!note] Note
> Status values: empty = todo; `in-progress` (with claim date); `done` (sources page written); `unverifiable` (full text unreachable, one-line reason); `failed-standard` (full text read, does not meet the evidence standard, one-line reason).
> Rule: a sources page is written only from the paper's own methods and results. Abstracts alone do not count.

| # | Gap | Candidate | Status | Note |
|---|-----|-----------|--------|------|
| 1 | GAP 1 sham-controlled human challenge | Couch et al. 1966, JAMA - experimental influenza, egg-grown inoculum vs placebo | unverifiable | Journal article not indexed in Crossref or Europe PMC by author/year and not returned by web search; no full text reachable. |
| 2 | GAP 1 sham-controlled human challenge | Cody/Wright adult RSV human challenge (placebo-controlled), primary paper | unverifiable | Primary paper not identified (no Crossref, Europe PMC, or web hit for Cody/Wright adult RSV challenge); citation itself unconfirmed. |
| 3 | GAP 1 sham-controlled human challenge | H1N1 pandemic-inoculum challenge (replicates Couch design) | | |
| 4 | GAP 2 controlled natural-route transmission | Cowling et al. 2009, Ann Intern Med - household facemask/hand-hygiene RCT, lab-confirmed influenza endpoint | unverifiable | Publisher subscription-only (DOI 10.7326/0003-4819-151-7-200910060-00142 returns 403); not in PMC; no author copy found in HKU Scholars Hub search. |
| 5 | GAP 2 controlled natural-route transmission | Herlocher et al. 2004, J Infect Dis - ferret contact-transfer transmission | unverifiable | Subscription-only (DOI 10.1086/424572 returns 403; Europe PMC open access N, no PMCID). Note: the paper's title is about oseltamivir-resistant influenza transmission in ferrets. |
| 6 | GAP 3 prospective cohort, exposure + infection markers + timing | Fox et al., Seattle Virus Watch family studies | | |
| 7 | GAP 3 prospective cohort, exposure + infection markers + timing | Monto & Sullivan Tecumseh household cohort (influenza) | | |
| 8 | GAP 4 intervention with disease endpoint | Cutland et al. 2005, Lancet - PCV9 Gambia trial (already filed as [[sources/cutts-2005-pcv9-gambia-rct]]; verify author name and reconcile) | | |
| 9 | GAP 4 intervention with disease endpoint | Vesikari et al. 2006 - rotavirus vaccine RCT, severe gastroenteritis endpoint | | |
| 10 | GAP 4 intervention with disease endpoint | Garland et al. 2007 (FUTURE II) - HPV, CIN2+ endpoint | | |
| 11 | GAP 5 isolation partials | Enders et al. 1954 - measles propagation (seek second-lab re-isolation) | | |

## Run log

- 2026-11-10 (run 1): Queue file created from the shortlist. Items 1, 2, 4, 5 attempted; none reachable as full text, so all four marked `unverifiable`. No sources pages written.
  - Item 1 (Couch 1966 JAMA): not indexed in Crossref or Europe PMC by author/year. Found the related Couch et al. 1966 Bacteriological Reviews paper (PMC378233, route of inoculation in volunteers), but PMC and Europe PMC full text were blocked (reCAPTCHA / HTTP 500). Lead for a later run; not a queue substitute.
  - Item 2 (Cody/Wright RSV challenge): primary paper not located. Related Hall et al. 1981 RSV route study is already filed as [[sources/hall-1981-infectivity-rsv-various-routes-inoculation]] (abstract lists dose groups only; no placebo arm stated in the abstract).
  - Item 3 (H1N1 pandemic challenge): not attempted this run.
  - Item 8 note: the paper filed as [[sources/cutts-2005-pcv9-gambia-rct]] is by Cutts et al.; the shortlist's "Cutland" appears to be a name error. Reconcile before a second filing.
- Next run: start at item 3, then 6, 7, 9, 10, 11. Items 6 and 7 (Seattle, Tecumseh) and 11 (Enders 1954) need a search for open-access full text first.

## Related

- [[synthesis/viral-disease-causation-evidence-ladder]]
- [[synthesis/virus-disease-attribution-audit-worklist]]
- [[synthesis/virus-causation-inferential-leaps]]
- [[concepts/placebo-controls]]
- [[concepts/surrogate-endpoints]]
