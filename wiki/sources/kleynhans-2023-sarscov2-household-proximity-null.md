---
title: Association of close-range contact patterns with SARS-CoV-2 - a household transmission study
category: source
summary: Kleynhans et al. 2023 (eLife 12:e84753) report a nested contact substudy of the South African case-ascertained prospective household transmission study (SA-S-HTS, Klerksdorp and Soweto, Oct 2020-Sept 2021) - wearable RFID proximity sensors worn for two weeks by 340 household members of 88 rRT-PCR-confirmed index cases, measuring every face-to-face (<1.5 m, 20-second resolution) contact with index cases and with all infected members; nasal swabs collected on three household visits per week; endpoint rRT-PCR-confirmed SARS-CoV-2 acquisition - and found NULL on every contact parameter (duration, frequency, cumulative time, aOR 1.0-1.1) while index minimum Ct<30 (aOR 10.4-16.8 vs Ct>35) and female contact sex (aOR ~2.4) carried the risk; sleeping in the same room as the index was null (OR 0.94); 153/252 contacts (60.7%) infected.
tags:
  - sars-cov-2
  - household-transmission
  - prospective-cohort
  - proximity-sensors
  - rfid-contact-measurement
  - pcr-confirmed-endpoint
  - null-result
  - south-africa
sources: 1
updated: 2026-11-10
claim_status: supported
claim_type: empirical
source_tier: tier-1
evidence_role: natural-route human-transmission cohort with directly measured exposure (sensor-logged face-to-face contact), serial PCR, and infection-timing data in the same people; second GAP 3 row for SARS-CoV-2 and the corpus's only transmission study with instrument-measured exposure
pmid: 37461328
doi: 10.7554/eLife.84753
pmcid: PMC10359094
---

# Kleynhans et al. 2023 - close-range contact patterns and SARS-CoV-2 household transmission (SA-S-HTS contact substudy)

> [!note] Note
> Full text read and verified 2026-11-10 (loop run 17, queue item 31) from the complete Europe PMC full-text XML of eLife 2023;12:e84753 (PMC10359094, CC-BY), including the peer-review exchange appended to the record. Every number below is from that full text, not from the abstract. Authors: Kleynhans J, Dall'Amico L, Gauvin L, Tizzoni M, Maloma L, Walaza S, Martinson NA, von Gottberg A, Wolter N, Makhasi M, Cohen C, Cattuto C, Tempia S; SA-S-HTS Group. The parent study's design is described here as reported by this paper, which cites the main-study methods paper (Kleynhans et al. 2022b, "Household transmission of SARS-CoV-2 from adult index cases living with and without HIV in South Africa, 2020-2021: a case-ascertained, prospective observational household transmission study").

## What experiment was run

- **Study type:** case-ascertained, prospective household transmission study (the main SA-S-HTS cohort) with a nested contact-measurement substudy; two urban South African communities, Klerksdorp (North West) and Soweto (Gauteng), October 2020 through September 2021. Sample size was computed for the main study (440 exposed household members), "but not the nested contact study."
- **Subjects and enrollment:** symptomatic adults (>18 years, symptom onset <=5 days) screened at clinics by rRT-PCR on nasopharyngeal swab; positives enrolled as presumptive index cases if the household had >=2 contacts and no household member had reported symptoms before the index's onset; serum collected at first and final visit (in-house spike ELISA + Roche Elecsys nucleocapsid); persons seropositive at baseline with no PCR-confirmed infection during follow-up were excluded from the acquisition analysis. In the contact substudy: contact data available for 88 index cases and 252 household contacts; 93 individuals (19%: 36 index, 73 contacts) excluded for sensor non-compliance (no contacts logged or stationary sensors by accelerometer). Median household size in the analysis 4 members (IQR 3-5); median 3 PCR-positive members per household; median 67% of household members infected including the index.
- **Exposure measurement (the distinctive element):** wearable RF proximity sensors (Cattuto et al. 2010 design) worn for two weeks, pinned to clothing or on a lanyard; packet exchange with RSSI thresholding defined face-to-face proximity within **<1.5 meters**; a contact = consecutive 20-second intervals with at least one packet; accelerometer movement required within each 5-minute slice (contacts while sitting/standing still retained); events from hand-out/collection days excluded; Klerksdorp timestamp faults repaired by cross-correlation time-series alignment between tag pairs. Participants were asked to wear sensors at home and to store them separately at night; field workers checked wearing at visits.
- **Follow-up and sampling:** households visited **three times a week** for nasal swabs, symptom data, and health-care-seeking data; rRT-PCR Allplex 2019-nCoV kit; first positives characterized by variant PCR and Ion Torrent whole-genome sequencing; households with more than one variant circulating (mixed clusters) excluded from analysis.
- **Comparator/control:** none (observational cohort - no sham arm; the design has no allocation, recorded explicitly).
- **Endpoint (named exactly):** "Any household member testing positive for SARS-CoV-2 within two weeks from the last positive result for the index case was considered a secondary SARS-CoV-2 case" (Methods, Data analysis); the association analyses use the outcome "testing positive for SARS-CoV-2" during follow-up (Table 3 footnote: "Outcome investigated: testing positive for SARS-CoV-2"). Symptom onset timing collected at visits; infection timing bounded by 3-visits-per-week swabbing.

## Result

- **Contact load in these households:** median 26 close-range proximity events per day (IQR 10-58); average event duration 0.7 minutes; median daily contact duration 18 minutes (IQR 9-45); maximum single-contact duration 61 minutes (IQR 25-142). Children <5 and 5-12 years had the highest contact duration and frequency; adults 35-59 and teenagers the highest infection risk - "close-range proximity patterns within the household did not fully account for the differences in transmission based on age."
- **Primary null:** on Wilcoxon rank-sum tests, no contact parameter (duration, frequency, cumulative time, average duration - with the index case or with all PCR-positive members) associated with acquisition (all p 0.1-0.8, Table 3). On multivariable mixed-effects logistic regression, no contact parameter was associated (aOR 1.0-1.1 across all seven parameters, Table 4).
- **What did carry risk:** index minimum Ct <30 vs >35: aOR 16.84 (95% CI 3.05-93.06) univariate, ~10.4-11.1 after adjustment; female contact sex aOR 2.51 (1.25-5.02) univariate, ~2.2-2.5 adjusted. Sleeping in the same room as the index: OR 0.94 (0.47-1.88) - null. Variant strata (Alpha, Delta vs Beta) and index age were not significant after adjustment (wide CIs).
- **Acquisition fraction in the analyzed contacts:** 153/252 (60.7%) tested positive during follow-up (Table 4 header: 99 negative / 153 positive).
- **Sensitivity analysis** restricted to households with no member excluded for baseline seropositivity (n=192; 66 negative / 126 positive): same result - no contact pattern significant (Table 5).
- **Direction-of-transmission caveat stated by the authors:** the index-directed analysis "would have missed the period when the index case was most infectious, just before symptom onset," and index misclassification (asymptomatic index) was possible; to address this they also ran the grouped analysis (contacts with all infected members), which "may also have diluted possible associations with the true infector."

## Main limitation (as recorded by the authors)

- Case-ascertained enrollment starts after symptom onset, so sensor deployment (first or second visit) cannot capture the index's pre-onset infectious period; measured contacts may also reflect behavior change after the household learned of infection.
- No data on NPI use (masking), indoor/outdoor contact location, or ventilation.
- Sensors measure face-to-face proximity only: "if individuals were close to each other but not directly facing one another for extended durations, we would not have measured this, although sharing of the same air may have occurred."
- Compliance losses: 73 sensors identified as not worn via accelerometer data; hardware failures, lost and damaged tags; participants without consent for the contact arm.
- Contacts could have been exposed outside the household (quarantine unmonitored); tertiary chains not modeled; multiple same-variant introductions possible (only mixed-variant households excluded; WGS did not resolve within-household directionality).
- Small sample size - "may have reduced our power to detect small differences in close proximity event parameters" - and the sensor substudy sample (88 of 124 enrolled index households) skewed toward Soweto, larger households, and non-smoking households (Table 1).

## Inferential leaps beyond the experiment

- **Route inference from a null:** the abstract and discussion offer that "droplet-mediated transmission during close-proximity contacts plays a smaller role than airborne transmission of SARS-CoV-2 in the household" as one explanation of the null. The study measured no aerosols, no ventilation, and no air sharing - it measured face-to-face proximity. The airborne explanation is an interpretation of a null, not a measurement; the authors' own list ("study limitations... or... high contact rates in households") keeps the alternatives open.
- **"High contact rates above the transmission threshold" hypothesis:** proposed without a threshold measurement.
- **Policy-adjacent suggestion:** that household ventilation "could potentially be a method to reduce secondary transmission" - no ventilation intervention was tested.
- The title's causal phrasing ("household transmission") rests on the within-2-weeks-of-index rule; within-household directionality was not directly observed (the authors' own caveat about unmonitored outside exposure and unobserved multiple introductions is quoted above).

## Which gap and ladder rung this fills

- **GAP 3 (prospective cohort with exposure + infection markers + disease timing in the same people), second SARS-CoV-2 row and the corpus's only instrument-measured-exposure row.** Exposure is not reconstructed or modeled: every <1.5 m face-to-face contact is logged by sensors at 20-second resolution; infection markers are serial rRT-PCR (three swab visits per week regardless of symptoms) plus entry/exit serology; timing comes from the same visit stream. Complements [[sources/kelly-2022-sars-cov-2-household-transmission-cohort]] (near-daily self-swabs, exposure imputed from household membership).
- Its null is itself evidence-grade: measured contact dose did not separate infected from uninfected contacts, while index viral load (Ct) did - a boundary datum for any claim that close face-to-face contact is the necessary and sufficient household exposure metric for SARS-CoV-2.
- Boundary kept sharp: this is an infection endpoint (PCR), not a disease endpoint; no clinical severity outcome is analyzed; and a case-ascertained design cannot measure community or asymptomatic-chain transmission.

## Related

- [[synthesis/viral-disease-causation-evidence-ladder]]
- [[synthesis/sars-cov-2-covid-causation-audit]]
- [[sources/kelly-2022-sars-cov-2-household-transmission-cohort]]
- [[sources/killingley-2022-sars-cov-2-human-challenge-model-validation]]
- [[sources/sauter-2026-phirst-influenza-household-transmission]]
- [[sources/cox-2025-cascadia-rsv-household-transmission]]
