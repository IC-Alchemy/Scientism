---
title: Household Transmission and Genomic Diversity of Respiratory Syncytial Virus in the United States, 2022-2023 (CASCADIA)
category: source
summary: 2025 CID analysis of the CASCADIA prospective community cohort (Seattle + Portland, 1,009 multi-person households, 3,058 participants aged 6 months-50 years, weekly at-home nasal swabs and symptom surveys irrespective of symptoms, 2022-2023) - RSV detected in 10% of participants and 20% of households; secondary RSV infection within 14 days of a distinct index case in 37/369 (10.0%) household contacts; 89% of index cases children <=12 years; whole-genome sequencing corroborates within-household transmission for same-household pairs <=14 days apart.
tags:
  - household-transmission
  - rsv
  - prospective-cohort
  - natural-route-transmission
  - pcr-endpoint
  - genomic-confirmation
  - evidence-synthesis
sources: 1
updated: 2026-11-10
claim_status: supported
claim_type: empirical
source_tier: tier-1
evidence_role: prospective household cohort with exposure, infection markers, and infection timing in the same people; GAP 3 replication row for RSV (second row, first high-income-country row, with genomic corroboration)
pmid: 40084542
pmcid: PMC13613862
doi: 10.1093/cid/ciaf048
---

# Household Transmission and Genomic Diversity of Respiratory Syncytial Virus in the United States, 2022-2023 (CASCADIA)

## Source type
- Role in this vault: the vault's second full-text GAP 3 RSV row and its first in a high-income country, replicating the design of [[sources/munywoki-2014-rsv-infant-source-household-cohort]] (rural Kenya, 2012 season) in the post-pandemic United States and adding whole-genome sequencing as a check on the timing-based transmission inference; fills queue item 24 in [[synthesis/source-verification-queue]].
- Journal/year: *Clinical Infectious Diseases* 2025;81(6):1159-1169 (online 2025-03-11; issue collection date 2025-12-15; Oxford University Press Standard Journals Publication Model author manuscript in PMC). Europe PMC lists pubYear 2026; the PMC page itself prints "Clin Infect Dis. 2025 Mar 11;81(6):1159-1169" - the 2025 citation is used here and the discrepancy recorded.
- Authors: Sarah N. Cox, Pavitra Roychoudhury, Collrane Frivold, Zack Acker, Tara M. Babu, Cassandra L. Boisvert, Marco Carone, ... Lea M. Starita, Alexandra Varga, Neil Yetz, Allison L. Naleway, Ana A. Weil, Helen Y. Chu - University of Washington, Brotman Baty Institute, Fred Hutchinson Cancer Center, Kaiser Permanente Center for Health Research (Portland), Seattle Children's, US CDC (contract 75D30121C12297).
- Source basis in hand: complete author-manuscript full text from PMC (PMC13613862) - Abstract, Methods (study design, data collection, laboratory testing, sequencing, statistical analysis), Results with Tables 1-2 and figure captions, Discussion with the authors' limitations list, Conclusions.

> [!warning] Warning
> This page is for research analysis only. It is not medical advice.

## Evidence fields
| Field | Extraction |
|---|---|
| Study type | Prospective community-based cohort study (CASCADIA platform), 1 June 2022-31 May 2023, metropolitan Seattle (University of Washington catchment: King/Snohomish/Pierce Counties) and Portland (Kaiser Permanente Northwest catchment); remote active surveillance; no randomization, no intervention |
| Subjects | 1,009 multi-person households (of 1,188 eligible) with 3,058 enrolled participants aged >=6 months to 50 years; 97% household retention over the study year; only 52% of households had complete ascertainment (all members enrolled); median 3 participants/household (2-8); 75.9% of analysis households reported income >$100,000 (authors flag affluent skew as a limitation) |
| Exposure / surveillance | At least weekly self-/parent-collected anterior nasal swabs and online symptom surveys **irrespective of symptoms**, plus an illness-triggered extra swab when >=1 new ARI symptom (fever, cough, sore throat, shortness of breath, myalgia, rhinorrhea) appeared >72 h after the last swab; baseline and semi-annual/annual serum, plus draws 30 days after infection or vaccination; serum RSV prefusion IgG by electrochemiluminescence immunoassay (Mesoscale), log-AU/mL; household co-residence with an incident RSV illness episode is the exposure; index case = first household member with RSV detected; co-primary = same-date detections |
| Comparator / control | Sham arm: **no** - an observational cohort cannot have sham infection; no comparison households. Internal contrasts (Table 2, log-linear Poisson GEE with robust SEs clustering by household): index viral detection >=1 week vs <1 week; contact age 6m-4y / 5-12y vs 13-50y; baseline RSV binding-antibody titers <= vs > median (5.1 log-AU/mL) of index and contact; index Ct (Crt) <= vs > median 18.9; site UW vs KPNW; asymptomatic vs symptomatic index |
| Endpoint (named exactly) | **"Potential secondary household transmission was defined as additional household member(s) with RSV detected 1-14 days after the identified index case(s) to align with the weekly testing protocol and prior RSV transmission studies"** - i.e., secondary RSV infection among contacts within <=14 days of the index case, where RSV positivity is RT-qPCR Ct <=37 or relative cycle threshold (Crt) <28 in a custom TaqMan Open Array panel; generation interval = days between index's and secondary case's first RSV-positive specimen; corroboration endpoint: whole-genome sequences (specimens Crt <18.5) with pairwise nucleotide differences compared between same-household detections <=14 days and >14 days apart |
| Result | RSV detected in 310/3,058 (10%) individuals within 200/1,009 (20%) households (5 Sept 2022-18 May 2023; 248 RSV A, 57 RSV B, 5 A+B at a median 77 days apart); 8 possible repeat RSV A infections (3%); of 200 incident household illness episodes, 170 had a distinct index case (30 co-primary excluded from the primary analysis). **37 secondary transmissions among 369 contacts = 10.0% (95% CI 7.0-14.4)**; 27/170 (16%) households had >=1 secondary case; median generation interval 7 days (IQR 7-13); sensitivity analyses 8.2-10.7%. Index cases children <=12 y in 24/27 (89%) (median 6 y); secondary cases adults in 21/37 (57%) (median 35 y). Adjusted RRs: contact age 6m-4y 3.49 (1.30-9.38), 5-12y 2.41 (1.05-5.50) vs 13-50y; **index viral detection >=1 week 5.62 (2.62-12.06)**; index viral codetection 0.32 (0.13-0.79); contact influenza vaccination 0.36 (0.15-0.84) (observational, season-confounded); **no association** with index viral load (Crt), baseline RSV binding-antibody titers of index or contact (all p>=.167); unexplained site contrast UW 14% vs KPNW 4% (aRR 5.50, 2.76-10.96); asymptomatic index contrast unstable (unadjusted 0.79, adjusted 3.63 [0.84-15.68], p=.084); among 11 asymptomatic index cases only 2 had secondary cases; 94% of index cases symptomatic; few sought care. Genomics: 120 specimens sequenced (93 RSV A: A.D.5.2 n=37, A.D.1 n=30, A.D.3 n=12, A.D.2.1 n=6; 27 RSV B: B.D.E.1 n=24, B.D.4.1.1 n=2); 19 households with >=2 cases: same-household pairs <=14 days apart differed by a mean 4 nucleotides [range 0-13] (n=17 households) vs 137 [37-236] (n=2) >14 days apart; no <=14-day same-household pair was from different clades; 1 participant shed one lineage (A.D.5.2) at 100% pairwise identity over 40 days (persistent shedding), another had two different subtypes 196 days apart (new infection) |
| Main limitation | Authors' own list: self-reported symptoms/behaviors (recall/social-desirability bias); asymmetric swabbing (symptomatic persons swabbed more often than asymptomatic, so index and episode detection may be misclassified); incomplete household enrollment (only 52% complete ascertainment, primary analysis retained partial households); baseline sera drawn at times unrelated to the illness episode (titer at infection unknown); sequencing lag prevents real-time disambiguation; only high-viral-load specimens sequenced; weekly cadence cannot capture peak viral load; affluent, high-income, mostly insured households limit generalizability |

## What the experiment can answer
- That in ordinary US households under weekly symptom-independent PCR, 10% of contacts acquired PCR-defined RSV within 14 days of an index case and 1 in 6 infected households produced a secondary case, with a median index-to-secondary interval of 7 days - a direct infection-based household transmission measurement in the post-mitigation, pre-RSV-immunization 2022-2023 season.
- That young children (<=12 years) were the introducers in 89% of households with a distinct index case and that secondary infections concentrated in adults and in contacts <=12 years - a direction-of-flow measurement from timed detections in the same population.
- That index episodes with viral detection >=1 week carried 5.6x the transmission risk of shorter episodes, while the index's (Ct-based) viral load and both parties' baseline binding-antibody titers showed no detectable association - a duration-vs-titer dissociation measured inside one cohort.
- That whole-genome sequencing is consistent with the timing-based attribution: same-household detections <=14 days apart were near-identical (mean 4 nt) and never cross-clade, vs 137 nt mean for >14-day pairs.

## What it cannot answer
- Transmission route: co-residence bundles droplet/fomite/aerosol contact; no route was measured.
- Severity or disease outcomes: endpoints are PCR detections and symptom reports; hospitalizations and lower-airway disease are not attributed to transmission events.
- Asymptomatic-relative-infectiousness: only 11 asymptomatic index cases (2 with secondary cases) - the adjusted contrast is unstable and the paper does not claim a precise ratio.
- Whether the influenza-vaccination association (aRR 0.36) is causal: it is an observational, strongly confounding-prone contrast (healthcare-seeking, health behavior), made in an RSV analysis.
- Generalizability beyond affluent, mostly complete-enrollment US households; only 19 of the 27 transmitting households contributed genomic pairs.

## Inferential leaps to watch
- "Most RSV household transmission occurs from infants and young children to adults" (Conclusions) - direction of transmission is inferred from the 1-14-day temporal ordering of detections, not from per-pair genomic directionality; sequencing corroborates within-household transmission (near-identity <=14 days) but cannot by itself identify which member introduced the virus. The leap is partially bridged in-house (near-identical genomes in <=14-day pairs) but is still an inference from timing.
- The plain-language summary states "RSV transmission occurred in 10% of household contacts" - what the design defines is *potential secondary transmission* by a timing window; the genomic corroboration covers only 17 of those households (mean 4 nt differences could in principle still represent two community introductions of the same circulating lineage in a high-circulation season).
- "These findings can be used to identify target populations for novel RSV prevention measures" - a leap from cohort observation to immunization-targeting policy; no intervention was tested.

## Relationship to other vault pages
- Second RSV row of the GAP 3 rung in [[synthesis/viral-disease-causation-evidence-ladder]] and [[synthesis/bronchiolitis-rsv-evidence-ladder]], replicating [[sources/munywoki-2014-rsv-infant-source-household-cohort]] across hemisphere, income setting, and season (Kenya 2012: school-children dominant introducers, 53.6% of infant infections within-household; US 2022-23: children <=12 dominant introducers, 16% of distinct-index households with a secondary case).
- Its duration-of-detection result (>=1 week, aRR 5.62) is the observational counterpart of the shedding-duration theme in [[sources/munywoki-2014-rsv-infant-source-household-cohort]] and the Ct-trajectory reconstructions in [[sources/sauter-2026-phirst-influenza-household-transmission]] and [[sources/tsang-2023-hong-kong-household-asymptomatic-transmission-reconstruction]].

## Related
- [[synthesis/bronchiolitis-rsv-evidence-ladder]]
- [[synthesis/viral-disease-causation-evidence-ladder]]
- [[synthesis/source-verification-queue]]
- [[sources/munywoki-2014-rsv-infant-source-household-cohort]]
- [[sources/devincenzo-2010-rsv-human-challenge-model-validation]]
- [[concepts/inferential-leap]]
