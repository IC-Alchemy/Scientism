---
title: Validation of the Wild-type Influenza A Human Challenge Model H1N1pdMIST
category: source
summary: 2015 Clinical Infectious Diseases dose-finding human challenge paper showing intranasal GMP A(H1N1)pdm09 produced mild-to-moderate influenza disease (shedding plus symptoms) in 69% of low-antibody adults at 10^7 TCID50.
tags:
  - human-challenge
  - influenza
  - influenza-virus
  - h1n1pdm09
  - dose-response
  - viral-shedding
sources: 1
updated: 2026-11-10
claim_status: supported
claim_type: empirical
source_tier: tier-1
evidence_role: primary influenza human challenge model validation; GAP 1 dose-finding rung (no sham arm)
pmid: 25416753
pmcid: PMC4342672
doi: 10.1093/cid/ciu924
---

# Validation of the Wild-type Influenza A Human Challenge Model H1N1pdMIST

## Source type
- Role in this vault: primary controlled human challenge paper for influenza A(H1N1)pdm09; fills GAP 1 in [[synthesis/source-verification-queue]] and rung 7 (controlled human challenge) of [[synthesis/viral-disease-causation-evidence-ladder]]
- Journal/year: *Clinical Infectious Diseases*, 2015;60(5):693 ff.
- Authors: Matthew J. Memoli, Lindsay Czajkowski, Susan Reed, Rani Athota, Tyler Bristol, Kathleen Proudfoot, Sarah Fargis, Matthew Stein, Rebecca L. Dunfee, Pamela A. Shaw, Richard T. Davey, Jeffery K. Taubenberger
- Source basis in hand: full-text PMC article (PMC4342672)

> [!warning] Warning
> This page is for research analysis only. It is not medical advice.

## Evidence fields
| Field | Extraction |
|---|---|
| Study type | Prospective dose-escalation human challenge (FDA IND BB-IND 14969, phase 1; ClinicalTrials.gov NCT01646138) in an isolation unit at the NIH Clinical Center |
| Subject / sample | 46 challenged healthy nonsmoking adults aged 18-50 (49 enrolled; 6 disqualified on pre-challenge respiratory panel, 3 re-enrolled later), mean age 29.2, pre-challenge HAI titer <=1:40, enrolled April 2012 - June 2013 |
| Intervention or exposure | Intranasal GMP-manufactured wild-type A(H1N1)pdm09 (all 8 gene segments of A/California/04/2009 reverse-genetics rescued in Vero cells; 3 amino-acid changes from the isolate: PA:G58S, HA:A388V, NA:E119K; ferret/mouse tests showed no infectivity, pathology, or fitness difference from the isolate). Quote: "Five hundred microliters of virus diluted in sterile saline was delivered in each nostril of a recumbent participant." Doses: 10^3, 10^4, 10^5, 10^6, 10^7 TCID50 (n=5, 4, 5, 19, 13) |
| Comparator / control | Sham arm: **no**. All participants received live virus; the design names only dose groups (statistical comparison was "the prevalence of MMID (Table 1) in the different dose groups"). Between-dose contrast replaces a placebo group: at 10^3-10^4 TCID50 no participant shed virus (0/9), against 77% shedding at 10^7. |
| Endpoint | Named exactly: "The primary objective was to determine the infectious dose of influenza A(H1N1)pdm09 that induced uncomplicated MMID [mild to moderate influenza disease] in at least 60% of healthy volunteers with hemagglutination inhibition (HAI) titers of <=1:40. MMID was defined as viral shedding detected by clinical molecular testing, plus the onset of at least 1 acute influenza-like illness symptom after intranasal challenge." Secondary: symptom counts/duration, daily nasal-wash qRT-PCR shedding, HAI and NAI serology, serum cytokines |
| Result | Primary objective met at 10^7 TCID50: MMID in 69% (9/13) vs 47% (9/19) at 10^6, 20% (1/5) at 10^5, 0% at 10^3 and 10^4 (P=.029 vs the two lowest doses). At 10^7: symptoms 85%, shedding 77%, >=4-fold HAI rise by week 8 85%. Overall 46 challenged: MMID 41%, symptoms 78%, shedding 43%. Symptoms began 24-72 h post-challenge and lasted about 8 days at 10^7; fever in only 10% of participants; no severe complications. In the text: shedding "preceded symptoms by 12-24 hours and terminated 2-3 days prior to symptom resolution" |
| Main limitation | No sham/placebo arm, so symptom rates in inoculated non-shedders (>30% at some doses) cannot be contrasted with a truly non-inoculated group; healthy selected adults with low baseline antibody; defined high-dose intranasal inoculation is not a natural-route exposure; upper-respiratory-predominant disease was a design goal |

## Which gap and ladder rung this fills
- Queue GAP 1 (sham-controlled human challenge with purified inoculum), partially: purified GMP wild-type inoculum and a defined clinical+virological endpoint are in hand; the sham-controlled element comes from the companion trial [[sources/han-2021-cr6261-placebo-controlled-h1n1pdm09-challenge]].
- Ladder rung 7 (controlled human challenge) of [[synthesis/viral-disease-causation-evidence-ladder]]; new row in [[synthesis/influenza-influenza-virus-evidence-ladder]].

## What the experiment can answer
- That a defined intranasal dose of GMP wild-type A(H1N1)pdm09 can produce viral shedding plus acute influenza-like symptoms (MMID) in a dose-dependent way in seronegative adults, with a reproducible 69% attack rate at 10^7 TCID50.
- That shedding detectable by qRT-PCR begins before symptom onset and ends before symptom resolution in this model.
- That pre-challenge HAI/NAI titer inversely correlates with clinical score in the inoculated population.

## What it cannot answer
- Whether natural-route (contact, aerosol, fomite) exposure produces the same disease or attack rates; no transmission was tested.
- Whether PCR-detected shedding equals infectiousness; infectious virus was not quantified from these specimens in this paper.
- Whether fever frequency in medically attended natural cases (~80% per studies the authors cite) applies to the general infected population; the 10% fever figure is a challenge-model observation.

## Later inferential-leap risk
- The authors move from shedding kinetics to infectiousness: "indicating that individuals may be infectious before symptom development." Shedding of RNA-detected virus is an exposure marker, not a demonstrated transmission event; the experiment contained no recipient subjects.
- "The model correlates well with natural infection" is an assertion from outcome similarity; the experiment demonstrates dose-dependent infectability under inoculation, not equivalence to community acquisition.

## Vault conclusion
Supported at the controlled-human-challenge rung: wild-type A(H1N1)pdm09 delivered as a purified GMP intranasal inoculum produced dose-dependent shedding plus clinical influenza-like disease in previously low-antibody adults. It does not by itself establish natural-route transmission or population-level causation; those remain separate rungs ([[synthesis/influenza-influenza-virus-evidence-ladder]]).

## Connections
- Fills queue item 3 in [[synthesis/source-verification-queue]] (GAP 1)
- Companion sham-controlled trial on the same model: [[sources/han-2021-cr6261-placebo-controlled-h1n1pdm09-challenge]]
- Earlier influenza ladder rows: [[sources/rosenau-1919-experiments-to-determine-mode-of-spread-of-influenza]], [[sources/smith-andrewes-laidlaw-1933-virus-obtained-from-influenza-patients]]
