---
title: Reconstructing Household Transmission Dynamics to Estimate the Infectiousness of Asymptomatic Influenza Virus Infections
category: source
summary: 2023 PNAS Bayesian transmission-model reconstruction of the Hong Kong 2009 pandemic H1N1 household cohort (727 households, 2,515 members; infection = >=4-fold HAI rise and/or positive PCR) - asymptomatic cases were an estimated 36% of infections with relative infectiousness 0.57 vs symptomatic cases (95% CrI 0.11-1.54); the authors' own power analysis (0.48 at the estimated effect size) and a CrI that includes 1.0 are recorded on the page.
tags:
  - influenza
  - influenza-virus
  - household-transmission
  - prospective-cohort
  - transmission-modeling
  - asymptomatic-infection
  - serology-endpoint
  - bayesian-methods
  - evidence-synthesis
sources: 1
updated: 2026-11-10
claim_status: supported
claim_type: empirical
source_tier: tier-1
evidence_role: model-based reconstruction of a prospective household cohort with exposure, infection markers, and timing in the same people; GAP 3 third influenza row (model-final-size design layer)
pmid: 37549267
pmcid: PMC10436695
doi: 10.1073/pnas.2304750120
---

# Reconstructing Household Transmission Dynamics to Estimate the Infectiousness of Asymptomatic Influenza Virus Infections

## Source type
- Role in this vault: model-reconstruction layer over the Hong Kong 2009 H1N1pdm09 household cohort data - the vault's third full-text GAP 3 influenza row (queue item 19, fulfilling the run-11 lead) and the first in which the transmission quantities themselves are posterior estimates from a Bayesian individual-based model fitted to serology, PCR, and symptom-diary data rather than directly tabulated counts.
- Journal/year: *Proceedings of the National Academy of Sciences*, 2023;120(33):e2304750120 (brief report; received 2023-03-23, accepted 2023-07-15; CC BY-NC-ND 4.0)
- Authors: Tim K. Tsang, Cana Wang, Vicky J. Fang, Ranawaka A. P. M. Perera, Hau Chia So, Dennis K. M. Ip, Gabriel M. Leung, J. S. Malik Peiris, Simon Cauchemez, Benjamin J. Cowling - HKU WHO Collaborating Centre / School of Public Health, Laboratory of Data Discovery for Health, HKU-Pasteur Research Pole, Institut Pasteur Paris
- Source basis in hand: complete open-access full text from Europe PMC (PMC10436695) - Abstract, Results, Discussion, Methods, stated limitations, figure caption, and reference list read end to end.

> [!warning] Warning
> This page is for research analysis only. It is not medical advice.

## Evidence fields
| Field | Extraction |
|---|---|
| Study type | Bayesian transmission-model reconstruction (secondary analysis) of household-cohort data. The Methods state the data source precisely: "We analyzed data collected from two community-based randomized controlled trials aimed at evaluating the benefits of influenza vaccination" (Hong Kong 2008/09 and 2009/10 studies; ref 10 = Cowling et al., *Clin Infect Dis* 2012;55:695-702). An individual-based household transmission model ("assuming that the hazard of infection was additive") was fitted with added time components so symptom diaries could inform the fit; "We developed a Bayesian methodology to overcome the challenge that transmission events could not be directly observed." Analysis restricted to the first epidemic wave of influenza A(H1N1)pdm09 in 2009 |
| Subjects | 3,160 individuals participated in the two studies, 301 in both; households with unknown infection status for all members excluded; **727 households with 2,515 household members analyzed**. In the first wave, 397/625 (64%) children and 315/1,239 (25%) adults were infected. "Almost all participants have a preseason HAI titer <10" (Dataset S1) - a seronegative, pandemic-naive population |
| Exposure / surveillance | Natural household + community exposure during the pandemic wave. Infection status from paired sera (four collection rounds, R1-R4) and self-collected swabs; symptoms from self-reported diaries (passive surveillance). Community infection risk enters the model through a proxy influenza-activity curve aligned to local pH1N1 activity (Fig. 1E). Recently vaccinated individuals excluded, "because the rise in Hemagglutination-inhibition titer from vaccination is indistinguishable from natural infections" |
| Comparator / control | Sham arm: **no** - an observational cohort reanalysis cannot have sham infection. Internal contrast: cases with no symptoms vs at least one symptom (main analysis); cases without acute respiratory illness (ARI: >=2 of fever >=37.8 C, cough, runny nose, sore throat, headache, phlegm, myalgia) vs with ARI (alternative analysis) |
| Endpoint (named exactly) | **Relative infectiousness of asymptomatic vs symptomatic influenza cases** - a model parameter (per-case household-transmission probability ratio). Companion estimates: probability of community infection (33% children, 12% adults), transmission probability from a symptomatic case to a household member (15% child case, 5% adult case), relative susceptibility of children (3.2x adults), proportion of cases with at least one symptom (64% overall) or ARI (46% overall), proportion of infections attributed to household transmission (12%), and proportion of household transmission attributed to asymptomatic cases (26%) |
| Result | Infection endpoint: "a fourfold or greater rise in antibody titers in his/her paired sera and/or a positive PCR in any collected swabs." **36% of cases asymptomatic (95% CrI 32-40%)**; "The posterior probability that asymptomatic cases are less infectious than symptomatic cases is 0.82, with estimated relative infectiousness 0.57 (95% CrI: 0.11, 1.54)." Alternative ARI definition: relative infectiousness 0.41 (95% CrI 0.07-1.09); "Estimates for other parameters are similar." Misclassification simulation: nondifferential symptom misclassification biases the ratio by 0.10 (at 0.2) and 0.24 (at 0.4). Retrospective power: 0.48 / 0.80 / 0.98 if the true relative infectiousness were 0.57 / 0.41 / 0.25; at the estimated 0.57, 0.75-0.86 power would need 1,500-2,000 households. Sensitivity analyses varying serial-interval/incubation assumptions gave similar point estimates |
| Main limitation | Authors' own list: (1) "the reliability of estimates depended on the accuracy of the proxy measure of influenza activity"; (2) results "may apply to only households but not to other settings"; (3) recently vaccinated individuals excluded (limits generalizability); (4) data are from the H1N1pdm09 pandemic only, "which may not be generalizable to other influenza subtypes." Also stated by the authors: fixing serial-interval/incubation parameters "may underestimate the uncertainty of estimates," and "Our results could not rule out the possibility that asymptomatic cases could be equally infectious" |

## What the experiment can answer
- That in 727 Hong Kong households under pandemic exposure, infection (>=4-fold HAI rise and/or PCR) reached 64% of children and 25% of adults in one wave, with an estimated 36% of all cases showing no symptoms on self-reported diaries - a serology-plus-PCR burden measurement independent of care-seeking.
- That a Bayesian final-size-plus-timing model fitted to those data yields a central estimate that asymptomatic cases transmit onward within households at roughly half the rate of symptomatic cases (0.57), with an 82% posterior probability of being less infectious - and, by the authors' own simulation, that the design had only 0.48 power at that effect size, i.e., this dataset cannot reliably distinguish 0.57 from no difference.

## What it cannot answer
- Transmission events directly: "transmission events could not be directly observed" (Methods). Every transmission quantity - who infected whom, when, and how infectious each class of case is - is a posterior estimate conditioned on a proxy activity curve, paired sera taken in four coarse rounds, and self-reported diaries.
- Whether asymptomatic cases are less infectious: the 95% CrI (0.11-1.54) includes 1.0, and the authors say so.
- Route of transmission, community-vs-household attribution beyond model structure, and any clinical severity outcome (none analyzed).
- Generalization to seasonal subtypes, post-2009 populations, or non-household settings (authors' own boundary).

## Inferential leaps to watch
- Abstract and Discussion headline the 0.57 point estimate and P=0.82 while the same paper's power analysis shows the study was underpowered (0.48) at exactly that value; the leap from "posterior central estimate 0.57" to "asymptomatic cases are about half as infectious" is not licensed by the paper's own uncertainty statement ("More data are required..." - final sentence).
- Community infection risk is carried by a proxy influenza-activity curve; mis-timing of that curve shifts all transmission attribution, and the authors concede fixed serial-interval assumptions may understate uncertainty.
- The framing that modeling studies "typically assume that asymptomatic infections are half to two-thirds as infectious" and the closing suggestion that quarantine of contacts "may be useful" import the result into policy territory the design (no interventions, model-based attribution) does not test.
- The consistency claim vs the South Africa PHIRST study (ref 12, Cohen et al. 2021, Lancet Glob Health, "~60% less infectious") compares two different surveillance regimes - passive diaries here, twice-weekly active swabs there - a partial replication only.

## Which gap and ladder rung this fills
- Queue GAP 3 (prospective cohort with exposure + infection markers + timing in the same people): third influenza row. It is the model-reconstruction companion to [[sources/kim-2012-kenya-household-pdm09-transmission-cohort]] (reported-ILI secondary endpoint) and [[sources/sauter-2026-phirst-influenza-household-transmission]] (serially PCR-observed episodes): here the infection endpoint is serology+PCR in a seronegative pandemic-naive cohort, but the transmission structure (who acquired infection from whom, asymptomatic vs symptomatic infectiousness) is inferred by the model rather than observed. Fills the analysis-layer slot between the two directly observed rows and adds the asymptomatic-infectiousness parameter neither supplies.
- Influenza ladder: "prospective household cohort, natural exposure (GAP 3)" rung extended from two rows to the three-row set in [[synthesis/influenza-influenza-virus-evidence-ladder]]; cross-cutting note extended in [[synthesis/viral-disease-causation-evidence-ladder]].

## Related
- [[sources/kim-2012-kenya-household-pdm09-transmission-cohort]] - first GAP 3 influenza row (Kenya PBIDS, self-reported secondary ILI)
- [[sources/sauter-2026-phirst-influenza-household-transmission]] - second GAP 3 influenza row (South Africa PHIRST, serially PCR-observed episodes)
- [[sources/cowling-2009-household-facemask-hand-hygiene-rct]] - the randomized natural-route row (same HKU group's earlier household platform)
- [[synthesis/influenza-influenza-virus-evidence-ladder]]
- [[synthesis/viral-disease-causation-evidence-ladder]]
- [[synthesis/virus-causation-inferential-leaps]]
- [[synthesis/source-verification-queue]]
