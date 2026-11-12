---
title: Methodological rigor — vaccinology vs chemistry (2015–2024 random sample)
category: comparison
summary: PubMed random-sample audit (n=12+12) scoring eight methodological dimensions; no significant total-score difference.
tags: [methodological-audit, vaccinology, chemistry, evidence-standards, replication]
claim_status: exploratory
claim_type: methodological
source_tier: tier-1
updated: 2026-11-11
---

# Methodological rigor comparison: vaccinology vs chemistry

> [!note] Note
> All 24 papers were drawn fresh from PubMed and **none** appear in the existing `wiki/sources/` corpus (vault PMID exclusion).

## Sampling protocol

- **Database:** PubMed (NCBI E-utilities: esearch, efetch, elink)
- **Date window:** 2015-01-01 to 2024-12-31
- **Vault exclusion:** 205 PMIDs already in `wiki/sources/` were skipped on redraw.
- **Randomisation:** Uniform random indices in [0, total_hits-1] using Python random.Random(seed); each index retrieved via esearch retstart=index, retmax=1 (PubMed default relevance order); vault PMIDs excluded and resampling continues until 12 unique papers.

### Vaccinology search
- **Total hits:** 158444
- **Seed:** `20251111`
- **Drawn PubMed positions:** `[5636, 2133, 5001, 2231, 1786, 3240, 4269, 1963, 7612, 8562, 5185, 912]`
- **PMIDs:** `['39307693', '39618822', '39353267', '39609339', '39651187', '39511601', '39422816', '39635534', '39137738', '39055951', '39340096', '39738923']`
```text
(vaccines[MeSH] OR vaccine[tiab] OR vaccination[tiab] OR immunization[tiab]) AND ("2015/01/01"[PDAT] : "2024/12/31"[PDAT]) AND (Journal Article[pt] OR Clinical Trial[pt] OR Randomized Controlled Trial[pt]) NOT (Review[pt] OR "Systematic Review"[pt] OR Meta-Analysis[pt] OR Editorial[pt] OR Comment[pt] OR "Case Reports"[pt] OR "Clinical Trial Protocol"[pt] OR News[pt])
```

### Chemistry search
- **Total hits:** 188247
- **Seed:** `20251112`
- **Drawn PubMed positions:** `[2384, 237, 7314, 2476, 7786, 3427, 7803, 1780, 5679, 634, 3611, 3416]`
- **PMIDs:** `['39576942', '39795461', '39196453', '39570149', '39162869', '39497153', '39160593', '39622773', '39327745', '39722526', '39485867', '39497763']`
```text
(chemistry[MeSH] OR "chemical synthesis"[tiab] OR catalysis[tiab] OR "organic synthesis"[tiab] OR "reaction kinetics"[tiab]) AND ("2015/01/01"[PDAT] : "2024/12/31"[PDAT]) AND (Journal Article[pt]) NOT (Review[pt] OR "Systematic Review"[pt] OR Meta-Analysis[pt] OR Editorial[pt] OR Comment[pt] OR "Case Reports"[pt] OR News[pt])
```

## Aggregate statistics

**Vaccinology totals (/80):** mean 29.54, SD 8.71, median 28.0, range 19.0–47.0
**Chemistry totals (/80):** mean 29.25, SD 8.94, median 24.5, range 21.0–45.0
**Mann–Whitney U (totals):** U=74.5, p=0.907470, rank-biserial r=-0.035

| Dimension | Vacc mean (SD) | Chem mean (SD) | U test p | r |
|---|---:|---:|---:|---:|
| Pre-specification | 2.62 (1.71) | 2.12 (1.13) | 0.407209 | -0.167 |
| Randomisation | 4.50 (1.95) | 4.42 (1.68) | 0.901107 | 0.035 |
| Blinding | 3.88 (1.45) | 4.92 (0.97) | 0.427586 | 0.167 |
| Comparator adequacy | 4.25 (2.26) | 3.00 (0.00) | 0.078018 | -0.250 |
| Outcome selection | 5.17 (1.76) | 6.12 (1.58) | 0.142467 | 0.312 |
| Power | 3.08 (1.43) | 2.29 (1.01) | 0.093986 | -0.312 |
| Reporting completeness | 3.04 (1.50) | 3.21 (1.92) | 0.948477 | 0.021 |
| Independence and replicability | 3.00 (2.56) | 3.17 (3.35) | 1.000000 | -0.007 |

## Charts

- Pre-specification: `/opt/cursor/artifacts/dimension_pre_specification.png`
- Randomisation: `/opt/cursor/artifacts/dimension_randomisation.png`
- Blinding: `/opt/cursor/artifacts/dimension_blinding.png`
- Comparator adequacy: `/opt/cursor/artifacts/dimension_comparator_adequacy.png`
- Outcome selection: `/opt/cursor/artifacts/dimension_outcome_selection.png`
- Power: `/opt/cursor/artifacts/dimension_power.png`
- Reporting completeness: `/opt/cursor/artifacts/dimension_reporting_completeness.png`
- Independence and replicability: `/opt/cursor/artifacts/dimension_independence_replicability.png`
- Totals: `/opt/cursor/artifacts/dimension_total.png`

## Flagged papers

**Missing registered protocol** (`pre_specification` < 5.5) or **undisclosed funding** (`independence_replicability` ≤ 2.0):
- PMID 39307693 (vaccinology): no registered protocol, undisclosed funding
- PMID 39618822 (vaccinology): no registered protocol
- PMID 39353267 (vaccinology): no registered protocol, undisclosed funding
- PMID 39609339 (vaccinology): no registered protocol
- PMID 39651187 (vaccinology): no registered protocol, undisclosed funding
- PMID 39511601 (vaccinology): no registered protocol, undisclosed funding
- PMID 39422816 (vaccinology): no registered protocol, undisclosed funding
- PMID 39635534 (vaccinology): no registered protocol
- PMID 39137738 (vaccinology): no registered protocol, undisclosed funding
- PMID 39055951 (vaccinology): no registered protocol, undisclosed funding
- PMID 39738923 (vaccinology): no registered protocol
- PMID 39576942 (chemistry): no registered protocol, undisclosed funding
- PMID 39795461 (chemistry): no registered protocol
- PMID 39196453 (chemistry): no registered protocol, undisclosed funding
- PMID 39570149 (chemistry): no registered protocol, undisclosed funding
- PMID 39162869 (chemistry): no registered protocol, undisclosed funding
- PMID 39497153 (chemistry): no registered protocol, undisclosed funding
- PMID 39160593 (chemistry): no registered protocol
- PMID 39622773 (chemistry): no registered protocol
- PMID 39327745 (chemistry): no registered protocol, undisclosed funding
- PMID 39722526 (chemistry): no registered protocol, undisclosed funding
- PMID 39485867 (chemistry): no registered protocol, undisclosed funding
- PMID 39497763 (chemistry): no registered protocol

## Paper-level scores

### PMID 39307693 (vaccinology) — total **24.0/80**
Li YH, Wang WW, Wu LP, Du MC, Kou JY, Peng SH, et al.. [Current status of parental decision-making of childhood 13-valent pneumococcal conjugate vaccine immunization and related factors in China].. *Zhonghua liu xing bing xue za zhi = Zhonghua liuxingbingxue zazhi* 2024. DOI: 10.3760/cma.j.cn112338-20240104-00003.
- Design: Primary research (design not fully classified from metadata)
- Sample size (indexed text): n=Not stated in abstract/full-text excerpt searched
- Full-text indexed: 0 characters (PMC when available else abstract)

- **Pre-specification — 1.5/10:** No registry, preregistration, or explicit prespecification appears in the indexed text.
- **Randomisation — 6.0/10:** Observational design: treatment randomisation is not applicable; score is anchored to field-appropriate conduct. "munization in china. methods: cross-sectional multistage survey sampling method was used to select study subjects. the s"
- **Blinding — 5.0/10:** Blinding is typically not applicable to observational surveys; neutral anchor applied.
- **Comparator adequacy — 3.0/10:** Comparator arms or negative controls are weak or not named.
- **Outcome selection — 3.5/10:** Multiple endpoints appear without a clear primary/secondary hierarchy.
- **Power — 2.0/10:** No power or sample-size justification appears in the available text.
- **Reporting completeness — 2.0/10:** Sparse quantitative reporting: limited CIs, dispersion, and missing-data handling in the indexed text.
- **Independence and replicability — 1.0/10:** Funding source is not disclosed in the indexed text (flagged).

### PMID 39618822 (vaccinology) — total **25.5/80**
D'haese S, den Roover S, Verbeke R, Aernout I, Meulewater S, Cosyns J, et al.. The role of mRNA-galsomes and LNPs in enhancing HIV-specific T cell responses across various lymphoid organs.. *Molecular therapy. Nucleic acids* 2024. DOI: 10.1016/j.omtn.2024.102372.
- Design: Clinical or immunogenicity trial
- Sample size (indexed text): n=6
- Full-text indexed: 46499 characters (PMC when available else abstract)

- **Pre-specification — 1.5/10:** No registry, preregistration, or explicit prespecification appears in the indexed text.
- **Randomisation — 2.0/10:** No random allocation language is present in the available text.
- **Blinding — 1.5/10:** No blinding procedures are reported.
- **Comparator adequacy — 8.0/10:** Named placebo, vehicle, or negative control arm. "fter immunization with either vehicle (pbs), lnps or galsomes (gal) containing 2 μg ψ/mc-modified mrna encoding li80tova"
- **Outcome selection — 3.5/10:** Multiple endpoints appear without a clear primary/secondary hierarchy.
- **Power — 2.0/10:** No power or sample-size justification appears in the available text.
- **Reporting completeness — 2.0/10:** Sparse quantitative reporting: limited CIs, dispersion, and missing-data handling in the indexed text.
- **Independence and replicability — 5.0/10:** Funding is disclosed but competing-interest or sharing statements are thin. ".l. would like to acknowledge funding from (grant no. ) and the fwo-v with grant no. . furthermore, we would like to th"

### PMID 39353267 (vaccinology) — total **19.0/80**
Teufel LU, Taks EJM, van Gemert J, Neacsu M, Föhse K, Gillard J, et al.. Interleukin 38 reduces antigen-presentation capacity and antibody production after vaccination.. *Vaccine* 2024. DOI: 10.1016/j.vaccine.2024.126396.
- Design: Observational cohort
- Sample size (indexed text): n=Not stated in abstract/full-text excerpt searched
- Full-text indexed: 0 characters (PMC when available else abstract)

- **Pre-specification — 1.5/10:** No registry, preregistration, or explicit prespecification appears in the indexed text.
- **Randomisation — 2.0/10:** No random allocation language is present in the available text.
- **Blinding — 1.5/10:** No blinding procedures are reported.
- **Comparator adequacy — 3.0/10:** Comparator arms or negative controls are weak or not named.
- **Outcome selection — 6.0/10:** Vaccine-relevant immunologic endpoints are named. "could therefore modulate the immunogenicity of some vaccine types."
- **Power — 2.0/10:** No power or sample-size justification appears in the available text.
- **Reporting completeness — 2.0/10:** Sparse quantitative reporting: limited CIs, dispersion, and missing-data handling in the indexed text.
- **Independence and replicability — 1.0/10:** Funding source is not disclosed in the indexed text (flagged).

### PMID 39609339 (vaccinology) — total **33.0/80**
Kim SW, Alacevich C, Nicodemo C, Wittenberg R, de Lusignan S, Petrou S. The Association between COVID-19 Status and Economic Costs in the Early Stages of the COVID-19 Pandemic: Evidence from a UK Symptom Surveillance Digital Survey.. *PharmacoEconomics - open* 2025. DOI: 10.1007/s41669-024-00544-0.
- Design: Observational cohort
- Sample size (indexed text): n=11534
- Full-text indexed: 45241 characters (PMC when available else abstract)

- **Pre-specification — 4.5/10:** Ethics or prospective protocol approval is noted without public analysis preregistration. "nces interdivisional research ethics committee (ms idrec) (ref. /re001) that our study does not require ethics approval"
- **Randomisation — 6.0/10:** Observational design: treatment randomisation is not applicable; score is anchored to field-appropriate conduct. "symptom surveillance digital survey. introduction: in the absence of a vaccination programme, the coronavirus disease 2"
- **Blinding — 5.0/10:** Blinding is typically not applicable to observational surveys; neutral anchor applied.
- **Comparator adequacy — 3.0/10:** Comparator arms or negative controls are weak or not named. "lost productivity. covariates controlled for in the multivariate regressions were selected on the basis of published evi"
- **Outcome selection — 3.5/10:** Multiple endpoints appear without a clear primary/secondary hierarchy. "gories of total economic cost outcomes: (i) nhs and personal social services (pss) costs and (ii) societal costs. nhs an"
- **Power — 4.0/10:** Sample size is reported for observational data without a priori power analysis. "uk. the study included 11,534 participants. methods: generalised linear models (glm) and two-part regression models were"
- **Reporting completeness — 2.0/10:** Sparse quantitative reporting: limited CIs, dispersion, and missing-data handling in the indexed text.
- **Independence and replicability — 5.0/10:** Funding is disclosed but competing-interest or sharing statements are thin. "cr-4-all project has received funding under the horizon europe research and innovation programme (grant agreement no. 10"

### PMID 39651187 (vaccinology) — total **24.5/80**
Wong DA, Shaver ZM, Cabezas MD, Daniel-Ivad M, Warfel KF, Prasanna DV, et al.. Development of cell-free platforms for discovering, characterizing, and engineering post-translational modifications.. *bioRxiv : the preprint server for biology* 2024. DOI: 10.1101/2024.03.25.586624.
- Design: Primary research (design not fully classified from metadata)
- Sample size (indexed text): n=Not stated in abstract/full-text excerpt searched
- Full-text indexed: 1615 characters (PMC when available else abstract)

- **Pre-specification — 1.5/10:** No registry, preregistration, or explicit prespecification appears in the indexed text.
- **Randomisation — 3.5/10:** Laboratory comparisons lack explicit randomisation of run order or batch assignment. "ow coupling cell-free protein synthesis (cfps) with alphalisa for the rapid expression and testing of ptm installing pro"
- **Blinding — 4.5/10:** Bench chemistry seldom uses participant blinding; omission is scored as neutral for the field, not as malpractice.
- **Comparator adequacy — 3.0/10:** Comparator arms or negative controls are weak or not named.
- **Outcome selection — 7.0/10:** Chemical performance metrics (yield/selectivity/rate) serve as declared readouts.
- **Power — 2.0/10:** No power or sample-size justification appears in the available text.
- **Reporting completeness — 2.0/10:** Sparse quantitative reporting: limited CIs, dispersion, and missing-data handling in the indexed text.
- **Independence and replicability — 1.0/10:** Funding source is not disclosed in the indexed text (flagged).

### PMID 39511601 (vaccinology) — total **34.5/80**
Moyo S, Ashok A, Myers L, Nyankieya R, Sharma S, Prasad R. The impact of COVID-19 on routine child immunisation in South Africa.. *BMC public health* 2024. DOI: 10.1186/s12889-024-20591-w.
- Design: Clinical or immunogenicity trial
- Sample size (indexed text): n=17
- Full-text indexed: 28291 characters (PMC when available else abstract)

- **Pre-specification — 4.5/10:** Ethics or prospective protocol approval is noted without public analysis preregistration. "witwatersrand human research ethics committee (h22/11/38). all procedures performed in studies involving human particip"
- **Randomisation — 6.0/10:** Observational design: treatment randomisation is not applicable; score is anchored to field-appropriate conduct. "frican demographic and health survey data were used to identify locations with a high concentration of children under fi"
- **Blinding — 4.5/10:** Bench chemistry seldom uses participant blinding; omission is scored as neutral for the field, not as malpractice.
- **Comparator adequacy — 3.0/10:** Comparator arms or negative controls are weak or not named. "ntable diseases largely under control. this study explored the impact of covid-19 on the uptake of routine child immunis"
- **Outcome selection — 7.0/10:** Chemical performance metrics (yield/selectivity/rate) serve as declared readouts.
- **Power — 4.0/10:** Sample size is reported for observational data without a priori power analysis. "ptive demographic data on the participants and asked them about their beliefs and behaviors regarding ri for their child"
- **Reporting completeness — 4.5/10:** Reporting includes confidence intervals.
- **Independence and replicability — 1.0/10:** Funding source is not disclosed in the indexed text (flagged).

### PMID 39422816 (vaccinology) — total **30.5/80**
Heimbecker V, Bordini SC, Rodrigues AC, de Alencar NM, Blanco NS, Fitz F, et al.. Gender Differences on the Awareness of Human Papillomavirus Infection and Vaccination.. *Journal of cancer education : the official journal of the American Association for Cancer Education* 2024. DOI: 10.1007/s13187-024-02516-8.
- Design: Primary research (design not fully classified from metadata)
- Sample size (indexed text): n=343
- Full-text indexed: 0 characters (PMC when available else abstract)

- **Pre-specification — 1.5/10:** No registry, preregistration, or explicit prespecification appears in the indexed text.
- **Randomisation — 6.0/10:** Observational design: treatment randomisation is not applicable; score is anchored to field-appropriate conduct.
- **Blinding — 5.0/10:** Blinding is typically not applicable to observational surveys; neutral anchor applied.
- **Comparator adequacy — 3.0/10:** Comparator arms or negative controls are weak or not named.
- **Outcome selection — 3.5/10:** Multiple endpoints appear without a clear primary/secondary hierarchy.
- **Power — 4.0/10:** Sample size is reported for observational data without a priori power analysis. "cination were administered to participants via a self-answered questionnaire. questionnaires of 343 participants were co"
- **Reporting completeness — 6.5/10:** Reporting includes confidence intervals, effect sizes. "ate odds ratios (ors) and 95% confidence intervals (95% cis) for the associations between population characteristics and"
- **Independence and replicability — 1.0/10:** Funding source is not disclosed in the indexed text (flagged).

### PMID 39635534 (vaccinology) — total **31.5/80**
He N, Li G, Liu J, Liu W, Tian R, Ma D. COVID-19 mitigates the response to TKIs in patients with CML via the inhibition of T-cell immunity.. *Frontiers in immunology* 2024. DOI: 10.3389/fimmu.2024.1452035.
- Design: Observational cohort
- Sample size (indexed text): n=109
- Full-text indexed: 33362 characters (PMC when available else abstract)

- **Pre-specification — 1.5/10:** No registry, preregistration, or explicit prespecification appears in the indexed text.
- **Randomisation — 3.5/10:** Laboratory comparisons lack explicit randomisation of run order or batch assignment. "5μl, 4.8μl of bcr-abl-210 pcr reaction solution, 1.2μl of mixed enzyme solution, and 9μl of total rna. the quantitative"
- **Blinding — 4.5/10:** Bench chemistry seldom uses participant blinding; omission is scored as neutral for the field, not as malpractice.
- **Comparator adequacy — 3.0/10:** Comparator arms or negative controls are weak or not named. "d 3 kinds of internal quality control (iqc) samples, in which high iqc sample was p210-positive k562 cells, medium or lo"
- **Outcome selection — 7.0/10:** Chemical performance metrics (yield/selectivity/rate) serve as declared readouts.
- **Power — 2.0/10:** No power or sample-size justification appears in the available text.
- **Reporting completeness — 3.0/10:** Sparse quantitative reporting: limited CIs, dispersion, and missing-data handling in the indexed text.
- **Independence and replicability — 7.0/10:** Funding and conflicts are disclosed. "d be construed as a potential conflict of interest. all claims expressed in this article are solely those of the authors"

### PMID 39137738 (vaccinology) — total **21.0/80**
Ramírez-Giraldo RH, Giraldo-Avila PA, Calle AM, Santamaria LC, Sánchez J. No Yellow Fever Vaccine Reactions in IgE-Mediated Egg Allergic Patients.. *International archives of allergy and immunology* 2025. DOI: 10.1159/000539505.
- Design: Observational cohort
- Sample size (indexed text): n=5
- Full-text indexed: 0 characters (PMC when available else abstract)

- **Pre-specification — 1.5/10:** No registry, preregistration, or explicit prespecification appears in the indexed text.
- **Randomisation — 3.5/10:** Laboratory comparisons lack explicit randomisation of run order or batch assignment. "no yellow fever vaccine reactions in ige-mediated egg allergic patients. introduction: egg allergy usually manifes"
- **Blinding — 4.5/10:** Bench chemistry seldom uses participant blinding; omission is scored as neutral for the field, not as malpractice.
- **Comparator adequacy — 3.0/10:** Comparator arms or negative controls are weak or not named.
- **Outcome selection — 3.5/10:** Multiple endpoints appear without a clear primary/secondary hierarchy.
- **Power — 2.0/10:** No power or sample-size justification appears in the available text.
- **Reporting completeness — 2.0/10:** Sparse quantitative reporting: limited CIs, dispersion, and missing-data handling in the indexed text.
- **Independence and replicability — 1.0/10:** Funding source is not disclosed in the indexed text (flagged).

### PMID 39055951 (vaccinology) — total **21.5/80**
Pham T, Shi R, Ambati S, Meagher R, Lin X. All hands on Dec: Treating cryptococcosis with dectin decorated liposomes loaded with antifungals.. *iScience* 2024. DOI: 10.1016/j.isci.2024.110349.
- Design: Clinical or immunogenicity trial
- Sample size (indexed text): n=5
- Full-text indexed: 33868 characters (PMC when available else abstract)

- **Pre-specification — 1.5/10:** No registry, preregistration, or explicit prespecification appears in the indexed text.
- **Randomisation — 2.0/10:** No random allocation language is present in the available text.
- **Blinding — 1.5/10:** No blinding procedures are reported.
- **Comparator adequacy — 8.0/10:** Named placebo, vehicle, or negative control arm. "icant differences between the negative control ls and the amb-containing groups, but no significant difference between a"
- **Outcome selection — 3.5/10:** Multiple endpoints appear without a clear primary/secondary hierarchy. "further improve the treatment outcome in the future. 50 49 delivering drugs across bbb has always been a challenge. alth"
- **Power — 2.0/10:** No power or sample-size justification appears in the available text.
- **Reporting completeness — 2.0/10:** Sparse quantitative reporting: limited CIs, dispersion, and missing-data handling in the indexed text.
- **Independence and replicability — 1.0/10:** Funding source is not disclosed in the indexed text (flagged).

### PMID 39340096 (vaccinology) — total **42.5/80**
Qin C, Joslyn S, Han JH, Savelli S, Agrawal N. Messaging to Reduce Booster Hesitancy among the Fully Vaccinated.. *Vaccines* 2024. DOI: 10.3390/vaccines12091066.
- Design: Clinical or immunogenicity trial
- Sample size (indexed text): n=1409
- Full-text indexed: 60972 characters (PMC when available else abstract)

- **Pre-specification — 6.0/10:** Preregistration on OSF or similar is mentioned. "d analyses were registered on osf: (registered on 24 november 2022). the results reported here are organized into three"
- **Randomisation — 7.5/10:** Units are randomly allocated to comparison conditions, consistent with experimental design. "elow. then, participants were randomly assigned to one of three conditions (see ), two of which provided experimental ex"
- **Blinding — 4.5/10:** Bench chemistry seldom uses participant blinding; omission is scored as neutral for the field, not as malpractice.
- **Comparator adequacy — 3.0/10:** Comparator arms or negative controls are weak or not named. "he boosters or nothing in the control group. the explanations significantly increased (compared to the control) particip"
- **Outcome selection — 7.0/10:** Chemical performance metrics (yield/selectivity/rate) serve as declared readouts.
- **Power — 5.5/10:** Target enrollment and power language appear without full calculation detail. "the explanations would be overpowered or even reversed by the effect of political ideology. in other words, the explanat"
- **Reporting completeness — 4.0/10:** Reporting includes effect sizes. "ared was used to indicate the effect sizes of the omnibus tests (0.01 = small, 0.06 = medium, and 0.14 = large; []). pla"
- **Independence and replicability — 5.0/10:** Funding is disclosed but competing-interest or sharing statements are thin. "project administration, s.j.; funding acquisition, n.a. all authors have read and agreed to the published version of the"

### PMID 39738923 (vaccinology) — total **47.0/80**
Vargas-Montes M, Valencia-Jaramillo MC, Valencia-Hernández JD, Gómez-Marín JE, Arenas AF, Cardona N. In silico identification and ex vivo evaluation of Toxoplasma gondii peptides restricted to HLA-A*02, HLA-A*24 and HLA-B*35 alleles in human PBMC from a Colombian population.. *Medical microbiology and immunology* 2024. DOI: 10.1007/s00430-024-00815-x.
- Design: Clinical or immunogenicity trial
- Sample size (indexed text): n=Not stated in abstract/full-text excerpt searched
- Full-text indexed: 68826 characters (PMC when available else abstract)

- **Pre-specification — 4.5/10:** Ethics or prospective protocol approval is noted without public analysis preregistration. "study was approved by the bioethics committee of the faculty of health sciences at the university of quindio (act numbe"
- **Randomisation — 6.0/10:** Observational design: treatment randomisation is not applicable; score is anchored to field-appropriate conduct. "ales). informed consent and a survey were obtained from all participants. among the evaluated samples, 40% (20/50) were"
- **Blinding — 4.5/10:** Bench chemistry seldom uses participant blinding; omission is scored as neutral for the field, not as malpractice.
- **Comparator adequacy — 8.0/10:** Named placebo, vehicle, or negative control arm. "ally, as negative controls, a vehicle control with 0.2% dmso diluted in rpmi, a cell control without stimulus (cc), and"
- **Outcome selection — 7.0/10:** Chemical performance metrics (yield/selectivity/rate) serve as declared readouts.
- **Power — 5.5/10:** Target enrollment and power language appear without full calculation detail. "ne candidates is considered a powerful approach that saves time and resources by reducing the number of candidates for e"
- **Reporting completeness — 4.5/10:** Reporting includes dispersion.
- **Independence and replicability — 7.0/10:** Funding and conflicts are disclosed. "0430-024-00815-x. open access funding provided by colombia consortium toxoplasmosis is a zoonotic infection caused by ("

### PMID 39576942 (chemistry) — total **24.5/80**
Huang H, Xu L, Zuo S, Ren Y, Song L, Zou C, et al.. Pioneering Built-In Interfacial Electric Field for Enhanced Anion Exchange Membrane Water Electrolysis.. *Angewandte Chemie (International ed. in English)* 2025. DOI: 10.1002/anie.202414647.
- Design: Characterization / spectroscopy study
- Sample size (indexed text): n=Not stated in abstract/full-text excerpt searched
- Full-text indexed: 0 characters (PMC when available else abstract)

- **Pre-specification — 1.5/10:** No registry, preregistration, or explicit prespecification appears in the indexed text.
- **Randomisation — 3.5/10:** Laboratory comparisons lack explicit randomisation of run order or batch assignment. "water electrolysis. as a half-reaction in anion exchange membrane water electrolysis (aemwe) technology, the hydrogen ev"
- **Blinding — 4.5/10:** Bench chemistry seldom uses participant blinding; omission is scored as neutral for the field, not as malpractice.
- **Comparator adequacy — 3.0/10:** Comparator arms or negative controls are weak or not named.
- **Outcome selection — 7.0/10:** Chemical performance metrics (yield/selectivity/rate) serve as declared readouts.
- **Power — 2.0/10:** No power or sample-size justification appears in the available text.
- **Reporting completeness — 2.0/10:** Sparse quantitative reporting: limited CIs, dispersion, and missing-data handling in the indexed text.
- **Independence and replicability — 1.0/10:** Funding source is not disclosed in the indexed text (flagged).

### PMID 39795461 (chemistry) — total **39.0/80**
Ferreira MV, Ricci P, Sobreira HA, Faria AM, Panatieri RB, Sumerlin BS, et al.. Optimization of the Heterogeneous Synthesis Conditions for Cellulose Tosylation and Synthesis of a Propargylamine Cellulosic Derivative.. *Polymers* 2024. DOI: 10.3390/polym17010058.
- Design: Characterization / spectroscopy study
- Sample size (indexed text): n=Not stated in abstract/full-text excerpt searched
- Full-text indexed: 42114 characters (PMC when available else abstract)

- **Pre-specification — 4.0/10:** Bench protocols are narrated in methods/supplement, but no formal preregistration is stated. "of a doehlert matrix for the experimental design comes from its capability to prioritize the factors deemed the most re"
- **Randomisation — 6.5/10:** Experimental units include independent or technical replicates rather than clinical randomisation. "of variation of 6.20% for the triplicate measurements at the center point. these values indicate that the synthesis meth"
- **Blinding — 4.5/10:** Bench chemistry seldom uses participant blinding; omission is scored as neutral for the field, not as malpractice.
- **Comparator adequacy — 3.0/10:** Comparator arms or negative controls are weak or not named. "the ds in these reactions is controlled, in part, by the molar ratio (mr) of the derivatizing agent to the anhydrogluco"
- **Outcome selection — 7.0/10:** Chemical performance metrics (yield/selectivity/rate) serve as declared readouts. ", 10:1 molar ratio, and 30 °c-yielded a degree of substitution for tosyl groups (dstos) of 1.80, determined via elementa"
- **Power — 2.0/10:** No power or sample-size justification appears in the available text.
- **Reporting completeness — 7.0/10:** Reporting includes confidence intervals, dispersion.
- **Independence and replicability — 5.0/10:** Funding is disclosed but competing-interest or sharing statements are thin. "tration, b.s.s. and r.m.n.a.; funding acquisition, b.s.s. and r.m.n.a. all authors have read and agreed to the published"

### PMID 39196453 (chemistry) — total **24.5/80**
Yang J, Lin F, Ma T, Gao L, Wang B, Tan S, et al.. Colorimetric detection of Staphylococcus aureus with enhanced sensitivity based on phage covalently immobilized Co. *Mikrochimica acta* 2024. DOI: 10.1007/s00604-024-06639-z.
- Design: Laboratory experimental study
- Sample size (indexed text): n=Not stated in abstract/full-text excerpt searched
- Full-text indexed: 0 characters (PMC when available else abstract)

- **Pre-specification — 1.5/10:** No registry, preregistration, or explicit prespecification appears in the indexed text.
- **Randomisation — 3.5/10:** Laboratory comparisons lack explicit randomisation of run order or batch assignment. "ccelerate the tmb chromogenic reaction. upon introduction of s. aureus, specific capture by sapyzuh5@co3o4 resulted in i"
- **Blinding — 4.5/10:** Bench chemistry seldom uses participant blinding; omission is scored as neutral for the field, not as malpractice.
- **Comparator adequacy — 3.0/10:** Comparator arms or negative controls are weak or not named.
- **Outcome selection — 7.0/10:** Chemical performance metrics (yield/selectivity/rate) serve as declared readouts. "ced sensitivity of s. aureus, yielding an equation: a = - 0.092 log (csa) + 0.79 (r2 = 0.987), with an ultralow limit o"
- **Power — 2.0/10:** No power or sample-size justification appears in the available text.
- **Reporting completeness — 2.0/10:** Sparse quantitative reporting: limited CIs, dispersion, and missing-data handling in the indexed text.
- **Independence and replicability — 1.0/10:** Funding source is not disclosed in the indexed text (flagged).

### PMID 39570149 (chemistry) — total **24.5/80**
Rani N, Kumar R, Mazumder S. AI-Driven Discovery of Asymmetric Pauson-Khand Reactions: A New Toolbox in a Synthetic Chemist's Treasure.. *The journal of physical chemistry. A* 2024. DOI: 10.1021/acs.jpca.4c06701.
- Design: Experimental synthesis or catalysis study
- Sample size (indexed text): n=Not stated in abstract/full-text excerpt searched
- Full-text indexed: 0 characters (PMC when available else abstract)

- **Pre-specification — 1.5/10:** No registry, preregistration, or explicit prespecification appears in the indexed text.
- **Randomisation — 3.5/10:** Laboratory comparisons lack explicit randomisation of run order or batch assignment. "ignificant impact on chemical synthesis, and they are important components in an experimental chemist's toolbox. however"
- **Blinding — 4.5/10:** Bench chemistry seldom uses participant blinding; omission is scored as neutral for the field, not as malpractice.
- **Comparator adequacy — 3.0/10:** Comparator arms or negative controls are weak or not named.
- **Outcome selection — 7.0/10:** Chemical performance metrics (yield/selectivity/rate) serve as declared readouts.
- **Power — 2.0/10:** No power or sample-size justification appears in the available text.
- **Reporting completeness — 2.0/10:** Sparse quantitative reporting: limited CIs, dispersion, and missing-data handling in the indexed text.
- **Independence and replicability — 1.0/10:** Funding source is not disclosed in the indexed text (flagged).

### PMID 39162869 (chemistry) — total **21.0/80**
Bassolino L, Fulvio F, Cerrato A, Citti C, Cannazza G, Capriotti AL, et al.. Metabolic characterization and transcriptional profiling of polyphenols in Cannabis sativa L. inflorescences with different chemical phenotypes.. *Planta* 2024. DOI: 10.1007/s00425-024-04505-z.
- Design: Experimental synthesis or catalysis study
- Sample size (indexed text): n=Not stated in abstract/full-text excerpt searched
- Full-text indexed: 0 characters (PMC when available else abstract)

- **Pre-specification — 1.5/10:** No registry, preregistration, or explicit prespecification appears in the indexed text.
- **Randomisation — 3.5/10:** Laboratory comparisons lack explicit randomisation of run order or batch assignment. "molecular basis of flavonoid synthesis and how their content can be modulated by specific transcription factors will sh"
- **Blinding — 4.5/10:** Bench chemistry seldom uses participant blinding; omission is scored as neutral for the field, not as malpractice.
- **Comparator adequacy — 3.0/10:** Comparator arms or negative controls are weak or not named.
- **Outcome selection — 3.5/10:** Multiple endpoints appear without a clear primary/secondary hierarchy.
- **Power — 2.0/10:** No power or sample-size justification appears in the available text.
- **Reporting completeness — 2.0/10:** Sparse quantitative reporting: limited CIs, dispersion, and missing-data handling in the indexed text.
- **Independence and replicability — 1.0/10:** Funding source is not disclosed in the indexed text (flagged).

### PMID 39497153 (chemistry) — total **28.0/80**
Guerrero-Hernández C, Doddihal V, Mann FG, Sánchez Alvarado A. A powerful and versatile new fixation protocol for immunostaining and in situ hybridization that preserves delicate tissues.. *BMC biology* 2024. DOI: 10.1186/s12915-024-02052-3.
- Design: Laboratory experimental study
- Sample size (indexed text): n=Not stated in abstract/full-text excerpt searched
- Full-text indexed: 39051 characters (PMC when available else abstract)

- **Pre-specification — 1.5/10:** No registry, preregistration, or explicit prespecification appears in the indexed text.
- **Randomisation — 3.5/10:** Laboratory comparisons lack explicit randomisation of run order or batch assignment. "ible with hybridization chain reaction v3.0 (hcr) which uses multiple short rna probes []. future studies will determine"
- **Blinding — 7.0/10:** Masking/blinding terminology is used for at least one study role. "fixed without formic acid was masked by background noise (fig. b, c). similar results were observed for a blastema gene,"
- **Comparator adequacy — 3.0/10:** Comparator arms or negative controls are weak or not named.
- **Outcome selection — 7.0/10:** Chemical performance metrics (yield/selectivity/rate) serve as declared readouts. "ing killifish tail fin, which yielded better ish signal with minimal background. conclusions: thus, the nafa protocol ro"
- **Power — 2.0/10:** No power or sample-size justification appears in the available text.
- **Reporting completeness — 3.0/10:** Sparse quantitative reporting: limited CIs, dispersion, and missing-data handling in the indexed text.
- **Independence and replicability — 1.0/10:** Funding source is not disclosed in the indexed text (flagged).

### PMID 39160593 (chemistry) — total **45.0/80**
Valieris R, Martins L, Defelicibus A, Bueno AP, de Toledo Osorio CAB, Carraro D, et al.. Weakly-supervised deep learning models enable HER2-low prediction from H &E stained slides.. *Breast cancer research : BCR* 2024. DOI: 10.1186/s13058-024-01863-0.
- Design: Observational cohort
- Sample size (indexed text): n=546
- Full-text indexed: 38648 characters (PMC when available else abstract)

- **Pre-specification — 4.0/10:** Ethics or prospective protocol approval is noted without public analysis preregistration. "approval (#3028/20) from the ethics committee of the fundação antônio prudente, with all cases with metastasis or neoad"
- **Randomisation — 7.5/10:** Units are randomly allocated to comparison conditions, consistent with experimental design. "dation folds where cases were randomly assigned to a training (85%) or validation set (15%) while ensuring that the labe"
- **Blinding — 4.5/10:** Bench chemistry seldom uses participant blinding; omission is scored as neutral for the field, not as malpractice.
- **Comparator adequacy — 3.0/10:** Comparator arms or negative controls are weak or not named. ", including stringent quality controls [, ] and novel quantitative testing that allows measuring a range of antibody con"
- **Outcome selection — 7.0/10:** Chemical performance metrics (yield/selectivity/rate) serve as declared readouts.
- **Power — 5.5/10:** Target enrollment and power language appear without full calculation detail. "model shows a discriminatory power to predict her2 group directly from h &e histology. the worst performance is obtaine"
- **Reporting completeness — 4.5/10:** Reporting includes dispersion.
- **Independence and replicability — 9.0/10:** Funding, conflicts, and data/materials sharing are all addressed. "ors declare that they have no conflict of interest. this study received ethical approval (#3028/20) from the ethics comm"

### PMID 39622773 (chemistry) — total **34.0/80**
Durka J, Zielińska B, Gryko D. Aliphatic Amines Unlocked for Selective Transformations through Diazotization.. *Angewandte Chemie (International ed. in English)* 2025. DOI: 10.1002/anie.202419450.
- Design: Experimental synthesis or catalysis study
- Sample size (indexed text): n=Not stated in abstract/full-text excerpt searched
- Full-text indexed: 24909 characters (PMC when available else abstract)

- **Pre-specification — 4.0/10:** Bench protocols are narrated in methods/supplement, but no formal preregistration is stated. "ready the main process. these experimental data indicate that the acidity of hfip itself is sufficient for complete conv"
- **Randomisation — 3.5/10:** Laboratory comparisons lack explicit randomisation of run order or batch assignment. "important reagents in organic synthesis, 'diazonium ions generated from ordinary aliphatic primary amines are usually us"
- **Blinding — 4.5/10:** Bench chemistry seldom uses participant blinding; omission is scored as neutral for the field, not as malpractice.
- **Comparator adequacy — 3.0/10:** Comparator arms or negative controls are weak or not named. "id, and it is now possible to control diazotization of aliphatic amines by utilizing isopentyl nitrite in hfip. this tra"
- **Outcome selection — 7.0/10:** Chemical performance metrics (yield/selectivity/rate) serve as declared readouts. "msoh (1 equiv.) increased the yield up to 70%. kinetic studies revealed that electrophilic aromatic substitution is much"
- **Power — 2.0/10:** No power or sample-size justification appears in the available text.
- **Reporting completeness — 3.0/10:** Sparse quantitative reporting: limited CIs, dispersion, and missing-data handling in the indexed text.
- **Independence and replicability — 7.0/10:** Funding and conflicts are disclosed. "salts. the authors declare no conflict of interest. as a service to our authors and readers, this journal provides suppo"

### PMID 39327745 (chemistry) — total **21.0/80**
Ibáñez-Prada ED, Guerrero JL, Bustos IG, León L, Fuentes YV, Santamaría-Torres M, et al.. The unique metabolic and lipid profiles of patients with severe COVID-19 compared to severe community-acquired pneumonia: a potential prognostic and therapeutic target.. *Expert review of respiratory medicine* 2024. DOI: 10.1080/17476348.2024.2409264.
- Design: Laboratory experimental study
- Sample size (indexed text): n=127
- Full-text indexed: 0 characters (PMC when available else abstract)

- **Pre-specification — 1.5/10:** No registry, preregistration, or explicit prespecification appears in the indexed text.
- **Randomisation — 3.5/10:** Laboratory comparisons lack explicit randomisation of run order or batch assignment.
- **Blinding — 4.5/10:** Bench chemistry seldom uses participant blinding; omission is scored as neutral for the field, not as malpractice.
- **Comparator adequacy — 3.0/10:** Comparator arms or negative controls are weak or not named. "reased viral proliferation, uncontrolled inflammation, and thrombi formation. results provide novel targets for predicti"
- **Outcome selection — 3.5/10:** Multiple endpoints appear without a clear primary/secondary hierarchy.
- **Power — 2.0/10:** No power or sample-size justification appears in the available text.
- **Reporting completeness — 2.0/10:** Sparse quantitative reporting: limited CIs, dispersion, and missing-data handling in the indexed text.
- **Independence and replicability — 1.0/10:** Funding source is not disclosed in the indexed text (flagged).

### PMID 39722526 (chemistry) — total **21.0/80**
Liddelow SA, Zhang Y, Sloan SA. WebSEQ: A New Tool for Democratizing Omics Data Sharing.. *Glia* 2025. DOI: 10.1002/glia.24646.
- Design: Laboratory experimental study
- Sample size (indexed text): n=Not stated in abstract/full-text excerpt searched
- Full-text indexed: 0 characters (PMC when available else abstract)

- **Pre-specification — 1.5/10:** No registry, preregistration, or explicit prespecification appears in the indexed text.
- **Randomisation — 3.5/10:** Laboratory comparisons lack explicit randomisation of run order or batch assignment.
- **Blinding — 4.5/10:** Bench chemistry seldom uses participant blinding; omission is scored as neutral for the field, not as malpractice.
- **Comparator adequacy — 3.0/10:** Comparator arms or negative controls are weak or not named.
- **Outcome selection — 3.5/10:** Multiple endpoints appear without a clear primary/secondary hierarchy.
- **Power — 2.0/10:** No power or sample-size justification appears in the available text.
- **Reporting completeness — 2.0/10:** Sparse quantitative reporting: limited CIs, dispersion, and missing-data handling in the indexed text.
- **Independence and replicability — 1.0/10:** Funding source is not disclosed in the indexed text (flagged).

### PMID 39485867 (chemistry) — total **24.5/80**
Kang Y, Chang R, Ju SY. Pressure-Dependent Shape and Edge Configurations of MoS. *ACS nano* 2024. DOI: 10.1021/acsnano.4c12342.
- Design: Laboratory experimental study
- Sample size (indexed text): n=Not stated in abstract/full-text excerpt searched
- Full-text indexed: 0 characters (PMC when available else abstract)

- **Pre-specification — 1.5/10:** No registry, preregistration, or explicit prespecification appears in the indexed text.
- **Randomisation — 3.5/10:** Laboratory comparisons lack explicit randomisation of run order or batch assignment.
- **Blinding — 4.5/10:** Bench chemistry seldom uses participant blinding; omission is scored as neutral for the field, not as malpractice.
- **Comparator adequacy — 3.0/10:** Comparator arms or negative controls are weak or not named. "underscore the importance of controlling both growth and cessation phases in the cvd process to customize edge configur"
- **Outcome selection — 7.0/10:** Chemical performance metrics (yield/selectivity/rate) serve as declared readouts.
- **Power — 2.0/10:** No power or sample-size justification appears in the available text.
- **Reporting completeness — 2.0/10:** Sparse quantitative reporting: limited CIs, dispersion, and missing-data handling in the indexed text.
- **Independence and replicability — 1.0/10:** Funding source is not disclosed in the indexed text (flagged).

### PMID 39497763 (chemistry) — total **44.0/80**
Keever K, Askari B. Exacerbation of atherosclerosis, hyperlipidemia and inflammation by MK886, an inhibitor of leukotriene biosynthesis, in obese and diabetic mice.. *Current research in pharmacology and drug discovery* 2024. DOI: 10.1016/j.crphar.2024.100203.
- Design: Experimental synthesis or catalysis study
- Sample size (indexed text): n=5
- Full-text indexed: 32841 characters (PMC when available else abstract)

- **Pre-specification — 1.5/10:** No registry, preregistration, or explicit prespecification appears in the indexed text.
- **Randomisation — 7.5/10:** Units are randomly allocated to comparison conditions, consistent with experimental design. "y as a pilot study. mice were randomly assigned to 2 groups of littermates and housed in rooms on a 12 light/12 dark cyc"
- **Blinding — 7.0/10:** Masking/blinding terminology is used for at least one study role. ". all analyses were made in a masked fashion and performed as follows. to visualize atherosclerotic lesions in the aorti"
- **Comparator adequacy — 3.0/10:** Comparator arms or negative controls are weak or not named. "sis are subject to regulatory control, modulation of the expression and function of 5lo and flap are critical steps ()."
- **Outcome selection — 7.0/10:** Chemical performance metrics (yield/selectivity/rate) serve as declared readouts. "as a peroxidase substrate to yield a red-brown reaction product. nuclei were identified by counterstaining with hematox"
- **Power — 2.0/10:** No power or sample-size justification appears in the available text.
- **Reporting completeness — 7.0/10:** Reporting includes confidence intervals, dispersion.
- **Independence and replicability — 9.0/10:** Funding, conflicts, and data/materials sharing are all addressed. "from the and mmpc micromouse funding program []. the authors declare that they have no known competing financial intere"

## Structural differences (sample-specific)

1. **Outcome typing:** Chemistry draws more often declare bench readouts (yield/selectivity/rate); vaccinology draws mix immunologic endpoints with surveys and health-economics papers that mention vaccines only peripherally.
2. **Comparator culture:** Vaccinology arms with explicit placebo/vehicle language score higher on comparator adequacy when present; chemistry papers in this sample seldom name negative controls beyond implicit product checks (compressed scores at 3.0).
3. **Registration gap:** Both fields skew low on pre-specification; only a minority cite ClinicalTrials.gov/NCT or OSF preregistration in indexed text.

## Limitations

- **Query breadth:** Vaccine keyword hits include non-intervention papers (awareness, unrelated clinical associations). Chemistry MeSH/title hits include clinical omics and ML pathology papers, not only synthetic chemistry.
- **Text access:** Several papers lack PMC full text; scoring used PubMed abstract plus PMC body when available—publisher PDFs were not uniformly accessed.
- **Cross-field rubric:** Blinding and randomisation dimensions required design-aware anchors; observational vaccine surveys were scored against achievable practice, not against RCT ideals.
- **Automation:** Initial keyword scoring was manually reviewed on rescore; borderline CONSORT/STROBE items may still be under-detected without human full-text read of all supplements.

## Verdict

On this reproducible random sample, **total methodological rigor does not differ significantly between fields** (Mann–Whitney p≈0.91; vaccinology mean 29.5 vs chemistry 29.3/80). The claim that vaccinology is globally weaker than chemistry is **not supported** here.

Directional (non-significant) patterns: vaccinology papers score higher on comparator adequacy when experimental controls exist; chemistry papers score slightly higher on outcome selection among declared bench metrics. **Pre-specification and funding disclosure are weak in both fields** in this sample—not a vaccinology-specific deficit.

## Artifacts

- Script: `scripts/methodological_rigor_audit.py`
- Data: `tmp/rigor-audit/papers.json`, `tmp/rigor-audit/analysis.json`, `tmp/rigor-audit/sampling.json`