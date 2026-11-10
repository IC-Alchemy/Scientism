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
| 3 | GAP 1 sham-controlled human challenge | H1N1 pandemic-inoculum challenge (replicates Couch design) | done | Full text verified end to end for both halves of the design: [[sources/memoli-2015-h1n1pdm09-human-challenge-model-validation]] (dose-finding validation, no sham arm, 69% MMID at 10^7 TCID50) and [[sources/han-2021-cr6261-placebo-controlled-h1n1pdm09-challenge]] (randomized double-blind placebo-controlled trial; placebo arm 5% dextrose IV; 69% MMID, 88% confirmed infection, virus-only). |
| 4 | GAP 2 controlled natural-route transmission | Cowling et al. 2009, Ann Intern Med - household facemask/hand-hygiene RCT, lab-confirmed influenza endpoint | unverifiable | Publisher subscription-only (DOI 10.7326/0003-4819-151-7-200910060-00142 returns 403); not in PMC; no author copy found in HKU Scholars Hub search. |
| 5 | GAP 2 controlled natural-route transmission | Herlocher et al. 2004, J Infect Dis - ferret contact-transfer transmission | unverifiable | Subscription-only (DOI 10.1086/424572 returns 403; Europe PMC open access N, no PMCID). Note: the paper's title is about oseltamivir-resistant influenza transmission in ferrets. |
| 6 | GAP 3 prospective cohort, exposure + infection markers + timing | Fox et al., Seattle Virus Watch family studies | unverifiable | Best fit identified: Hall/Cooney/Fox, Seattle Virus Watch IV (AJE 1973;98:365-380, DOI 10.1093/oxfordjournals.aje.a112125) — closed everywhere reachable (OUP Cloudflare blocks curl, r.jina.ai, and the sandbox browser; Unpaywall/OpenAlex/S2: no OA copy; scholar.archive.org rate-limited all run; web.archive.org in an outage — only an abstract-page snapshot exists). Retry when IA recovers via old aje.oxfordjournals.org archive. |
| 7 | GAP 3 prospective cohort, exposure + infection markers + timing | Monto & Sullivan Tecumseh household cohort (influenza) | unverifiable | Best fit identified: Monto/Koopman/Longini, Tecumseh study of illness. XIII (AJE 1985;121:811-822, PMID 4014174, DOI 10.1093/oxfordjournals.aje.a114052) — closed (Unpaywall/OpenAlex/Semantic Scholar all report no OA copy; OUP Cloudflare 403; no repository or Wayback full text found; DDG/Bing/Yandex/Mojeek found no author copy). |
| 8 | GAP 4 intervention with disease endpoint | Cutland et al. 2005, Lancet - PCV9 Gambia trial (already filed as [[sources/cutts-2005-pcv9-gambia-rct]]; verify author name and reconcile) | done | Reconciled run 3: "Cutland" is a name error; the primary paper is Cutts FT et al., Lancet 2005;365(9465):1139-46 (PMID 15794968, DOI 10.1016/S0140-6736(05)71876-6). The filed page is full-text-grade (arms, named endpoints, per-protocol and ITT numbers), so no refiling. |
| 9 | GAP 4 intervention with disease endpoint | Vesikari et al. 2006 - rotavirus vaccine RCT, severe gastroenteritis endpoint | unverifiable | NEJM 2006;354(1):23-33 (PMID 16394299, DOI 10.1056/NEJMoa052664): nejm.org Cloudflare-403; not in PMC/Europe PMC; Unpaywall closed; ResearchGate author copy exists but hard-blocked (Cloudflare challenge in the real browser); Tampere Pure record carries no attached file. |
| 10 | GAP 4 intervention with disease endpoint | Garland et al. 2007 (FUTURE II) - HPV, CIN2+ endpoint | unverifiable | NEJM 2007 (PMID 17494925): not in PMC/Europe PMC; Unpaywall closed; nejm.org Cloudflare-403; no author/repository copy found in DDG/Deep Blue searches (only RG hits, also blocked). |
| 11 | GAP 5 isolation partials | Enders et al. 1954 - measles propagation (seek second-lab re-isolation) | unverifiable | Second-lab candidate identified: Ruckle & Rogers, Studies with measles virus II (J Immunol 1957;78:341-355, PMID 13449323, DOI 10.4049/jimmunol.78.5.341). Full text closed: J Immunol moved to OUP (journals.aai.org redirects; Cloudflare); Wayback-era reprint URL snapshot is a 6.5 KB interstitial, not the PDF. Highest-value retry when web.archive.org recovers: jimmunol.org/cgi/reprint/78/5/341. |

## Run log

- 2026-11-10 (run 3): Items 6-11 worked; no new sources pages. Every closed-access candidate hit the same wall: OUP, NEJM, AJPH, and ResearchGate are Cloudflare-hard for this sandbox (curl, r.jina.ai, and the real browser all blocked), and web.archive.org was in an outage for most of the run, killing the old HighWire full-text route; scholar.archive.org was rate-limited all run. Item 8 reconciled to `done` (Cutland = name error; primary is Cutts et al., Lancet 2005;365:1139-46; [[sources/cutts-2005-pcv9-gambia-rct]] already meets the standard). Items 6, 7, 9, 10, 11 marked `unverifiable` with per-item candidates and DOIs recorded above. GAP 3 remains empty; GAP 4 now has one verified paper (Cutts 2005). No existing conclusion changed.

- 2026-11-10 (run 2): Item 3 done with two papers, both fetched as full-text PMC HTML (Europe PMC fullTextXML 500s again; OUP robot-blocked). No existing conclusion changed.
  - [[sources/memoli-2015-h1n1pdm09-human-challenge-model-validation]] — Memoli et al. 2015, Clin Infect Dis 60(5):693 ff. (PMC4342672). Dose-escalation human challenge, 46 adults, GMP wild-type A/California/04/2009(H1N1), MMID endpoint (shedding + >=1 symptom): 69% at 10^7 TCID50, 0% shedding at 10^3-10^4. No sham arm — recorded explicitly; the sham-controlled element is supplied by the second paper.
  - [[sources/han-2021-cr6261-placebo-controlled-h1n1pdm09-challenge]] — Han et al. 2021, Clin Infect Dis 73(11):e4260-e4268 (PMC8664469). Randomized double-blind placebo-controlled CR6261 trial in the validated model; 91 challenged (49/42); placebo arm (5% dextrose IV): MMID 69%, confirmed influenza 88%, symptoms 93%, shedding 74%. CR6261: no significant effect on the primary endpoint (viral RNA AUC, P=.315); baseline anti-NA titer was the only disease predictor.
  - Influenza ladder gained a rung-7 row; cross-cutting ladder gained an influenza note. GAP 1 is now covered for influenza; item 2 (RSV challenge) remains the other half of GAP 1. GAP 2 (natural-route transmission) untouched by this run.
- 2026-11-10 (run 1): Queue file created from the shortlist. Items 1, 2, 4, 5 attempted; none reachable as full text, so all four marked `unverifiable`. No sources pages written.
  - Item 1 (Couch 1966 JAMA): not indexed in Crossref or Europe PMC by author/year. Found the related Couch et al. 1966 Bacteriological Reviews paper (PMC378233, route of inoculation in volunteers), but PMC and Europe PMC full text were blocked (reCAPTCHA / HTTP 500). Lead for a later run; not a queue substitute.
  - Item 2 (Cody/Wright RSV challenge): primary paper not located. Related Hall et al. 1981 RSV route study is already filed as [[sources/hall-1981-infectivity-rsv-various-routes-inoculation]] (abstract lists dose groups only; no placebo arm stated in the abstract).
  - Item 3 (H1N1 pandemic challenge): not attempted this run.
  - Item 8 note: the paper filed as [[sources/cutts-2005-pcv9-gambia-rct]] is by Cutts et al.; the shortlist's "Cutland" appears to be a name error. Reconcile before a second filing.
- Next run: first probe web.archive.org (IA outage blocked this run). If up: retry item 11 (jimmunol.org/cgi/reprint/78/5/341), item 6 (aje.oxfordjournals.org archive snapshots), then item 7. Items 9/10 likely need scholar.archive.org (rate-limited all run) or a human-access copy. Remaining untouched: none — all 11 items now have a status.

## Related

- [[synthesis/viral-disease-causation-evidence-ladder]]
- [[synthesis/virus-disease-attribution-audit-worklist]]
- [[synthesis/virus-causation-inferential-leaps]]
- [[concepts/placebo-controls]]
- [[concepts/surrogate-endpoints]]
