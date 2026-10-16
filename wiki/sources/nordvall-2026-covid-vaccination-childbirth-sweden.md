---
title: "COVID-19 Vaccination Carries No Association with Childbirth Rates in Sweden (Nordvall 2026)"
category: source
summary: Region Jönköping registry cohort (59,773 women aged 18-45) analysing dose-2 COVID-19 vaccination as a time-varying exposure against an estimated conception date (delivery minus 280 days) and against recorded miscarriages; the deposited R code is audited in this vault.
tags:
  - analysis-code
  - childbirth
  - cox-regression
  - fertility
  - miscarriage
  - mrna-vaccines
  - observational-cohort
  - registry-data
  - sweden
  - time-varying-exposure
  - vaccines
sources: 1
updated: 2026-10-16
claim_status: unresolved
claim_type: empirical
source_tier: tier-1
source_path: none (full text via Europe PMC PMC13310814; code via Zenodo 10.5281/zenodo.18138478)
source_date: 2026-01-21
authors:
  - dennis nordvall
  - thomas schön
  - jorma hinkula
  - olle eriksson
  - armin spreco
  - örjan dahlström
  - johan lyth
  - daniel axelsson
  - elin gursky
  - marie blomberg
  - toomas timpka
ingested: 2026-10-16
evidence_role: Single-cohort observational test of dose-2 COVID-19 vaccination against childbirth and recorded miscarriage; anchor for the vault's code-level reproducibility audit.
pmid: 41565977
pmcid: PMC13310814
doi: 10.1038/s43856-026-01396-x
---

# COVID-19 Vaccination Carries No Association with Childbirth Rates in Sweden (Nordvall 2026)

## Source type
- Role in this vault: a primary observational cohort with deposited analysis code, audited line by line in [[synthesis/nordvall-2026-script-audit]].
- Journal/year: *Communications Medicine*, published online 21 January 2026.
- Authors: Nordvall D, Schön T, Hinkula J, Eriksson O, Spreco A, Dahlström Ö, Lyth J, Axelsson D, Gursky E, Blomberg M, Timpka T.
- Source basis in hand:
  - full text (Europe PMC JATS XML);
  - Supplementary Materials (Tables S1-S5, Figures S1-S4) and the transparent peer-review file;
  - the deposited R script `CommMedNordvall2025Rscript.txt` (Zenodo record 18138478, GitHub `Tooti02/VaccEval` v1.0, 2026-01-03). The copy supplied to this vault is byte-identical to the Zenodo file (md5 `f6c85aa0f65fe4a69da1f726c0e77f13`).
- Not in hand: the registry data. The paper's data statement says they are held by the health-service providers under a restricted-access agreement.

> [!warning] Warning
> This page is for research analysis only. It is not medical advice.

## Evidence fields
| Field | Extraction |
|---|---|
| Study type | Retrospective registry cohort. Cox proportional-hazards models on a calendar-time scale (days since 2021-01-01), with dose-2 vaccination as a time-varying covariate. The paper describes this as emulating an experiment in which vaccine was randomly distributed on 1 January 2021. |
| Subject / sample | All women aged 18-45 on 1 January 2021 resident in Jönköping County, Sweden (N = 59,773). Analysed N: 56,787 (280-day model), 56,935 (266-day model) and 59,661 (miscarriage model), per Table S4. |
| Intervention or exposure | Second dose of a COVID-19 vaccine (97% of doses mRNA), counted from the dose-2 date. Dose 3, death and 2023-09-30 censor follow-up. |
| Comparator / control | Person-time before dose 2 and person-time of women never given dose 2. Women with one dose only count as unexposed (791 women). |
| Endpoint | (1) An index date set 280 days before a recorded childbirth (ICD-10 O80-O84; childbirths recorded 2021-10-08 to 2024-07-06), with 266 days as a sensitivity analysis. (2) Recorded miscarriage (ICD-10 O03), analysed separately. |
| Result | Table S4. Childbirth, 280 days: unadjusted HR 0.94 (0.89-1.00); age-adjusted 1.03 (0.97-1.09). 266 days: 0.96 (0.90-1.02); 1.04 (0.98-1.11). Recorded miscarriage: 0.84 (0.69-1.03); 0.86 (0.70-1.05). |
| Main limitation | Observational design adjusted for age only, entered as one linear term; comorbidity was deliberately left unadjusted. The index date is a fixed offset from delivery, not a recorded conception or gestational age. Pregnancies not ending in a recorded delivery are invisible to the childbirth endpoint, and induced abortions were unavailable. The deposited code does not regenerate the published analyses as written (see [[synthesis/nordvall-2026-script-audit]]). |

## Reported results in more detail
- Calendar-period HRs (Table S4; periods split at day 212 and day 365).
  - 280-day model: 0.99 (0.71-1.40), 0.95 (0.86-1.05), 1.11 (0.97-1.28).
  - 266-day model: 0.91 (0.75-1.10), 0.98 (0.88-1.09), 1.11 (1.02-1.20).
  - Miscarriage model: 1.23 (0.69-2.22), 0.82 (0.54-1.27), 0.82 (0.65-1.05).
- One-dose exposure (main text, 280 days):
  - Childbirth: unadjusted 0.93 (0.88-0.99), adjusted 1.02 (0.96-1.09). The paper calls the unadjusted estimate "statistically insignificant", but its interval excludes 1.
  - Miscarriage: 0.84 (0.70-1.00) unadjusted, 0.90 (0.74-1.09) adjusted.
- Table S5 reports an "adjusted algorithm", described as adjusting "for exclusion of pre-dose 2 events in the time-split dataset". Under it:
  - childbirth 1.00 (0.94-1.06) at 280 days and 1.01 (0.95-1.07) at 266 days;
  - recorded miscarriage 0.80 (0.66-0.97).
  - Without censoring at dose 3, miscarriage is 0.73 (0.61-0.87), and 0.82 (0.68-0.98) when one-dose women are included.
  - These sensitivity intervals exclude 1 in the direction of fewer recorded miscarriages among vaccinated women. The abstract reports only the primary miscarriage estimate.
- Counts reported in the paper:
  - 45,165 women (75.5%) received two doses.
  - 5,955 women (10%) gave birth before any booster.
  - 542 women had a recorded miscarriage during the vaccination period.

## What the source claims
- The authors conclude that COVID-19 vaccination "is not associated with a decrease in childbirth after adjusting for common confounding factors".
- The authors state that the findings "provide evidence to support vaccination policies for women of childbearing age".
- The authors argue that socio-economic conditions and a shrinking cohort of potential parents (lower Swedish birth rates around 1992-1998) are "the most plausible explanations" for the 2021-2024 birth decline.
- The authors say the miscarriage analysis addresses vaccine effects on pregnant women, under the stated assumption that vaccine effects on documented and undocumented pregnancy losses are similar.

## What the experiment can answer
- **The childbirth question it can answer.** Among women aged 18-45 in one Swedish county, not identified as pregnant at study start, did the hazard of a delivery-derived index date (delivery minus 280 days) differ between person-time after dose 2 and other person-time, given a linear term for baseline age? The reported age-adjusted answer is HR 1.03, with an interval of 0.97-1.09.
- **The miscarriage question it can answer.** It can say the same for recorded miscarriages (ICD-10 O03) in the health information system, a count that the authors note misses early losses for which no care was sought.

## What it cannot answer
- **Fertility as a whole.** Conceptions ending in miscarriage, induced abortion (data unavailable) or unrecognised loss never produce the childbirth endpoint.
- **Vaccination during pregnancy.** On the 280-day index, any vaccination after the estimated index date is unexposed time. A pregnancy lost after vaccination removes an unexposed event rather than adding an exposed one. Reviewer 1 raised this conflation, and the authors kept the combined design.
- **Causal effect.** Moving from unadjusted 0.94 to age-adjusted 1.03 shows that a single linear age term changes the estimate by more than the width of its interval. Pregnancy intention, health-care seeking and comorbidity are not measured or not adjusted. The E-values in the script (1.20-1.31) quantify sensitivity to an unmeasured confounder, not its absence.
- **Long-term effects on fertility.** The authors acknowledge this.
- **Causes of the population-level birth decline.** No experiment or model in the paper tests the socio-economic explanation the discussion offers.

## Later inferential-leap risk
The leap starts from a confidence interval spanning 1, in one county, under one age-only Cox specification. It goes to a general statement that vaccination "is not associated with a decrease in childbirth" and to support for vaccination policy. The paper's own sensitivity tables contain estimates whose intervals exclude 1:
- the childbirth unadjusted one-dose estimate;
- the 266-day late-period estimate;
- several miscarriage estimates.

The abstract does not carry these. See [[concepts/inferential-leap]].

## Vault conclusion
- The paper reports no statistically significant association between dose-2 vaccination and its delivery-derived index event in the primary age-adjusted model. That is a narrow observational result, and the vault records it as reported.
- **The vault does not treat the conclusion as supported.**
  1. The deposited code cannot be run as deposited:
     - two lines with curly quotes fail to parse;
     - line 39 (266 days) overwrites line 38 (280 days);
     - the miscarriage section merges an object other than the one it prepares;
     - objects such as `combA` and `F32_33` are never defined.
  2. The paper says women "recorded as being ≥22+0 weeks pregnant on 1 January 2021" were excluded from the miscarriage analysis. Neither code path in the deposit applies that rule:
     - the step that is merged applies no such rule;
     - the step that is prepared but never merged would remove women whose first 2021 miscarriage fell before 4 June 2021.
  3. No independent replication is in the vault.
- On whether COVID-19 vaccination changed childbirth or miscarriage hazards in this population, the vault's answer is: **we do not know** beyond this single age-adjusted model. Details are in [[synthesis/nordvall-2026-script-audit]].

## Connections
- Code audit: [[synthesis/nordvall-2026-script-audit]].
- Endpoint construction: [[concepts/clinical-endpoints]], [[concepts/surrogate-endpoints]].
- Reproducibility: [[concepts/replication-crisis]].
- Conclusion scope: [[concepts/inferential-leap]].
- Vaccine outcome pages: [[synthesis/specific-vaccine-overall-health-outcome-evidence]].
