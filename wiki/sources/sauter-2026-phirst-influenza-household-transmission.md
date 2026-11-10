---
title: The Roles of Pre-Season Immunity, Age, Viral Shedding, and Community Exposures in Shaping Influenza Household Transmission Dynamics
category: source
summary: 2026 Nat Commun analysis of the South Africa PHIRST prospective household cohort (327 households, twice-weekly nasopharyngeal swabs of every member regardless of symptoms, pre-season HAI sera, 2016-2018) - influenza infection episodes by rRT-PCR in 1,518 people; household and community exposure intensity, pre-season HAI >=1:40 (protective for 3 of 4 subtypes), and age were independently associated with infection acquisition.
tags:
  - household-transmission
  - influenza
  - influenza-virus
  - prospective-cohort
  - natural-route-transmission
  - pcr-endpoint
  - immunity-correlates
  - evidence-synthesis
sources: 1
updated: 2026-11-10
claim_status: supported
claim_type: empirical
source_tier: tier-1
evidence_role: prospective household cohort with exposure, infection markers, and infection timing in the same people; GAP 3 replication row for influenza with serially PCR-observed infections
pmid: 42669676
pmcid: PMC13526887
doi: 10.1038/s41467-026-76037-x
---

# The Roles of Pre-Season Immunity, Age, Viral Shedding, and Community Exposures in Shaping Influenza Household Transmission Dynamics

## Source type
- Role in this vault: analysis of the PHIRST prospective household cohort (Prospective Household cohort study of Influenza, Respiratory Syncytial virus, and other respiratory pathogens community burden and Transmission dynamics in South Africa) - the vault's second full-text GAP 3 influenza row and the first in which infections themselves (not reported symptoms) are serially observed by PCR in every household member; fills the replication slot next to [[sources/kim-2012-kenya-household-pdm09-transmission-cohort]] in [[synthesis/source-verification-queue]].
- Journal/year: *Nature Communications*, 2026;17:9238 (published 2026-07-30; CC-BY 4.0)
- Authors: Molly K. Sauter, Jackie Kleynhans, Jocelyn Moyes, Meredith L. McMorrow, Florette K. Treurnicht, Orienka Hellferscee, Anne von Gottberg, Nicole Wolter, Amelia Buys, Lorens Maake, Neil A. Martinson, Kathleen Kahn, Limakatso Lebina, Katlego Motlhaoleng, Floidy Wafawanaka, Francesc Xavier Gomez-Olive, Stefano Tempia, Bryan Grenfell, Cecile Viboud, Kaiyuan Sun, Cheryl Cohen - NIH Fogarty International Center, Princeton, NICD/NHLS Johannesburg, US CDC, Wits University, Westlake University
- Source basis in hand: complete open-access full text from Europe PMC (PMC13526887), including Results, Discussion, Methods (study design, laboratory testing, analytical approach), figure captions, and stated limitations.

> [!warning] Warning
> This page is for research analysis only. It is not medical advice.

## Evidence fields
| Field | Extraction |
|---|---|
| Study type | Prospective household cohort with individual-level transmission modeling; two South African sites (rural Agincourt HDSS, Mpumalanga; urban Jouberton, Klerksdorp, North West); fresh cohorts enrolled each year 2016-2018 before the influenza season; intensive follow-up 6 months (2016) or 10 months (2017-2018); no randomization, no intervention |
| Subjects | 327 households and 1,684 individuals enrolled and completed follow-up across the three years; 1,518 individuals included in the analysis (480 in 2016, 523 in 2017, 515 in 2018) with complete samples and analyzed pre-season titers; 56% <18 years; 16% living with HIV (19% of those with CD4 <200); **no individual had received an influenza vaccine for the current year** - deliberately a natural-immunity population |
| Exposure / surveillance | Twice-weekly household visits collecting nasopharyngeal swabs from every member **regardless of symptoms** ("symptom-independent routine testing"); pre-season serum for hemagglutination-inhibition (HAI) titers against A/South Africa/2517/2016 (A(H1N1)pdm09), A/Singapore/INFIMH-16-0019/2016 (A(H3N2)), B/South Africa/R3037/2016 (B/Victoria), B/South Africa/R05631/2017 (B/Yamagata). Household force of infection (FOI) = daily total viral load in the household reconstructed from members' Ct trajectories via a Bayesian piecewise-linear shedding-kinetics model (100 posterior resamples); community FOI = fraction of the enrolled cohort with an active PCR-confirmed episode |
| Comparator / control | Sham arm: **no** - an observational cohort cannot have sham infection; the paper has no comparison households. Internal contrasts: pre-season HAI <1:40 vs >=1:40, age strata vs >=40 years reference, HIV status strata, household size, and time-varying exposure intensity (per 10-Ct-unit steps) within the same population |
| Endpoint (named exactly) | **Influenza infection episode**: rRT-PCR (FTD Flu/RSV detection assay) Ct <37, clustered as one episode when the same subtype/lineage and positive samples <14 days apart (25 coinfections, 4% of episodes, excluded); daily infection-acquisition risk modeled by multivariable Poisson regression (equivalent to Cox here), fitted to the 100 resampled shedding trajectories and pooled by Rubin's rules; secondary endpoints: shedding duration and peak viral load (estimated minimum Ct); immunity marker: pre-season HAI titer >=1:40 |
| Result | 1,258 influenza-positive specimens (~1% of all specimens); **513/1,518 individuals (34%) had >=1 influenza infection episode**; episodes by year 174/239/210. (a) Household FOI: a 10-Ct-unit increase in household viral load raised acquisition risk HR 1.96 (1.58-2.44) for A(H1N1)pdm09, 1.64 (1.32-2.03) A(H3N2), 1.77 (1.42-2.20) B/Victoria, 1.70 (1.15-2.52) B/Yamagata. (b) Community FOI: a 0.01 rise in cohort prevalence (peak 5-6%) raised risk HR 1.89-2.01 across subtypes. (c) **Pre-season HAI >=1:40 was protective for three of four subtypes**: HR 0.30 (0.18-0.48) pdm09, 0.65 (0.45-0.93) H3N2, 0.48 (0.31-0.74) B/Victoria; no B/Yamagata effect at the 1:40 threshold (a continuous-titer sensitivity analysis did find an association). (d) Age, vs >=40 y: <5 y HR 2.69 (1.33-5.46) pdm09, 5.65 (2.85-11.21) B/Victoria, 3.19 (1.33-7.65) B/Yamagata; 5-11 y HR 5.66 (2.98-10.73) B/Victoria; 12-18 y HR 2.04 (1.19-3.49) H3N2, 2.17 (1.07-4.42) B/Victoria, 3.42 (1.61-7.23) B/Yamagata. (e) For B/Yamagata: PLWH with CD4 <200 HR 4.07 (1.20-13.86), CD4 >=200 HR 2.65 (1.33-5.28); each extra household member HR 0.88 (0.80-0.98). Children had longer shedding and higher estimated peak viral load than adults after titer adjustment; pre-season HAI also shortened pdm09 shedding. Per-subtype analysis bases: 923 (pdm09), 500 (H3N2), 866 (B/Vic), 507 (B/Yam) individuals. No multiple-comparison adjustment (stated in Fig. 5 caption) |
| Main limitation | Authors' own list: 2-3-day sampling gaps can miss short episodes; Ct is an indirect, uncalibrated viral-load proxy; pre-season HAI assumed constant through the season; coinfections excluded; the transmission model lacks contact-structure (behavior vs biology of age effects not separable); community FOI is an internal-cohort prevalence proxy (no independent site surveillance); the unvaccinated cohort limits generalizability; B/Yamagata was underpowered (and is now extinct post-COVID); pre-COVID-period data only |

## What the experiment can answer
- That under symptom-independent, twice-weekly PCR of every household member across three seasons, one third of this unvaccinated, young, high-HIV-prevalence South African population acquired >=1 PCR-defined influenza infection per year - a direct infection-based household burden measurement, independent of care-seeking or symptom reporting.
- That measured infection risk rose with reconstructed household viral-load exposure (HR ~1.6-2.0 per 10-Ct-unit) and with community prevalence (HR ~1.7-2.0 per 0.01) - an exposure-response structure inside natural households.
- That naturally acquired pre-season HAI >=1:40 tracked 50-70% lower infection risk for A(H1N1)pdm09, A(H3N2), and B/Victoria (not B/Yamagata), and that age remained associated with risk after titer and exposure adjustment - i.e., the classic 1:40 correlate-of-protection observation, replicated in natural (non-vaccine) immunity.

## What it cannot answer
- Whether the household-exposure association is causal exposure-response: the exposure variable is *reconstructed from the same household members' infection episodes* being modeled (posterior-resampled to propagate uncertainty, but not an independent exposure measurement), so circularity between "who is infected" and "how much exposure their household generated" cannot be fully excluded.
- Transmission route: co-residence bundles droplet/fomite/aerosol contact; the model has no contact structure.
- Clinical disease endpoints: acquisition and shedding are the endpoints; no severity outcome is attributed to any transmission event.
- Generalization to vaccinated populations, to post-2019 immunity landscapes, or to B/Yamagata (underpowered and extinct).

## Inferential leaps to watch
- The introduction claims symptom-independent testing "permits... direct observation of transmission events" - what is directly observed is serial PCR positivity; transmission events, episode onset ("infection onset defined as one day prior to the first observed shedding day"), and exposure intensity are model reconstructions from Ct trajectories calibrated to challenge-study kinetics. The leap from observed serial Ct curves to timed transmission events is an inference and is recorded as such.
- The 1:40 HAI protection benchmark is imported from vaccine-mediated adult studies; applying it to natural immunity in children and PLWH is an extrapolation the authors partially flag.
- "Viral shedding intensity was predictive of risk" is presented in the discussion alongside human-challenge dose-response as if the same quantity were measured; here exposure is a Ct-based proxy (authors concede Ct is "not a direct measure"), and the comparison to challenge dose is an analogy, not a measured dose.
- Policy framing (control strategies informed by asymptomatic transmission, post-COVID immunity-gap predictions) goes beyond the cohort's design; the paper's own concluding sentences mark those as open questions.

## Which gap and ladder rung this fills
- Queue GAP 3 (prospective cohort with exposure + infection markers + timing in the same people): second influenza row, the replication of [[sources/kim-2012-kenya-household-pdm09-transmission-cohort]] - and, on endpoint quality, the stronger of the two: infections are serially PCR-observed regardless of symptoms, where Kim 2012's secondary endpoint was self-reported ILI. Both agree that co-residence with a PCR-confirmed case carries measurable infection risk; PHIRST adds exposure-response structure and a natural-immunity protection gradient.
- Influenza ladder: "prospective household cohort, natural exposure (GAP 3)" rung extended from one row to the two-row set in [[synthesis/influenza-influenza-virus-evidence-ladder]]; cross-cutting note extended in [[synthesis/viral-disease-causation-evidence-ladder]].

## Related
- [[sources/kim-2012-kenya-household-pdm09-transmission-cohort]] - the first GAP 3 influenza row (Kenya, self-reported secondary endpoint)
- [[sources/munywoki-2014-rsv-infant-source-household-cohort]] - the GAP 3 RSV row written this run
- [[sources/cowling-2009-household-facemask-hand-hygiene-rct]] - the randomized natural-route row above the cohort rung
- [[sources/memoli-2015-h1n1pdm09-human-challenge-model-validation]] and [[sources/han-2021-cr6261-placebo-controlled-h1n1pdm09-challenge]] - the inoculation rungs whose shedding-kinetics calibration this cohort's model borrows
- [[synthesis/influenza-influenza-virus-evidence-ladder]]
- [[synthesis/viral-disease-causation-evidence-ladder]]
- [[synthesis/source-verification-queue]]
