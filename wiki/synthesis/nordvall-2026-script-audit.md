---
title: Nordvall 2026 Analysis Script Audit
category: synthesis
summary: Line-by-line audit of the deposited R script behind Nordvall et al. 2026 (COVID-19 vaccination and childbirth, Sweden), covering interval splitting, fixed-offset index dates, and missing-value handling through the miscarriage filters, tested by running the authors' own lines on synthetic registry data.
tags:
  - analysis-code
  - childbirth
  - code-audit
  - computational-reproducibility
  - cox-regression
  - miscarriage
  - registry-data
  - time-varying-exposure
  - vaccines
sources: 1
updated: 2026-10-16
claim_status: unresolved
claim_type: methodological
---

# Nordvall 2026 Analysis Script Audit

> [!warning] Warning
> This page is research analysis, not medical advice. The registry data behind the paper are restricted and were not available. Every number below that comes from synthetic data describes what the code does to invented records. None of it estimates anything about Jönköping County.

## Scope and method
- **Study:** [[sources/nordvall-2026-covid-vaccination-childbirth-sweden]].
- **Script audited:** `CommMedNordvall2025Rscript.txt`, Zenodo 10.5281/zenodo.18138478 (v1.0, md5 `f6c85aa0f65fe4a69da1f726c0e77f13`). The copy supplied for this audit is byte-identical to the Zenodo file. Line numbers below refer to it.
- **Environment:** R 4.3.3 with survival 3.5.8. The paper used R 4.3.0.
- **Method.** The authors' own lines were executed verbatim, one top-level expression at a time:
  - Part I data preparation, lines 22-129;
  - Part II, lines 321-413.
  - The input was a synthetic registry written to the script's own file paths and column layout.
  - After every expression, the run logged the row count, person count and number of all-NA rows of each working table.
  - The resulting start/stop dataset was compared row by row with an independent `survival::tmerge()` build from the same inputs.
- **Synthetic world.** All parameters are assumptions made for illustration; none is calibrated to the registry:
  - dose-2 uptake about 75%, roll-out mainly May-September 2021;
  - an age-shaped hazard of a conception leading to delivery;
  - half of knowingly pregnant women deferring vaccination until after delivery;
  - true dose-2 HR set to 1.0 or 0.9;
  - gestational age at delivery with mean about 278 days and about 6% preterm.
- **Code and output:**
  - `synthesis/nordvall-2026-script-audit/audit_common.R`: shared helpers (traced execution, interval checks, `tmerge()` rebuild).
  - `synthesis/nordvall-2026-script-audit/synthetic_audit.R`: everything on this page.
  - `synthesis/nordvall-2026-script-audit/registry_audit.R`: the same checks for someone with authorised data access.
  - `synthesis/nordvall-2026-script-audit/results/synthetic_audit_output.txt`: full output of the run reported here.

## Answers in brief
| Check | What the deposited code does | Shown by | Still unknown |
|---|---|---|---|
| Is `survival::tmerge()` used? | No. Exposure intervals are built by hand: rows are duplicated at lines 54-58, then a per-person loop at lines 99-113 overwrites each interval end. `survSplit()` (lines 229, 239, 433) only splits calendar periods, and `tt()` (lines 248-259) only fits a time-varying coefficient. | Reading the code. A verbatim run matched `tmerge()` for every person except five identified edge-case types. | How many real women fall into each edge-case type. |
| Vaccination before entry into the risk set | No interval starts before day 0. A woman whose recorded dose-2 date precedes 2021-01-01 is not excluded: line 61 drops only her exposed row, so she is analysed as unexposed for all follow-up. | Verbatim run: 3 of 3 injected cases were kept as unexposed. | The real count. The paper says vaccination opened to adults in January 2021, so any such date would be a recording error. |
| Raw gestational-age distribution | It cannot be pulled from the script's inputs. The positional column drops imply a delivery extract with three columns and no gestational age. | Code arithmetic. | The real distribution needs Medical Birth Register or obstetric-record data. |
| Does a GA-based offset change the PH output? | On synthetic data the overall adjusted HR barely moved: a mean shift of about 0.1% and at most 2.4% in one world. The first-period HR and the Schoenfeld p-value moved more. | One verbatim run plus 2 × 60 replicate worlds. | The size in the real data, which depends on the registry's GA distribution. |
| Row counts around a "≥22 weeks" miscarriage filter | No line filters on gestational weeks. Line 128 removes every woman with any miscarriage record, of any date. The 22-week step (lines 335-337) prepares an object that line 355 never merges. | Code reading and verbatim trace. | Which miscarriage path produced the published Model 2. |
| NA rows discarding complete cases | The miscarriage filter cannot create or drop rows through NA. Upstream filters turn NA conditions into all-NA "phantom" rows, and women with a missing birth date lose all their rows at line 122. | Verbatim trace with injected NAs. | Real NA counts. `registry_audit.R` reports them. |

## 1. Interval splitting

### How the exposure intervals are built
1. **Lines 54-58.** Every woman gets an unexposed row starting 2021-01-01. Each woman with a dose-2 record also gets an exposed row starting on her dose-2 date.
2. **Lines 77-78.** Rows whose index date falls before the row's start date are dropped. An index date before dose 2 therefore stays on the unexposed row.
3. **Lines 99-113.** A loop over `PatientID` copies the next row's start age into each non-final row's end age, and line 114 forces `status = 0` on those rows.
4. **Line 122.** Rows with a length of zero or less are removed.

### Comparison with `tmerge()`
The verbatim run used 20,000 eligible synthetic women and true HR = 1.
- **Agreement.** 33,316 of 33,329 script rows were identical to the `tmerge()` rows.
- **Differences.** 13 women differed. Every difference has a computed cause, and none is unexplained.
- **After removing those 13 women,** the age-adjusted HR is identical in both datasets: 1.0202 (0.8962-1.1614), 1,325 events.

The causes, in the script's behaviour:

1. **Dose 2 recorded before entry.** Line 61 is commented "Remove exposed before 2021-01-01", but it removes only the exposed row. The woman stays in the cohort as unexposed for all follow-up, whereas `tmerge()` would treat her as exposed from day 0.
   - **Effect on the risk-set entry check:** no interval starts before day 0, but such a woman is misclassified rather than excluded.
   - **Likely real count:** the paper says vaccination was made available to residents aged 18 and over from January 2021, so any such date would be a recording error. Table S1 covers 2021-2024 only and cannot show it, so only the registry can give the count.
2. **Index date on the dose-2 day.** The exposed row has zero length and is dropped at line 122. The unexposed row was already forced to `status = 0` by the loop, so the event disappears entirely. `tmerge()` keeps it as an unexposed event.
   - **Synthetic frequency:** besides the injected cases, two such ties arose naturally among about 1,325 events.
3. **Dose 2 after the end of follow-up, or after death.** The loop extends the unexposed row to the dose-2 date before line 122 drops the zero- or negative-length exposed row. The unexposed person-time then runs past 2023-09-30, or past death.
   - **Likely real count:** Table S1 lists 16 women with dose 2 between October 2023 and December 2024.
   - **Effect:** on a calendar-time scale with no events after day 1002, this extra person-time cannot move the Cox estimate. It does inflate any person-time totals.
4. **A duplicated record in any merged file (more than two rows per woman).** Line 106 re-sorts `test` in descending date order, but the loop writes start ages taken from the ascending-ordered copy. The result is a duplicated unexposed interval, so the woman sits twice in every risk set up to her dose 2.
   - Example: the injected duplicate death record produced (0,163], (0,163], (163,422] instead of (0,163], (163,422].
   - **Real data:** whether any input file has duplicate personal numbers is unknown; `registry_audit.R` counts them.
5. **Index date exactly 2021-01-01.** The woman is removed entirely, together with her event, because her only interval has zero length. `tmerge()` does the same, since an event at time 0 cannot sit in a (start, stop] interval, but nothing documents it.
   - **Likely real count:** with the 280-day offset this is every woman who delivered on 8 October 2021, the first day of the paper's stated delivery window. With the 266-day offset it is everyone who delivered on 24 September 2021.

Line 90 is commented as removing "faulty dose 3 dates that are registered prior to dose 2". In practice it removes the exposed row and censors the unexposed row at the faulty dose-3 date, which is equivalent to `tmerge()` with censoring at dose 3.

### Survival-curve and immortal-time checks
- **The "ever exposed" Kaplan-Meier summary (lines 162-189).** It classifies each woman by `max(exposure)`. Women who conceived before their dose 2 lose their exposed row at line 78 and count as never exposed, while vaccinated women's event-free pre-vaccination time is credited to the exposed group.
  - **Synthetic size:** with true HR = 1, a Cox model on that person-level summary gives HR 0.35.
  - This is classic immortal-time bias. The figure-labelled survival curves in the paper do not appear to come from this block, because its labels are in Swedish ("Ej exponerad", "Tid").
- **Figure S2.1** ("adjusted by age", "exposure=0/1", time in days, y-axis 0.85-1) matches lines 197-226. Those curves are `survfit()` predictions from the fitted Cox model at fixed exposure values.
  - Predictions from a proportional-hazards model are proportional by construction, so inspecting them cannot reveal a violation of proportional hazards. The paper cites them for exactly that purpose.
  - The block itself does not run as deposited: line 198 needs `F32_33`, which is not in the cohort layout, and line 204 uses `combA`, which is never defined.

## 2. Index-date arithmetic

### What the code does
- **Two offset lines.** Line 38 (`Kontaktdatum - 280`) and line 39 (`Kontaktdatum - 266`) both assign `Befruktningsdatum`. Run top to bottom, line 39 wins, so the 266-day sensitivity analysis is what a straight run produces. The paper's primary analysis uses 280 days, which matches the E-value line 152.
- **The index replaces the delivery date.** Line 40 drops column 3 (the delivery date) and line 41 renames the index to `Kontaktdatum`.
- **The offset also decides cohort membership.** Lines 44-46 exclude women whose index date falls before 2021-01-01 as "pregnant at study start". This fits the different Ns in Table S4 (56,787 at 280 days, 56,935 at 266 days).
- **Labelling.** 280 days is the conventional span from last menstrual period (LMP) to delivery, and conception is usually about 14 days after the LMP. The paper calls the 280-day index an "estimated conception date", but the date is closer to an LMP date. Its 266-day sensitivity analysis is the conception-based version.

### Gestational age is not in the analysis inputs
The positional indices at lines 40, 64, 79, 95 and 259 are jointly consistent with one input layout:
- a 5-column cohort file;
- a 2-column death file;
- a 3-column delivery file holding the personal number, a second column dropped at line 64, and the delivery date.

In that layout no gestational-age field reaches the analysis, so the raw gestational-age distribution cannot be pulled from the script's inputs. This is inferred from the code; the files themselves were not seen. Adding a gestational-age column to the delivery file without editing those positional drops would shift them and remove the wrong columns.

### What a GA-based offset does on synthetic data
The synthetic gestational-age distribution is an assumption and was never observed:
- mean 278.4 days, with 6.3% of deliveries before 259 days;
- the fixed 280-day offset minus the LMP-based offset averages 1.6 days (SD 14.5 days);
- the error exceeds 28 days for 5.0% of deliveries, almost all of them preterm births.

**One verbatim world.** Lines 22-125 were run four times on the same 20,000 synthetic women (true HR = 1), changing only the index date, which was injected right after line 39.

| Index date | Age-adjusted HR (95% CI) | Events | Excluded as pregnant at start | Schoenfeld p (exposure) | HR days 0-212 / 213-365 / 366-end |
|---|---|---|---|---|---|
| Fixed 280 days (paper primary) | 1.022 (0.898-1.163) | 1,325 | 716 | 0.013 | 1.02 / 0.89 / 1.08 |
| Delivery minus recorded GA (LMP-based) | 1.056 (0.928-1.201) | 1,345 | 706 | 0.031 | 1.08 / 0.92 / 1.11 |
| Fixed 266 days (paper sensitivity) | 1.049 (0.921-1.194) | 1,328 | 685 | 0.021 | 0.99 / 0.96 / 1.09 |
| Delivery minus (GA - 14) (conception-based) | 1.042 (0.916-1.186) | 1,353 | 667 | 0.006 | 0.82 / 0.96 / 1.11 |

**Event-level reclassification.**
- 280 days vs the LMP-based index: 12 of 1,314 shared events changed exposure class, and 42 events appeared under only one definition. Those 42 come mainly from women moving in or out of the "pregnant at start" exclusion and in or out of follow-up.
- 266 days vs the conception-based index: 11 of 1,319 shared events changed class, and 43 appeared under only one definition.

**Replicate simulation.** 60 synthetic worlds of 60,000 women per true HR, interval data built with `tmerge()` (validated against the verbatim build above).

| True HR | Fixed 280 | LMP-based | Fixed 266 | Conception-based |
|---|---|---|---|---|
| 1.0 (mean adjusted HR, SD) | 0.9996 (0.037) | 1.0009 (0.036) | 1.0008 (0.038) | 1.0007 (0.039) |
| 0.9 (mean adjusted HR, SD) | 0.9043 (0.034) | 0.9031 (0.034) | 0.9017 (0.032) | 0.9005 (0.032) |

Within the same world, the fixed offset minus the GA-based offset changed the adjusted log-HR by:
- true HR 1.0: on average -0.0014 (280 vs LMP-based) and +0.0002 (266 vs conception-based);
- true HR 0.9: on average +0.0013 for both comparisons;
- in the worst single world, by at most 0.024.

**Interpretation, limited to these synthetic assumptions.**
- On the overall HR, the fixed offsets were essentially unbiased against GA-based offsets: about 0.1% on average and at most about 2.4% in one world. That is smaller than the between-world sampling SD of about 3.5%.
- The early-period HR and the Schoenfeld p-value moved more, because the first calendar period has few exposed events. The synthetic world also has unobserved heterogeneity in fertility, so its Schoenfeld p-values say nothing about the paper.
- A real distribution with a heavier preterm tail, or vaccination clustered near conception, could change the size of the effect. **We do not know the size in the registry.** `registry_audit.R` runs this exact comparison given a gestational-age file.

## 3. Missingness and the miscarriage filters

### The "≥22 weeks" filter is not in the code
No line filters on a recorded gestational week. The 22-week idea appears in three places that do not line up:

| Where | What it does |
|---|---|
| Paper, Methods (miscarriage analysis) | Women "recorded as being ≥22+0 weeks pregnant on 1 January 2021 were excluded". |
| Part II lines 335-337 | `FörstaMissfall21_` dates are shifted by `n <- -154` days (22 weeks), commented "Remove miscarriages within 22 weeks after study start". Combined with the before-start filter at lines 368-369, this would remove women whose first 2021+ miscarriage fell before 2021-06-04. It would also move every miscarriage index date 154 days earlier. |
| Part II line 355 | Merges `Missfall`, not the shifted `FörstaMissfall21_`. In a fresh R session Part II stops here with "object 'Missfall' not found". In the same session as Part I it uses `Missfall.csv` unshifted, so lines 335-337 have no effect on the analysis. |
| Part I line 128 ("Remove miscarriages (extra analysis)") | `comb[!(comb$Personnr %in% Missfall$Personnr),]` removes every woman with any record in `Missfall.csv`, whatever its date or gestational week. |

The paper's rule (exclude women ≥22 weeks pregnant at baseline) and the shift-based rule (exclude women who miscarried in the first 22 weeks of follow-up) select different women. The deposited Part II applies neither, because line 355 does not use the shifted object.

### Row counts with injected missing values
Synthetic run: 20,000 eligible women plus 1,600 ineligible people. Injected missing values: 5 ages, 5 birth dates, 2 sexes, 1 `PatientID`, 3 delivery dates, 2 dose-2 dates, 2 `Missfall` personal numbers and 2 `Missfall` dates.

| Line | Step | Rows | Persons | All-NA rows |
|---|---|---|---|---|
| 25 | read cohort | 21,600 | 21,600 | 0 |
| 32 | age 18-45 | 20,000 | 19,995 | 5 |
| 33 | women only | 20,000 | 19,993 | 7 |
| 44-45 | `grav`: index before 2021-01-01 | 673 | 672 | 1 |
| 46 | remove pregnant at start | 19,328 | 19,328 | 0 |
| 80 | remove missing `PatientID` | 33,496 | 19,327 | 0 |
| 122 | remove intervals of length ≤ 0 | 33,491 | 19,319 | 9 |
| 128 | miscarriage filter | 32,059 | 18,498 | 0 |

What the trace shows:
- **Lines 32-33 keep missing values as junk rows.** A missing age or sex does not drop the row: R's `[` with an NA condition inserts an all-NA "phantom" row in its place.
- **Line 46 removes those phantom rows by coincidence.** The missing delivery dates also produced a phantom row in `grav`, and `NA %in% c(..., NA)` is `TRUE`. With complete delivery dates, the phantom rows would have survived to line 80.
- **Line 80** silently drops the woman with a missing `PatientID`.
- **Line 122 loses complete cases.** Eight women disappear here:
  - Five had only a missing birth date; their age and every event date were present. The script derives interval lengths from age in days, so their rows became 9 all-NA rows.
  - Three had a 280-day index date exactly on 2021-01-01, so their events vanished with them. In the real data this is everyone who delivered on 8 October 2021, the first day of the paper's stated delivery window. Table S2 implies roughly 11 deliveries a day in 2021.
- **Line 128 removes 821 real women (1,423 rows) plus the 9 phantom rows.** The phantom rows go only because `Missfall` also holds a missing personal number. Of the 821 women:
  - 615 had only pre-2021 miscarriage records;
  - 2 had only undated records;
  - 61 carried a childbirth event, which was deleted with them, so events fell from 1,351 to 1,290.
- **Kept but misclassified, never reported:**
  - 2 women with a dose-2 record but no dose-2 date stay in as unvaccinated;
  - 3 women with a delivery record but no delivery date stay in as event-free.

**Answer to the NA question.** The miscarriage filter neither creates nor drops rows through NA, because `%in%` never returns NA. Complete cases are lost upstream, at line 122, when only the birth date is missing. Records with a missing event date are kept as non-events rather than flagged. Before/after counts at line 128 mix three things: women removed by design, phantom rows removed by an NA-matches-NA coincidence, and events deleted along with the women.

**Part II, run after Part I in the same session** (same synthetic world):

| Variant | Persons | Events |
|---|---|---|
| As deposited: line 355 merges `Missfall` (all records, unshifted) | 19,358 | 148 |
| Line 355 replaced by the -154-day shifted `FörstaMissfall21_` | 19,953 | 127 |

- **As deposited, women with any pre-2021 miscarriage record leave the miscarriage cohort.** The before-start filter at lines 368-369 removes both of their rows.
- **Women with more than one record get extra rows.** Seven synthetic women had more than one `Missfall` record, and the merge at line 355 multiplies their rows.
- **Under the shift, vaccination during the pregnancy counts as unexposed.** An event dated miscarriage − 154 days counts as exposed only if dose 2 came at least 154 days before the miscarriage, in practice before conception. Of 75 synthetic miscarriages that followed the woman's dose 2, 20 were classified as unexposed. This contradicts the authors' description of the miscarriage model as addressing vaccine effects in pregnant women, if the shifted path was the one used.

### What the published Ns can and cannot settle
- **Model 1.** The analysed N is 56,787, which is 2,986 below the cohort of 59,773. That is of the same order as the 2021 births that fall before 8 October (Table S2: 4,038 births in 2021, about 3,100 pro rata). This fits the pregnant-at-start exclusion at lines 44-46.
  - It does not fit line 128 also having been applied, if `Missfall.csv` spans 2016-2024 like Table S3 (2,173 recorded miscarriages in 2016-2020). In that case line 128 would remove well over a thousand further women.
  - That inference depends on the file's date range, which is not visible.
- **Model 2.** N is 59,661, so 112 women were excluded. That count is compatible with more than one code path and cannot be resolved without the data.

## 4. Other reproducibility findings
- **The deposit cannot be `source()`d.** It is a text document with a prose header, and lines 136 and 140 use curly quotes, which R does not parse.
- **Two naming states are mixed.** Line 132 renames `ÅlderStartdatum` to `age`, yet lines 158, 166, 198-200, 240-243, 250 and 258 still use `ÅlderStartdatum` on the renamed data (line 416 and lines 434-437 repeat this in Part II). No single top-to-bottom order runs every model line.
- **Undefined objects.** `combA` (line 204) is never defined, and `F32_33` (line 198) is not in the cohort layout that the positional indices imply.
- **Line 257** calls `ns(..., Boundary.knots = FALSE)`, which errors in R.
- **Spline boundaries.** The knots run to day 1074, but follow-up ends at day 1002 (2023-09-30).
- **Table S5 is not in the deposit.** The paper's Table S5 ("adjusted algorithm", one-dose exposure, no dose-3 censoring) has no corresponding code: no dose-1 file is read.
- **Positional column indexing** at lines 40, 64, 79, 95 and 259 makes the pipeline silently layout-dependent.

## What this wiki currently concludes
- **Established by running the authors' code** on synthetic inputs:
  - The interval construction matches `tmerge()` for ordinary records.
  - It mishandles five identifiable edge cases:
    - a dose-2 date before entry;
    - an index date on the dose-2 day;
    - dose 2 after the end of follow-up or after death;
    - duplicated input records;
    - an index date on day 0.
  - In synthetic worlds, replacing the fixed 280/266-day offset with a delivery-specific gestational age changed the overall adjusted HR by about 0.1% on average.
  - No "≥22 weeks" filter on recorded gestational weeks exists.
  - The Part II code does not use the 22-week-shifted object it prepares.
  - NA-driven phantom rows arise upstream of the miscarriage filter, not at it.
- **Not established:** whether any of this changes the published estimates. That needs the registry, and `registry_audit.R` is written to answer it. Until then, the vault keeps the paper's conclusion `unresolved`. We do not know whether the published HRs would survive these corrections.

## How to rerun
```bash
# synthetic audit (downloads the script from Zenodo when no path is given)
LC_ALL=C.UTF-8 Rscript wiki/synthesis/nordvall-2026-script-audit/synthetic_audit.R [CommMedNordvall2025Rscript.txt]
# registry audit, for authorised data holders
LC_ALL=C.UTF-8 Rscript wiki/synthesis/nordvall-2026-script-audit/registry_audit.R CommMedNordvall2025Rscript.txt [ga_file.csv] [out_dir]
```
Environment variables `N_VERBATIM`, `N_SIM` and `REPS` size the synthetic run. The values used here were 20,000, 60,000 and 60.

## Connections
- Source: [[sources/nordvall-2026-covid-vaccination-childbirth-sweden]]
- [[concepts/replication-crisis]]: analysis code that is deposited but does not regenerate the published results.
- [[concepts/clinical-endpoints]] and [[concepts/surrogate-endpoints]]: an endpoint whose date is computed rather than observed.
- [[concepts/inferential-leap]]: from one age-adjusted model to policy support.
