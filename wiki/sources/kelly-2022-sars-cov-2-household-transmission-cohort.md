---
title: Magnitude and Determinants of SARS-CoV-2 Household Transmission - A Longitudinal Cohort Study
category: source
summary: 2022 Clin Infect Dis prospective longitudinal household cohort (San Francisco Bay Area, Sept 2020-Jan 2022) - 42 symptomatic primary cases and 74 household contacts with near-daily self-collected nasal swabs regardless of symptoms; 32/74 (43%) contacts infected by serial RT-PCR, 81% of transmissions within 5 days of case onset, no cumulative-incidence difference by primary-case vaccination status (41% vs 45%, p=0.60), and the all-infections-are-primary-case-transmissions assumption quoted on the page.
tags:
  - sars-cov-2
  - covid
  - household-transmission
  - prospective-cohort
  - natural-route-transmission
  - pcr-endpoint
  - infectious-virus-assay
  - vaccination-transmission
  - evidence-synthesis
sources: 1
updated: 2026-11-10
claim_status: supported
claim_type: empirical
source_tier: tier-1
evidence_role: prospective household cohort with exposure, infection markers, and infection timing in the same people; GAP 3 anchor row for SARS-CoV-2
pmid: 35788827
pmcid: PMC9278251
doi: 10.1093/cid/ciac545
---

# Magnitude and Determinants of SARS-CoV-2 Household Transmission - A Longitudinal Cohort Study

## Source type
- Role in this vault: the vault's first full-text GAP 3 row for SARS-CoV-2 (queue item 20) - a natural-route household transmission cohort with near-daily infection-marker observation of contacts regardless of symptoms, plus infectious-virus (plaque/CPE) measurement on the primary cases.
- Journal/year: *Clinical Infectious Diseases*, 2022;75(Suppl 2):S193-S204 (published 2022-07-05; part of the CID supplement "Vaccines, Variants, and Vigilance", supported by an IDSA-CDC cooperative agreement)
- Authors: J. Daniel Kelly, Scott Lu, Khamal Anglin, Miguel Garcia-Knight, Jesus Pineda-Ramirez, Sarah A. Goldberg, Michel Tassetto, Amethyst Zhang, ... Raul Andino, Jeffrey N. Martin - UCSF, San Francisco VA Medical Center, Drexel, and US CDC Respiratory Viruses Branch
- Source basis in hand: complete 31-page accepted-manuscript PDF (1.0 MB) retrieved from the PMC OA package (PMC9278251) after solving the PMC proof-of-work download challenge - Methods (design, participants, measurements, RT-PCR, sequencing, CPE and plaque assays, analytical definitions, statistics), Results, Discussion, and stated limitations read end to end. Europe PMC fullTextXML returned HTTP 500 this run.

> [!warning] Warning
> This page is for research analysis only. It is not medical advice.

## Evidence fields
| Field | Extraction |
|---|---|
| Study type | "This was a longitudinal cohort study enrolling vaccinated and unvaccinated individuals (index cases) at the time of SARS-CoV-2 infection and their household contacts." Index-case-ascertained household cohort, San Francisco Bay Area, September 2020 - January 2022 (ancestral through Delta and early Omicron). No randomization, no intervention |
| Subjects | Enrolled 65 index cases + 115 household contacts (180 total). Analysis cohort after excluding asymptomatic primary cases and co-primary households: **42 symptomatic primary cases and their 74 household contacts (116 participants)**; median household size 3 (IQR 2-4); contacts 40 (54%) unvaccinated, 4 (5%) partially, 30 (41%) vaccinated. Primary cases enrolled median 4 days (1-5) after symptom onset; half (21) vaccinated (95% mRNA) |
| Exposure / surveillance | Natural household exposure to a symptomatic primary case. "Anterior nasal specimens were self-collected daily from dE through d14 and then on d17, d19, d21, and d28" relative to case symptom onset - median 14 specimens per case (552 total) and per contact (924 total); telephone questionnaires on days E, 9, 14, 21, 28. Laboratory: RT-qPCR (N + E genes, Biorad CFX); whole-genome sequencing (ARTIC primers v3/4.1, MinION, Pangolin 3.0.2); infectious virus by cytopathic effect on Vero-hACE2-TMPRSS2 cells (days 0-14) and conventional plaque assay on peak specimens |
| Comparator / control | Sham arm: **no** - an observational cohort cannot have sham infection. Internal contrasts: household contacts of 21 vaccinated vs 21 unvaccinated primary cases; contacts by own vaccination status; primary-case variant strata (Delta 18, non-VOI/VOC 12, Omicron 3, Epsilon 3, Alpha 1, unclassified 5) |
| Endpoint (named exactly) | "The primary outcome was SARS-CoV-2 infection among contacts" - defined as "the identification of SARS-CoV-2 RNA in any nasal or oropharyngeal specimen longitudinally obtained over the infectious period." Secondary: 14-day cumulative incidence, serial interval, and host/viral determinants (comorbidity, sex, RNA-load peak, RNA-shedding duration, infectious-viral-load peak and duration) by GEE modified-Poisson clustering on household |
| Result | **32/74 (43%) household contacts infected**; 5/32 (16%) asymptomatic; none hospitalized. "Almost all (26/32, 81%) transmission events occurred within 5 days since day of symptom onset of the primary case, with a median serial interval of 3 days (IQR: 2, 4; range: 0, 12)." Cumulative incidence: contacts of vaccinated cases 14/34 (41%; 95% CI 25-59) vs unvaccinated cases 18/40 (45%; 95% CI 29-62; p=0.60); vaccinated-to-vaccinated 12/29 (41%; 24-61); unvaccinated-to-unvaccinated 16/34 (47%; 30-65). By case variant: Delta 12/29 (41%), Omicron 2/5 (40%), Epsilon 1/8 (13%), non-VOI/VOC 12/22 (55%). Adjusted determinants: primary-case comorbidity aRR 2.1 (1.2-3.8) and RNA shedding >=10 days associated with contact infection; infectious-viral-shedding duration aRR 1.05 per day (0.96-1.2, n.s.); maximum RNA load and maximum infectious titer not significantly associated; no contact-level factor (age, sex, BMI, vaccination, comorbidity) significant |
| Main limitation | Authors' own list: some cases already RNA-negative for infectious virus at enrollment (possible left-censoring); maximum measured load may not be the true peak; sequencing success differed by vaccination status, so "we had a different distribution of variants among the vaccinated versus unvaccinated primary cases, potentially biasing the difference in cumulative incidence among these groups to the null"; phylogeny "unable to decipher the transmission chain with individual-level resolution"; exposure magnitude and mitigation behaviors not measured; sparse symptom characterization of contacts; recruitment skewed to health-system-connected symptomatic cases; small sample, underpowered for several associations incl. variant differences and shedding duration; time since vaccination/boosters not assessable |

## What the experiment can answer
- That in Bay Area households with a symptomatic index case under near-daily nasal swabbing regardless of symptoms, 43% of contacts acquired PCR-defined SARS-CoV-2 infection within the observation window, with 81% of transmissions within 5 days of case onset and a median serial interval of 3 days - infection-marker-plus-timing measurement in the same people, independent of symptom reporting (5/32 secondary infections asymptomatic).
- That measured household exposure-response markers behave differently than shedding-magnitude intuition: adjusted risk tracked duration of RNA shedding (>=10 days) and case comorbidity, not peak RNA load or peak infectious titer (the authors concede possible underpowering).
- That transmission was common from both vaccinated and unvaccinated primary cases, with no significant cumulative-incidence difference as measured (41% vs 45%, p=0.60).

## What it cannot answer
- Whether each contact infection came from the index case: the paper's own words - "we assumed that all infections identified in these households represented transmission from the primary case" - with phylogeny confirming clade-similarity only, not individual chains, and shared exposures possible.
- Whether vaccination reduces transmission: the vaccinated/unvaccinated primary-case contrast is observational (21 vs 21), confounded by calendar time (all vaccinated cases enrolled June 2021+ in the Delta/Omicron eras) and by the variant-distribution imbalance the authors themselves flag as biasing toward the null; a null difference with overlapping CIs is not evidence of no effect.
- Any disease endpoint: contact infection is RNA detection; severity outcomes are limited to "none were hospitalized" among household cases.
- Route of transmission (co-residence bundles droplet/fomite/aerosol contact) and generalization beyond health-system-connected, non-hospitalized, symptomatic index cases.

## Inferential leaps to watch
- The all-transmissions-from-the-primary-case assumption is stated as an assumption ("we assumed...") yet the results tables (43% cumulative incidence, serial intervals) are presented as primary-case transmission magnitudes; shared-exposure and co-primary pathways are handled by a decision algorithm plus one phylogenetic reclassification, not by chain resolution.
- Discussion headline "Although vaccination may reduce severity, it did not significantly reduce transmission" converts a non-randomized, era-confounded null (p=0.60, wide CIs) into a transmission-effect claim - an equivalence leap the paper's own limitation list partially retracts ("may have been underpowered").
- Abstract-level policy recommendation ("household contacts will need to employ additional interventions") goes beyond the design: no intervention was tested or randomized.
- "Vaccination prevents severe illness[16]" enters the Discussion by citation, not from this cohort's data.

## Which gap and ladder rung this fills
- Queue GAP 3 (prospective cohort with exposure + infection markers + timing in the same people): first SARS-CoV-2 row, extending the rung to a third pathogen after influenza (Kim 2012, Sauter 2026, Tsang 2023) and RSV (Munywoki 2014). Nearest-neighbor design to Munywoki 2014: serial symptom-independent swabs of all household members; here contacts were enrolled pre-existing-infection-free (prior confirmed/suspected infection excluded), swabbed near-daily for 28 days, and sequenced - with the transmission-from-index assumption doing work Munywoki's G-gene sequencing did more directly.
- SARS-CoV-2 ladder/audit: adds the natural-route human-transmission rung to [[synthesis/sars-cov-2-covid-causation-audit]], which previously held only the uncontrolled challenge model (Killingley 2022) and animal/characterization rows.
- Cross-cutting ladder note extended in [[synthesis/viral-disease-causation-evidence-ladder]].

## Related
- [[sources/munywoki-2014-rsv-infant-source-household-cohort]] - the GAP 3 RSV row (same serial-swab-all-members design)
- [[sources/kim-2012-kenya-household-pdm09-transmission-cohort]] and [[sources/sauter-2026-phirst-influenza-household-transmission]] - GAP 3 influenza rows
- [[sources/tsang-2023-hong-kong-household-asymptomatic-transmission-reconstruction]] - GAP 3 model-reconstruction row; its asymptomatic-infectiousness parameter pairs with this cohort's 5/32 asymptomatic secondary infections
- [[synthesis/sars-cov-2-covid-causation-audit]]
- [[synthesis/viral-disease-causation-evidence-ladder]]
- [[synthesis/source-verification-queue]]
