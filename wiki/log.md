---
tags:
  - scientism
  - evidence-standard
  - authority-as-evidence
  - experiment-first
  - vault-maintenance
  - science
  - meta
  - methodology
  - methodological-critique
  - replication-crisis
---

# Log — Scientism

> Append-only timeline. Every LLM operation leaves an entry here.
>
> Format: `## [YYYY-MM-DD] <op> | <title>` followed by an optional detail line.
> Valid ops: `ingest`, `query`, `lint`, `create`, `update`, `delete`, `note`.
>
> Grep the last 10 entries: `grep "^## \[" log.md | tail -10`

## [2026-11-10] create | Munywoki 2014 JID household RSV cohort (queue item 17: GAP 3 RSV row) and Sauter 2026 Nat Commun PHIRST influenza household transmission (queue item 18: GAP 3 influenza replication row)
Run 11 of the source-verification loop. Item 17 done after citation reconciliation (no Munywoki 2013 PLoS ONE paper exists; actual primary: J Infect Dis 2014;209(11):1685-1692, PMID 24367040, PMC4017365) - [[sources/munywoki-2014-rsv-infant-source-household-cohort]] written from full text; RSV ladder gained its first natural-route household-cohort rung. Item 18 done: [[sources/sauter-2026-phirst-influenza-household-transmission]] (Nat Commun 2026;17:9238, PMC13526887) written from full text; influenza ladder GAP 3 rung extended to two rows ([[sources/kim-2012-kenya-household-pdm09-transmission-cohort]] + Sauter 2026). Cross-cutting ladder GAP 3 note extended and RSV note updated. Tsang 2023 PNAS Hong Kong household reconstruction (PMC10436695) retrieved, left as a next-run lead. Both queue rows marked done with full extracts.

## [2026-11-10] ingest | Aiello 2012 PLoS ONE and Suess 2012 BMC Infect Dis household/residence-hall NPI trials (queue items 15-16: GAP 2 replication rows)
Run 10 of the source-verification loop. Both verified end to end from Europe PMC full text (PMC3266257, PMC3285078); sources pages written; influenza ladder natural-route rung and cross-cutting ladder extended to a replicated 3/3-null-as-randomized result; queue item 5 (Herlocher 2004) re-exhausted and remains unverifiable; queue items 15/16 marked done with full extracts and recorded table/label inconsistencies.

## [2026-05-04] note | Vault initialized
Topic: **Scientism**. Layers created: `raw/`, `wiki/{entities,concepts,sources,comparisons,synthesis}`.
Schema loader: `CLAUDE.md` + `AGENTS.md` + `.cursorrules`.

## [2026-05-04] update | Scientism seed source ingested and schema specialized

Updated AGENTS.md and CLAUDE.md. Added source, concept, entity, comparison, and synthesis starter pages from raw/Scientism.md. Regenerated wiki/index.md.

## [2026-05-04] ingest | Raw corpus batch ingested into wiki

Batch-ingested the broader `raw/` corpus into `wiki/sources/` with evidence-quality triage, added new methodology and history concept/entity pages, expanded synthesis, and regenerated `wiki/index.md`. Out-of-scope or low-signal notes were preserved but marked explicitly rather than forced into conclusions.

## [2026-05-04] create | Vault maintenance guide

Added a meta synthesis page describing how to maintain the vault, including ingest, query, lint, triage, and local script usage.

## [2026-05-04] ingest | Scobey polio article and AIDS congressional letter

Added attributed source pages for the Scobey poliomyelitis-poisoning article and the 1995 Gutknecht-to-Fauci AIDS letter, updated related polio/AIDS and inferential-leap pages, refreshed synthesis triage/overview, and regenerated `wiki/index.md`.

## [2026-05-04] query | Gutknecht letter questions 7-9

Added a narrow synthesis page answering questions 7-9 with primary and official sources only, linked it from the 1995 Gutknecht letter source page, and prepared the vault for regenerated indexing.

## [2026-05-04] query | Gutknecht letter questions 1-12

Added a consolidated synthesis page answering all 12 questions from the March 24, 1995 Gutknecht letter, keeping 1995 framing separate from stronger current evidence and marking the unresolved funding-total question explicitly.

## [2026-05-04] update | Tightened evidence standard against appeal to authority

Updated `CLAUDE.md` and `AGENTS.md` to require experiment-first support, explicitly reject authority summaries as scientific evidence, and downgrade the Gutknecht evidence-check page to unresolved pending direct study-level reconstruction.

## [2026-05-04] update | Removed authority-style evidence from Gutknecht notes

Reworked the Gutknecht synthesis pages so the consolidated page is now only a research worklist and the 7-9 detail page keeps only direct-study support where available.

## [2026-05-04] update | Vault-wide experiment-first evidence cleanup

Updated wiki templates, synthesis pages, concept/entity pages, and flagged source pages to enforce direct method, endpoint, result, and limitation requirements; added lint checks for authority-as-evidence phrasing and unsupported `claim_status: supported` pages.

## [2026-05-04] ingest | ViroLIEgy method page, Rosenau influenza page, and Leverson germ-theory critique

Added three Tier 3 source pages from `raw/`, updated germ-theory and scientism-related concept/entity/synthesis pages, kept all conclusions attribution-bound, and flagged the new material as dispute-mapping and follow-up research leads rather than closure.

## [2026-05-05] query | Pediatric vaccine placebo-control trial audit

Used Lens scholarly search and PubMed abstracts to check the 18 trial records cited by the CHD pediatric vaccine placebo-control source. Added a trial-record audit page, linked it from the CHD source page, and updated placebo-control and endpoint concept pages to distinguish active comparators, placebo-labeled comparators, and unresolved placebo composition.

## [2026-05-05] query | Vaccinated children more healthy question

Added a direct synthesis answer clarifying that the currently audited vaccine trials do not establish that vaccinated children are more healthy than not vaccinated children, because the measured endpoints are mostly narrower disease, immunogenicity, or short-term safety outcomes rather than broader overall-health comparisons.

## [2026-05-05] query | Lens shortlist for vaccinated-versus-unvaccinated health outcomes

Ran tighter Lens searches for vaccinated-versus-unvaccinated child health outcomes, including all-cause mortality, hospitalization, chronic disease, neurodevelopment, asthma, allergy, and development endpoints. Added the strongest candidate studies and search strings to the vaccinated-children synthesis page.

## [2026-05-05] update | Added results to vaccinated-children shortlist

Added abstract-level reported results for each shortlisted study in the vaccinated-versus-unvaccinated health-outcomes synthesis page, keeping the result separate from each study's design limits.

## [2026-05-05] update | Added interpretation boundary to vaccinated-children synthesis

Clarified that the current shortlist does not establish a broad overall-health benefit claim for childhood vaccination, while also requiring vaccine-specific and endpoint-specific support before converting harm associations into universal causal conclusions.

## [2026-05-05] update | Added parental messaging endpoint boundary

Updated the vaccinated-children synthesis, disease-prevention comparison, inferential-leap concept, and research-program overview to state that parents may hear disease-specific vaccine evidence presented as proof of overall child-health benefit. Marked that as an inferential leap unless broad health outcomes are directly measured.

## [2026-05-05] ingest | Effectiveness and Cost-Benefit of Influenza Vaccination of Healthy Working Adults

Added a Tier 1 source page for the Bridges et al. randomized saline-placebo influenza vaccine trial in healthy working adults. Updated clinical endpoints, placebo controls, inferential leap, disease-prevention versus health-outcomes, source-corpus triage, and regenerated `wiki/index.md`.

## [2026-05-05] update | Corrected 1997-1998 influenza vaccine trial endpoint summary

Revised the Bridges et al. source summary and related endpoint/comparison pages to preserve the paper's unfavorable 1997-1998 clinical-utilization finding: vaccine recipients reported significantly more ILI-related sick days, lost workdays, and physician-visit work hours than placebo recipients.

## [2026-05-05] update | Added warning-gap framing for Bridges influenza vaccine trial

Updated the Bridges et al. source page, scientism concept page, inferential-leap page, and research-program overview to treat the unfavorable 1997-1998 randomized clinical-utilization findings as a central author-conclusion versus endpoint-result case for the vault.

## [2026-05-05] update | Gutknecht questions 7-9 direct-study expansion

Ran one PMID/DOI API lookup per candidate paper for the Gutknecht questions 7-9 audit, saved PubMed JSON/CSV and Lens JSON lookup dumps under `wiki/synthesis/`, added linked source pages for the direct studies and chronology records, rebuilt the direct-study registers, and preserved full-text-needed flags where abstracts were insufficient.

## [2026-05-05] update | Answered Gutknecht evidence-check page

Converted the Gutknecht evidence-check synthesis from a pure worklist into a current answer page under the vault evidence standard. Marked questions 1-3 and 7-9 as partial answers where direct studies now exist, kept questions 4-6 and 10-12 unresolved, and repaired the Q7-9 chronology table formatting.

## [2026-05-06] query | Clarified European Collaborative Study 1991 mortality denominator

Updated the 1991 perinatal HIV source page to clarify that the 17% by-12-month mortality estimate applies to infected children, not all 600 enrolled children; that the transmission estimate used the mature follow-up subset; and that the 1991 abstract does not itself report treatment exposure or mortality among presumed-uninfected exposed children.

## [2026-05-06] query | Added denominator and drug-toxicity boundary

Added a further boundary to the European Collaborative Study 1991 source page: the abstract does not support re-denominating the infected-child death endpoint over all 600 enrolled children, and it does not support attributing deaths to drug toxicity without treatment-stratified mortality data.

## [2026-05-06] query | Virus-disease attribution audit worklist

Created `wiki/synthesis/virus-disease-attribution-audit-worklist.md`, listed a practical starter set of disease-virus attribution claims, and used parallel Lens searches to log candidate foundational papers for AIDS/HIV, poliomyelitis/poliovirus, rabies, smallpox, measles, influenza, COVID-19, and cervical cancer/HPV.

## [2026-05-06] query | Virus causation inferential-leap analysis

Added `wiki/synthesis/virus-causation-inferential-leaps.md` to separate what foundational virus-attribution experiments directly tested from the broader causation narratives later built on them, with a specific provisional warning about polio-style artificial-route challenge experiments versus natural-route causation claims.

## [2026-05-06] query | Failed virus-causation attempt register

Added `wiki/synthesis/failed-virus-causation-attempts-register.md` to track failed, negative, or non-confirmatory experimental leads alongside the foundation-paper shortlist, including a direct primary lead for poliomyelitis transmission problems and a commentary-led influenza failure track that still needs primary reconstruction.

## [2026-05-06] ingest | Sabin 1938 and Rosenau 1919 negative-result source pages

Added direct source pages for Sabin and Olitsky's 1938 poliomyelitis intranasal tissue-recovery paper and Rosenau's 1919 JAMA influenza transmission report, then expanded `wiki/synthesis/failed-virus-causation-attempts-register.md` and the inferential-leap synthesis so the polio and influenza failed-attempt entries now rest on primary papers with explicit endpoint boundaries.

## [2026-05-06] query | SARS-CoV-2 COVID-19 causation endpoint audit

Added `wiki/synthesis/sars-cov-2-covid-causation-audit.md` to downgrade the Killingley human challenge paper from causation proof to uncontrolled challenge-model evidence, separate PCR endpoints from infectious-virus or disease-causation endpoints, and distinguish virus characterization, animal-model pathogenicity, and unresolved controlled human clinical causation.

## [2026-05-07] query | COVID early intubation and noninvasive ventilation Lens summary

Created `wiki/synthesis/covid-early-intubation-noninvasive-ventilation-lens-summary.md` from Lens DOI lookups covering 14 early-intubation, HFNC, and NIV papers. Saved abstract-derived summaries, DOI/Lens IDs, study type, protocol issue, and endpoint signals without reproducing full copyrighted abstracts.

## [2026-05-08] query | Shingles VZV causation and vaccine trial audit

Used Lens-assisted parallel searches to log endpoint-level candidate papers for shingles etiology, foundational varicella-zoster culture/serology/latency evidence, and modern zoster vaccine randomized trials. Added `wiki/synthesis/shingles-vzv-causation-and-vaccine-trial-audit.md` and linked it from the virus-disease attribution worklist.

## [2026-05-10] query | Continued virus-disease attribution audit worklist

Used Lens-assisted parallel searches to expand the attribution worklist for mumps, rubella, chickenpox, hepatitis A/B/C, infectious mononucleosis, Burkitt lymphoma, and Kaposi sarcoma. Updated the inferential-leap synthesis to preserve detection, serology, animal challenge, molecular-clone, prospective cohort, tumor-association, and lesion-specific endpoints as separate evidence questions.

## [2026-05-14] query | Viral disease causation evidence ladder

Used Lens lookups and source checks to add Rivers 1937, Fredericks and Relman 1996, and Jefferson et al. 2022 as methodological source pages. Added `wiki/synthesis/viral-disease-causation-evidence-ladder.md` to separate detection, isolation, serology, challenge, transmission, intervention, and replicated-convergence endpoints, then linked it from the virus-disease worklist, inferential-leap synthesis, failed-attempt register, and core concept pages.

## [2026-05-14] query | Failed virus-causation attempt follow-up candidates

Used Lens-assisted parallel searches to replace the "no clear failed-attempt paper in hand yet" rows for measles, smallpox, rabies, AIDS/HIV, and cervical cancer/HPV with candidate failed-attempt, route-boundary, host-range, nonprogression, exclusivity-boundary, HPV-negative, assay-failure, and insufficiency papers. Kept the entries provisional where full-text primary extraction is still needed.

## [2026-05-21] query | Specific vaccine overall health outcome evidence

Added `wiki/sources/cutts-2005-pcv9-gambia-rct.md` and `wiki/synthesis/specific-vaccine-overall-health-outcome-evidence.md` to preserve the clearest favorable direct evidence found so far: a randomized, double-blind, placebo-controlled PCV9 trial in Gambian children reporting lower all-cause admissions and all-cause mortality in the vaccine group. Updated the broader vaccinated-children synthesis to keep this narrow evidence separate from the unresolved whole-schedule question.

## [2026-05-31] create | Scientism methodological overreach manuscript

Added `wiki/synthesis/scientism-methodological-overreach-and-the-discipline-of-evidence.md` as a long-form research manuscript summarizing the vault's current evidence grammar, endpoint discipline, germ-theory and virology causation audits, negative-result handling, AIDS/AZT evidence checks, vaccine health-outcome distinctions, and open research agenda. Linked it from `wiki/synthesis/scientism-research-program-overview.md`.

## [2026-05-31] update | Polio evidence ladder pass

Added `wiki/synthesis/poliomyelitis-poliovirus-evidence-ladder.md`, created a full-text-backed source page for Enders, Weller, and Robbins 1949 tissue-culture cultivation of the Lansing strain, and expanded the manuscript's polio section to separate monkey challenge, route/tissue recovery, tissue culture, direct-isolation gaps, and ordinary natural-route causation.

## [2026-05-31] update | Influenza evidence ladder pass

Added `wiki/synthesis/influenza-influenza-virus-evidence-ladder.md`, created full-text-backed source pages for Smith, Andrewes, and Laidlaw 1933 and Shope and Francis 1936, and expanded the manuscript's influenza section to separate Rosenau's pre-virus human challenge failures from ferret passage, swine susceptibility, contact-boundary, serology, and ordinary human natural-route causation.

## [2026-05-31] update | Mumps evidence ladder pass

Added `wiki/synthesis/mumps-mumps-virus-evidence-ladder.md`, created full-text-backed source pages for Johnson and Goodpasture 1934, Leymaster and Ward 1947, and Henle et al. 1948, and expanded the manuscript and cross-cutting virology pages to separate monkey parotid-duct inoculation, chick-embryo isolation, induced human exposure, serology, saliva shedding, and ordinary community transmission.

## [2026-05-31] update | Rubella evidence ladder pass

Added `wiki/synthesis/rubella-rubella-virus-evidence-ladder.md`, created full-text-backed source pages for Parkman, Buescher, and Artenstein 1962, Weller and Neva 1962, and Sigurdardottir et al. 1963, and expanded the manuscript and cross-cutting virology pages to separate acute-case recovery, tissue-culture propagation, paired-serology, monkey inoculation, congenital-rubella acquisition gaps, and ordinary transmission.

## [2026-05-31] update | Chickenpox VZV evidence ladder pass

Added `wiki/synthesis/chickenpox-varicella-zoster-virus-evidence-ladder.md`, created full-text-backed source pages for Weller 1953, Cheatham et al. 1956, and Weller, Witton, and Bell 1958, and expanded the manuscript and cross-cutting virology pages to separate lesion-fluid culture, fatal-case blood/tissue recovery, varicella-zoster culture similarity, zoster latency/reactivation, and ordinary chickenpox transmission.

## [2026-05-31] update | Hepatitis B evidence ladder pass
Added a hepatitis B/HBV ladder page and source pages for Krugman, Giles, and Hammond 1967 and Acs et al. 1987, separating pre-HAV/HBV syndrome-split evidence from molecular-clone/cell-produced virion infectivity in intravenously inoculated chimpanzees and from unresolved Australia-antigen, early chimpanzee-passage, and ordinary human transmission rungs.

## [2026-05-31] update | Hepatitis C evidence ladder pass
Added a hepatitis C/HCV ladder page and source pages for Choo et al. 1989, Kuo et al. 1989, Alter et al. 1989, and Yanagi et al. 1997, separating molecular identification, recombinant-antigen antibody assay validation, prospective transfusion serology, donor linkage, molecular-clone infectivity, noninfectious-clone boundaries, and unresolved 1984 chimpanzee passage, 1999 transmissible-virion clone, ordinary transmission, and chronic-disease mechanism rungs.

## [2026-05-31] update | Cervical cancer HPV evidence ladder pass
Added a cervical cancer/HPV ladder page and source pages for Durst et al. 1983, Boshart et al. 1984, Durst et al. 1985, Matsukura et al. 1986, and Cullen et al. 1991, separating HPV16/18 tumor-DNA detection, type specificity, physical-state analysis, integration, viral-cell junction structure, integration-boundary evidence, and unresolved prospective progression, necessity, sufficiency, cofactor, and intervention rungs.

## [2026-05-31] update | Kaposi sarcoma HHV-8 evidence ladder pass
Added a Kaposi sarcoma/HHV-8 ladder page and source pages for Chang et al. 1994, Moore and Chang 1995, O'Neill et al. 1996, and Moore et al. 1996, separating KSHV molecular discovery, lesion PCR, cross-status detection, lesion-versus-normal tissue boundaries, viral characterization, infected-cell-line evidence, limited serology, and unresolved transmission, prospective timing, necessity, sufficiency, cofactor, and tumor-initiation rungs.

## [2026-05-31] update | Infectious mononucleosis EBV evidence ladder pass
Added an infectious mononucleosis/EBV ladder page and source pages for Klein et al. 1968, Nye and Lambert 1973, and Hallee et al. 1974, separating EBV-linked immunofluorescence, EBV antibody, case/contact serology, prospective seroconversion, EBV-specific IgM, clinical IM, inapparent EBV infection, mono-like illness boundaries, and unresolved purified-virus sufficiency and route-specific transmission rungs.

## [2026-05-31] update | Burkitt lymphoma EBV evidence ladder pass
Added a Burkitt lymphoma/EBV ladder page and source pages for Henle and Henle 1965, Epstein et al. 1965, and Nonoyama et al. 1973, separating derived-cell viral-interference behavior, cultured-cell virus-like particles, negative biological recovery attempts, tumor-tissue EBV DNA detection, comparison-tumor boundaries, and unresolved necessity, sufficiency, tumor-initiation, ordinary-transmission, and cofactor rungs.

## [2026-05-31] update | Rabies evidence ladder pass
Added a rabies/rabies-virus ladder page and source pages for Goodpasture 1925, Dawson 1941, Matsumoto 1963, Hummeler et al. 1967, Miyamoto and Matsumoto 1967, Charlton and Casey 1979, and Shirakawa et al. 2007, separating artificial masseter inoculation, neural-spread pathology, chick-embryo propagation, infected-brain morphology, tissue-culture replication, street/fixed strain differences, oral/nasal route boundaries, and unresolved ordinary bite-transmission, human clinical-causation, and post-exposure-prophylaxis rungs.

## [2026-05-31] update | Measles evidence ladder pass
Created full-text source pages and a synthesis ladder for failed blood inoculation, respiratory-material monkey challenge, pathology endpoints, tissue-culture isolation, serology, plaque assay, and ordinary-transmission limits.

## [2026-05-31] update | Smallpox evidence ladder pass
Created full-text source pages and a synthesis ladder for nonhuman-primate variolation, mouse nasal-route and lung-recovery boundaries, egg propagation and stability, monkey contact/aerosol transmission, simian-reservoir limits, and ordinary-human-transmission gaps.

## [2026-05-31] update | Hepatitis A evidence ladder pass
Created full-text source pages and a synthesis ladder for CR326 marmoset propagation, human-serology neutralization, particle characterization, infected-liver localization, noncytopathic cell-culture propagation, and full-text acquisition gaps for acute-stool IEM and chimpanzee challenge/tissue-shedding papers.

## [2026-05-31] update | SARS evidence ladder pass
Created full-text source pages and a synthesis ladder for SARS-CoV patient association, culture/isolation, EM, RT-PCR, serology, multicentre comparison, cynomolgus macaque challenge, lung pathology, viral localization, partial re-isolation, and artificial combined-route animal-model limits.
## [2026-05-31] update | MERS -> MERS-CoV evidence ladder
Created source pages for Zaki et al. 2012, de Wit et al. 2013, and Adney et al. 2014; added [[synthesis/mers-mers-cov-evidence-ladder]]; updated the virus attribution worklist, evidence-ladder synthesis, inferential-leap page, failed-attempt register, and manuscript to keep index-case isolation, macaque challenge, and camel shedding endpoints separate.
## [2026-05-31] update | HFMD -> enteroviruses evidence ladder
Created source pages for Alsop et al. 1960, Brown and O'Leary 1974, Ishimaru et al. 1980, and Li et al. 2014; added [[synthesis/hand-foot-mouth-disease-enteroviruses-evidence-ladder]]; updated the attribution worklist, evidence-ladder synthesis, inferential-leap page, failed-attempt register, and manuscript to separate Coxsackie A16 lesion isolation, Coxsackie A16 serology, EV71 outbreak/CNS association, and tree-shrew model endpoints.
## [2026-05-31] update | Rotavirus and norovirus gastroenteritis evidence ladders
Created source pages for four rotavirus papers and four norovirus papers; added [[synthesis/rotavirus-gastroenteritis-evidence-ladder]] and [[synthesis/norovirus-gastroenteritis-outbreaks-evidence-ladder]]; updated the worklist, cross-cutting ladder, inferential-leap page, failed-attempt register, and manuscript to keep tissue antigen, clinical association, human challenge, culture, outbreak, PCR-shedding, and enteroid-replication endpoints separate.
## [2026-05-31] update | RSV bronchiolitis evidence ladder
Created source pages for Chanock et al. 1957, Chanock and Finberg 1957, Cradock-Watson et al. 1971, Prince et al. 1978, and Hall et al. 1981; added [[synthesis/bronchiolitis-rsv-evidence-ladder]]; updated the worklist, cross-cutting ladder, inferential-leap page, failed-attempt register, and manuscript to separate early isolation, serology/epidemiology, diagnostic bronchiolitis association, cotton-rat pathology, and adult route-inoculation endpoints.
## [2026-05-31] update | HSV and VZV evidence ladders
Created started ladder pages for cold sores/HSV-1, genital herpes/HSV, and shingles/VZV reactivation; added source pages for HSV-1 oral shedding, HSV-1 UV-reactivation, HSV-1 intensive shedding, genital HSV lesion culture, genital HSV asymptomatic reactivation and shedding, genital HSV-1 shedding, asymptomatic genital transmission, and VZV ganglionic latency/reactivation papers; linked the pages into the worklist, evidence-ladder synthesis, inferential-leap page, failed-attempt register, and manuscript.

## [2026-10-01] query | Source-gap inventory and next steps
Read the index, log, attribution worklist, failed-attempt register, and raw/ inventory. Found un-ingested raw material (raw/reprocrisis Nature 2016 survey, HPV vaccine evidence review PDF, purification essay, Speciation, Vaccine Clips), already-named full-text acquisition gaps (hepatitis A/B/C, SARS, AIDS boundary set, HPV boundary set, rabies route set, polio 1910/1951 candidates), structural gaps (replication-crisis anchors, one-page comparison layer, entity pages resting on Tier 3 commentary, unresolved Gutknecht Q4-6 and Q10-12), and a stale wiki/index.md (117 pages listed vs about 230 on disk).

## [2026-10-01] ingest | Replication-crisis anchors ingested and concept rebuilt
Ingested raw/reprocrisis (Baker, Nature 2016 researcher survey) and created source pages for the Open Science Collaboration 2015 psychology replication project (PMID 26315443) and the Begley-Ellis 2012 preclinical-cancer commentary (PMID 22460880, marked unresolved as a non-inspectable commentary). Rebuilt [[concepts/replication-crisis]] from exploratory to anchored, keeping the three anchors' evidentiary limits distinct.

## [2026-10-01] ingest | CIDRAP 2026 HPV vaccine systematic review
Created [[sources/cidrap-2026-hpv-vaccine-evidence-review]] from the full 104-page PDF in raw/ (PROSPERO CRD420261300907; 274 studies including the 2025 Cochrane RCT and observational reviews). Updated [[synthesis/cervical-cancer-hpv-evidence-ladder]] to start its intervention rung with RCT CIN2+ endpoints (RR 0.39), pooled observational cancer/CIN3+ outcomes, Cochrane-certainty safety findings, one mixed POTS outcome, and the unresolved one-vs-two-dose margin.

## [2026-10-01] ingest | HPV boundary set extracted (10 abstract-level source pages)
Created abstract-level source pages for Kaliff 2020, Rodriguez-Carunchio 2015, Petry 2017, Arroyo Muhr 2020 (both sequencing papers; correcting the register's "Lagheden" attribution), Caussy 1988, Claas 1989, McCance 1983, Peto 2004 (Manchester cohort), and Skinner 2016 (VIVIANE control arm), and rewrote the HPV candidate list in [[synthesis/failed-virus-causation-attempts-register]] with links.

## [2026-10-01] ingest | AIDS boundary set extracted (7 source pages)
Created pages for Alter 1984 (chimpanzee plasma transmission without AIDS syndrome), the CDC 1984 MMWR LAV-chimpanzee report (extracted from the CDC archive), Fultz 1987 (persistent infection), Learmont 1992 (single-donor nonprogression, 1/6 vs 94/101), Smith 1993 and Spira 1993 (idiopathic CD4 lymphocytopenia; correcting the register's "Ho" attribution), and Novembre 1997 (AIDS development in a chimpanzee after ten years, as comparator). Rewrote the AIDS section of the register with links.

## [2026-10-01] ingest | Rabies route set and hepatitis/SARS gap papers
Created rabies route pages for Davis 2007 (aerosol: mice died, bats survived with poor challenge protection) and Ramsden-Johnston 1975 (oral infection did occur in foxes and skunks), plus a pointer page for Bell-Moore 1971 (no abstract or free text obtainable); noted the register's Charlton 1979 "candidate" was already extracted in the May pass. Created five hepatitis A records (Feinstone 1973, Dienstag 1975, Schulman 1976, Thornton 1977, Maynard 1975), three hepatitis B pointer pages (Dane 1970, Maynard 1972, Barker 1973 - no indexed abstracts), two hepatitis C records (Tabor 1984 two-agent chimpanzee passage; Hong 1999 transmissible molecular clone), and three SARS records (Ksiazek 2003, Rota 2003, Fouchier 2003). All marked abstract-level or pointer-level; updated the hepatitis A/B/C and SARS ladder pages, the register, and the worklist to keep "abstract-level in hand, full-text still needed" boundaries explicit.

## [2026-10-01] create | Second comparison page
Added [[comparisons/ladder-standard-vs-revisionist-virus-causation-critique]] mapping the dispute structure between the vault's rung-separated ladder standard and the Tier 3 revisionist critique, with symmetric inferential-error warnings and both supporting and critical sources linked.

## [2026-10-01] lint | Index regenerated and lint cleanup
Regenerated wiki/index.md (117 to 271 pages). Ran scripts/lint_wiki.py: added missing frontmatter to six hub pages and six older Tier 3 source pages, added a Main limitations section to [[concepts/replication-crisis]] for its supported status, and linked the new comparison page from the register and worklist. Remaining lint notes are pre-existing structural items (hub-page orphans and the wiki.md index/log link resolution).

## [2026-10-01] update | Vault-wide formatting and navigation pass
Normalizing pass across all 271 wiki pages, content-preserving only. Frontmatter: replaced folded-scalar (`>-`) titles/summaries with single-line values, converted ISO timestamps to plain dates, quoted six pages whose titles contained colons and had been broken by the ai-tagger plugin into doubled frontmatter blocks (original values restored, duplicate blocks removed), sorted tags, and emitted keys in a canonical order. Body: converted 117 `> Note:`/`> Warning:` blockquotes to Obsidian callouts (`[!note]`/`[!warning]`), unified heading variants (Related pages→Related, API abstract→Indexed abstract, Source type and scope→Source type, What this source can answer→What the source can answer, What this wiki can conclude→What this wiki currently concludes), and stripped trailing whitespace. Navigation: rewrote scripts/update_index.py (robust frontmatter parsing, clean dates, entry-points section, and the 207 source pages grouped into 14 topic clusters instead of one flat alphabetical list) and regenerated wiki/index.md; replaced the five empty folder-index stub maps (concepts, entities, sources, comparisons, synthesis) and the stale wiki.md app:// dump with real curated navigation pages; updated .templates/source-summary.md to the canonical source-page structure; documented the callout convention in AGENTS.md. Added scripts/normalize_formatting.py to make the pass rerunnable. Lint is now clean: 0 broken links, 0 orphans, 0 missing frontmatter. `updated:` dates were reformatted but not advanced, since no page content changed.

## [2026-10-08] lint | Wikilink normalization and stale-link repair
Added scripts/normalize_links.py and rewrote 734 bare-basename wikilinks to full-path links across all wiki pages, so links resolve unambiguously outside Obsidian and lint_wiki.py can verify them. Manually repaired the 12 links the script could not resolve: six raw-title links in the vault-operator table of [[entities/viroliegy]] (now full-path links with the title kept as alias) and six stale bare [[empirical-evidence]] links in concept incoming-links tables (now [[concepts/empirical-evidence]]). Lint went from 746 broken links to 0. Regenerated wiki/index.md.

## [2026-10-08] ingest | Three remaining un-ingested raw files
Created Tier 3 triage source pages for the last raw files without wiki pages: [[sources/speciation-direct-evidence-ai-chat]] (AI-chat on what would count as direct speciation evidence; leads recorded as to-verify, model-generated citations flagged), [[sources/vaccine-clips-research-lead]] (stub research lead on the prevention-vs-health-benefit inference), and [[sources/is-complete-purification-isolation-of-a-virus-even-possible]] (ViroLIEgy purification essay; isolation-definition and exosome-overlap questions marked unresolved, PMC6972601 named as a verification lead). Cross-linked from [[concepts/inferential-leap]], [[concepts/virus-isolation]], and [[comparisons/disease-prevention-vs-health-outcomes]]; added a Research leads and vault meta section to the source map; corrected the now-false "not yet promoted" line on [[concepts/empirical-evidence]].

## [2026-10-08] update | Entity pages wired to the vault's experimental record
Deepened all six entity pages ([[entities/edward-jenner]], [[entities/louis-pasteur]], [[entities/robert-koch]], [[entities/paul-feyerabend]], [[entities/rene-dubos]], [[entities/mike-stone]]) with Related source pages sections that separate the experimental record from commentary and critique, dispute pairs linked both ways (e.g. Fouchier 2003 Koch's-postulates claim vs Rivers 1937 revision), explicit open questions naming what primary evidence is still missing, and corrected sources: counts. Feyerabend and Dubos now state plainly that the vault holds no primary or Tier 1/2 text for them.

## [2026-10-08] update | Thornton 1977 upgraded to full text
Obtained the full text of Thornton, Tsiquaye, and Zuckerman 1977 (Br J Exp Pathol) from the seven PMC2041211 page images (scanned article, no text layer; Europe PMC fullTextXML 500s). Upgraded [[sources/thornton-1977-human-hepatitis-a-chimpanzees]] to full-text depth and claim_status supported at the chimpanzee-inoculation rung: 18/23 seronegative chimpanzees developed hepatitis across three human HAV sources, 27-nm particle shedding in 2 animals (days 9-19, density mostly 1.34 g/ml), antibody during incubation, four uninoculated controls well, hepatitis-B markers excluded. Updated the hepatitis A ladder accordingly; Thornton now anchors the chimpanzee rung at full-text strength. Bulk-checked the other five candidates (Hong 1999, Dienstag 1975, Schulman 1976, Ksiazek 2003, Rota 2003) against Europe PMC: none open access, no PMCIDs — their pages correctly remain abstract-level.

## [2026-10-16] ingest | Nordvall 2026 COVID-19 vaccination and childbirth (paper + deposited R code)
Created [[sources/nordvall-2026-covid-vaccination-childbirth-sweden]] from the full text (Europe PMC PMC13310814), Supplementary Materials (Tables S1-S5), the transparent peer-review file, and the deposited analysis script (Zenodo 10.5281/zenodo.18138478 v1.0; the user-supplied copy is byte-identical). Evidence fields name the registry cohort design, dose-2 time-varying exposure, the delivery-minus-280-day index endpoint, recorded-miscarriage endpoint, and Table S4/S5 results, including sensitivity estimates whose intervals exclude 1 that the abstract does not carry. Marked claim_status unresolved: observational, age-only adjustment, no replication in the vault, and the deposited code does not regenerate the published analyses as written.

## [2026-10-16] create | Nordvall 2026 analysis script audit
Created [[synthesis/nordvall-2026-script-audit]] with R code under wiki/synthesis/nordvall-2026-script-audit/ (audit_common.R, synthetic_audit.R, registry_audit.R, results/). It answers three requested checks: tmerge() use and risk-set entry; fixed 280/266-day offsets versus gestational-age-based index dates; row counts and NA handling through the miscarriage filters. The authors' own lines were run verbatim on a synthetic registry laid out like the script's inputs, and compared row by row with a survival::tmerge() rebuild. Registry data were not available, so data-level magnitudes remain unknown; registry_audit.R is provided for authorised data holders. Cross-linked from [[concepts/inferential-leap]], [[concepts/replication-crisis]], [[concepts/clinical-endpoints]], and the synthesis and sources hubs.

## [2026-11-10] create | Source verification queue and first verification run
Created [[synthesis/source-verification-queue]] from the 11-item virology shortlist (GAP 1-5), with per-item status. Attempted queue items 1, 2, 4, and 5 with Crossref, Europe PMC, web search, and publisher/PMC fetches. None returned full text, so all four are marked `unverifiable` with one-line reasons: Couch 1966 JAMA not indexed; Cody/Wright RSV primary paper not located; Cowling 2009 and Herlocher 2004 subscription-only (publisher 403). Noted leads: Couch et al. 1966 Bacteriological Reviews (PMC378233, route of inoculation in volunteers, full text blocked here) and Cutts 2005 (filed as [[sources/cutts-2005-pcv9-gambia-rct]]; shortlist's "Cutland" appears to be a name error). No sources pages written; no existing conclusions changed. Index gained one synthesis entry.

## [2026-11-10] ingest | Memoli 2015 and Han 2021 — controlled human challenge for A(H1N1)pdm09 (queue item 3, GAP 1)
Fetched both full texts from PMC HTML (Europe PMC fullTextXML 500s; OUP robot-blocked) and wrote [[sources/memoli-2015-h1n1pdm09-human-challenge-model-validation]] (Clin Infect Dis 2015;60(5):693 ff., PMC4342672: dose-escalation challenge, 46 adults, GMP wild-type A/California/04/2009(H1N1), MMID endpoint = shedding + >=1 symptom, 69% MMID at 10^7 TCID50, 0% shedding at 10^3-10^4, no sham arm) and [[sources/han-2021-cr6261-placebo-controlled-h1n1pdm09-challenge]] (Clin Infect Dis 2021;73(11):e4260-e4268, PMC8664469: randomized double-blind placebo-controlled CR6261 trial, 91 challenged; virus-only placebo arm 69% MMID, 88% confirmed infection, 93% symptoms, 74% shedding; CR6261 no significant effect on viral RNA AUC, P=.315; baseline anti-NA titer the only disease predictor). Together they fill queue item 3 / GAP 1 (sham-controlled human challenge with purified inoculum) for influenza. Marked inferential leaps: shedding-before-symptoms read as possible pre-symptomatic infectiousness (no recipients tested); one anti-stalk mAb result generalized to anti-stalk immunity. Influenza ladder gained a rung-7 row (sources 4->6); cross-cutting ladder gained the influenza challenge note. Item 6 (Seattle Virus Watch) was claimed, released unfetched — the run's two-paper budget went to the item 3 pair.

## [2026-11-10] note | Source verification queue run 3 — one reconciliation, five unreachable
Worked queue items 6-11. No new sources pages: OUP, NEJM, AJPH, and ResearchGate are Cloudflare-hard for this sandbox (curl, r.jina.ai, and the sandbox browser all blocked), web.archive.org was in an outage for most of the run, and scholar.archive.org was rate-limited all run. Item 8 reconciled to `done`: the shortlist's "Cutland" is a name error; the primary paper is Cutts FT et al., Lancet 2005;365(9465):1139-46, and [[sources/cutts-2005-pcv9-gambia-rct]] already carries full-text-grade fields (arms, named endpoints, per-protocol and ITT results). Items 6 (Hall/Cooney/Fox AJE 1973 Seattle Virus Watch IV), 7 (Monto/Koopman/Longini AJE 1985 Tecumseh XIII), 9 (Vesikari NEJM 2006), 10 (Garland FUTURE II NEJM 2007), and 11 (second-lab measles re-isolation: Ruckle & Rogers, J Immunol 1957;78:341-355) are marked `unverifiable` with exact citations and retry leads recorded in [[synthesis/source-verification-queue]]. GAP 3 still has no verified rung; GAP 4 has one (Cutts 2005). No existing conclusion changed.

## [2026-11-10] ingest | Vesikari 2006 REST — placebo-controlled disease-endpoint vaccine trial for rotavirus (queue item 9, GAP 4)
Wayback (recovered this run) holds the full HighWire HTML of Vesikari et al. 2006 (NEJM 354:23-33, REST trial, Merck V260-006) at content.nejm.org/cgi/content/full/354/1/23; read end to end and filed as [[sources/vesikari-2006-pentavalent-rotavirus-rest-rct]]: randomized double-blind placebo-controlled trial, 68,038 infants dosed (34,035 vaccine / 34,003 placebo, "visibly indistinguishable placebo"), endpoints named exactly (confirmed intussusception within 42 days; G1-G4 rotavirus gastroenteritis >=14 days after dose 3 by EIA case definition; severity-score >16 severe disease; hospitalization/ED/clinic use; IgA seroconversion). Results: 74.0% efficacy any severity (95% CI 66.8-79.9), 98.0% severe (95% CI 88.3-100) per-protocol first season; hospitalization/ED reduction 94.5%; intussusception adjusted RR 1.6 (95% CI 0.4-6.4); all-cause mortality 24 vs 20, no efficacy analysis. Inferential leaps recorded: global mortality framing without a rotavirus-death endpoint; "not all rotavirus vaccines are associated with intussusception" stated from a CI compatible with a small increase; disease-specific health-care figures. GAP 4 now has two anchors (Cutts 2005 all-cause; Vesikari 2006 disease-endpoint). Rotavirus ladder gained an intervention row; [[synthesis/specific-vaccine-overall-health-outcome-evidence]] gained an iteration separating REST's target-disease evidence from the all-cause proof; attribution worklist row updated. Items 6 and 11 re-attempted (IA up: item 11 reprint snapshot is a Sign In page; item 6 has no article-level snapshots; scholar.archive.org serves a JS shell) — both remain `unverifiable`. No existing conclusion changed.

## [2026-11-10] ingest | FUTURE II 2007 — quadrivalent HPV vaccine RCT with disease endpoint (queue item 10, GAP 4)
Fetched and read the full 2007 HighWire HTML of The FUTURE II Study Group (NEJM 356:1915-1927, PMID 17494925, DOI 10.1056/NEJMoa061741, NCT00092534) from Wayback snapshots of content.nejm.org/cgi/content/full/356/19/1915 and wrote [[sources/future-ii-study-group-2007-quadrivalent-hpv-cin2-rct]]. Evidence fields: phase 3 randomized double-blind placebo-controlled trial, 12,167 women 15-26 (6087/6080), quadrivalent HPV-6/11/16/18 VLP vaccine vs "a visually indistinguishable aluminum-containing placebo" (AAHS — sham arm yes, not inert, quote preserved); endpoint named exactly (CIN grade 2/3, AIS, or invasive cervical carcinoma with HPV-16/18 DNA in ≥1 of 3 adjacent lesion sections, blinded 4-pathologist consensus, WHO criteria); results 98% VE per-protocol susceptible (1 vs 42), 95% unrestricted susceptible, 44% ITT type-specific, 17% ITT any-type, zero cancers in either arm, vaccination does not alter prevalent infection/lesions. Name reconciled: "Garland" in the queue is FUTURE I (anogenital diseases); the queue item's paper is the Study Group paper. Inferential leaps recorded: precursor-lesion-to-cancer extrapolation, susceptible-population quoting risk, adjuvant-matched safety comparisons, nonsignificant cross-type subgroup sentences. HPV intervention rung of [[synthesis/cervical-cancer-hpv-evidence-ladder]] upgraded from review-started (CIDRAP 2026) to primary-paper-anchored; [[synthesis/viral-disease-causation-evidence-ladder]] HPV note updated; [[synthesis/virus-disease-attribution-audit-worklist]] cervical-cancer row updated; [[synthesis/specific-vaccine-overall-health-outcome-evidence]] gained iteration 5 (target-lesion evidence, non-inert placebo, not all-cause proof); the placebo-composition audit row for PMID 17494925 in [[sources/pediatric-vaccine-trial-records-placebo-control-audit]] resolved from full text. Items 11 (Ruckle & Rogers 1957) and 6 (Hall/Cooney/Fox 1973) re-attempted with a fully functional CDX and remain `unverifiable`; item 6's DOI corrected to 10.1093/oxfordjournals.aje.a121566 (the a112125 DOI in older notes is Seattle Virus Watch VI). GAP 3 still has no verified rung; queue "next run" guidance rewritten with the general HighWire-Wayback CDX pattern. Index and sources map regenerated. No existing conclusion changed.

## [2026-11-10] ingest | Cowling 2009 household RCT and DeVincenzo 2010 + Byrne 2026 RSV challenge pair (queue items 4 and 2, GAP 2 anchor + GAP 1 RSV half)
Fetched and read the full HighWire HTML of Cowling et al. 2009 (Ann Intern Med 151(7):437-446, PMID 19652172, DOI 10.7326/0003-4819-151-7-200910060-00142, NCT00425893) from archived annals.org captures (2009 full/abstract and 2012 full; numbered tables not archived, per-arm estimates taken from narrative) and filed [[sources/cowling-2009-household-facemask-hand-hygiene-rct]]: cluster-randomized 1:1:1 household trial in Hong Kong (407 randomized, 259 households/794 contacts analyzed), control arm "control (lifestyle measures)" quoted, primary endpoint named exactly (secondary attack ratio via RT-PCR-confirmed contact infection, nasal+throat swabs), results 60/794 (8%) infected, household-level SAR 24%/14%/18% (P=.37), no significant difference as randomized, prespecified within-36-hours subgroup facemask+hygiene aOR 0.33 (95% CI 0.13-0.87); limitations and leaps recorded (subgroup elevated to abstract conclusion; pandemic-mitigation generalization; control contamination, ~50% mask adherence). GAP 2 (controlled natural-route transmission) now has a human influenza anchor; the influenza ladder gained a natural-route row and the cross-cutting ladder an influenza note. Item 2 done: "Cody/Wright" could not be identified in PubMed/Europe PMC (probable name error, pattern of items 8/10); verified the identifiable adult RSV challenge primaries as a two-paper set mirroring item 3 - [[sources/devincenzo-2010-rsv-human-challenge-model-validation]] (AJRCCM 2010;182(10):1305-1314, PMC3001267: GMP wild-type RSV-A Memphis 37 dose-escalation across ~3.0-5.4 log10 PFU, 27/35 (77%) infected by qPCR, viral load correlated with symptom/DPE/mucus endpoints, P<0.0001; no sham arm, recorded explicitly; leap flagged: "viral load drives disease" causal language and infant extrapolation) and [[sources/byrne-2026-s337395-placebo-controlled-rsv-challenge]] (CID 2026;83(3):e652-e660, PMC13644856, DOI 10.1093/cid/ciag367: randomized double-blind placebo-controlled S-337395 trial in the Memphis 37b model, 114 inoculated, 60 (53%) infected; primary endpoint VL-AUC by qRT-PCR; 300 mg -88.94% VL-AUC, -78.15% TSS-AUC vs placebo, no serious AEs; placebo controls the drug, not inoculation - recorded). RSV ladder gained two challenge rows; cross-cutting ladder gained an RSV note. Item 5 (Herlocher 2004 ferret transmission, JID 190(9):1627-1630) re-exhausted: bronze OUP PDF Cloudflare-403 twice, Wayback 302-only, uchicago legacy URL now JSTOR-redirected, fatcat timeouts, OpenAIRE instances all publisher/403; remains `unverifiable`. Items 6, 7, 11 untouched and still `unverifiable`. No existing conclusion changed; index regenerated.

## [2026-11-10] ingest | Couch et al. 1969 Nature letter - equine influenza syndrome produced in man (run-7 lead, queue item 14)
The run-7 lead ("Couch, R. B., Douglas, R. G., Jr, Kasel, J. A., Riggs, S., & Knight, V. (1969) Nature (Lond.) (in press)", cited on [[sources/kasel-couch-1969-experimental-infection-man-horses-influenza]] for the human inoculation procedures) was identified via Crossref as Couch RB, Douglas RG Jr, Kasel JA, Riggs S, Knight V, "Production of the Influenza Syndrome in Man with Equine Influenza Virus", Nature 1969;224(5218):512-514, DOI 10.1038/224512a0 (not PubMed-indexed; no PMID). Full scanned PDF (5.07 MB) retrieved from the 2022-10-15 Wayback capture of nature.com/articles/224512a0.pdf (application/pdf, HTTP 200) and read end to end in OCR; Table 1 and the "A/equi-2/Miami/1/68" strain-name sentence verified visually from 200-dpi page images. Filed as [[sources/couch-1969-nature-equine-influenza-syndrome-man]]. Evidence fields: single-arm experimental human challenge (no sham/placebo group - recorded explicitly); fifteen antibody-free prisoner volunteers, health established and written consent obtained, November 1968; 2 mL undiluted inoculum (passage egg5 HK2 man1 HK4 man1 HK3, stored at -70 degrees C since 1965, aliquot shown free of extraneous viruses) by nasal instillation and Devilbiss No. 127 spray, administered dose 10^6.7 TCID50 by simultaneous RhMK titration; endpoints virus recovery (throat swab/gargle days 0-6, 8, 10, 11 in RhMK), four-fold-or-greater neutralizing antibody (haemadsorption-inhibition, 32 TCID50, 4-week sera), physician-observed illness twice daily classified as febrile URI/LRI/systemic categories; results virus recovered from 15/15 (mean 5 positive specimens, 3.3 positive days), seroconversion 14/15, illness 13/15 on day 2-3 (Table 1: 2 febrile URI+LRI+systemic, 8 febrile URI+systemic, 3 afebrile URI, 2 no illness), heterologous A2/Hong Kong rise 9/15 (Spearman r=0.4, P<0.05), fever shorter (mean 1.3 days) than textbook natural-influenza descriptions; March 1965 pilot (6 men, 10^5.3 TCID50): shedding 4/6, antibody 5/6, no illness - a within-lab dose-associated illness contrast. Recorded as printed: narrative text calls the three URI-only cases febrile while Table 1's row is "Afebrile URI" (13/15 ill either way); the printed strain name Miami/1/68 conflicts with the letter's own 1963 isolation date and the companion Bulletin's A/Equi-2/Miami/63; the dose here (10^6.7) differs from the Bulletin's 10^8.75 for the same-looking trial - flagged, not resolved. Leaps recorded: "typical human influenza" (textbook comparison, no natural-case arm) and the closing claim that the result "lends credence to the possibility that ... equines ... might contribute to the emergence of new variants of human influenza" (no natural transfer, reassortment, or emergence observed - inoculation experiment only); abstract's "Hong Kong variant was derived from the equine virus" is serologic-relationship inference (Coleman et al.), not an experiment in this letter. [[synthesis/influenza-influenza-virus-evidence-ladder]] rung 7 extended (sources 10 to 11); [[synthesis/viral-disease-causation-evidence-ladder]] influenza challenge note extended; [[sources/kasel-couch-1969-experimental-infection-man-horses-influenza]] lead resolved and cross-linked. Queue: items 6 and 7 re-attempted with IA back online and re-exhausted with citation corrections (item 6 issue number corrected to 98(5); corrected-URL CDX probing finds only the 2016 .short abstract page; item 7's CDX hits are 301/302 redirects resolving to the OUP article-abstract page, no full text ever crawled; fatcat still down) - both remain `unverifiable`; abstracts alone do not meet the standard. Item 11 untouched (route-exhausted per run 7). No existing conclusion changed; index regenerated.

## [2026-11-10] ingest | Kasel & Couch 1969 Bull WHO controlled human influenza challenge (queue item 1, GAP 1 reconciliation)
Queue item 1's citation ("Couch et al. 1966, JAMA - experimental influenza, egg-grown inoculum vs placebo") proven nonexistent: PubMed holds nine Couch 1966 publications, none in JAMA, and Crossref's 1966 JAMA influenza-title set contains only a news item and editorials (same name/journal-error pattern as items 8/10). Couch's real 1966 volunteer paper - Couch, Cate, Douglas, Gerone, Knight, "Effect of route of inoculation on experimental respiratory viral disease in volunteers and evidence for airborne transmission", Bacteriol Rev 30(3):517-529, PMC378233 - was retrieved in full text this run via a solved PMC proof-of-work cookie (SHA-256 pow challenge) and verified NOT to be the item: coxsackievirus A21, rhinovirus NIH 1734, and adenovirus type 4 route comparisons in antibody-free volunteers, tissue-culture inocula, no influenza, no placebo/sham arm. The nearest Couch-authored controlled human influenza challenge with reachable full text was verified end to end from the WHO IRIS scan and OCR (handle 10665/262509, PMC2427734): Kasel JA & Couch RB, "Experimental Infection in Man and Horses with Influenza A Viruses", Bull WHO 1969;41:447-452, PMID 5309454, filed as [[sources/kasel-couch-1969-experimental-infection-man-horses-influenza]]. Evidence fields: 15 seronegative adult male volunteers (21-35 y, written informed consent documented) inoculated with 10^8.75 TCID50 A/Equi-2/Miami/63 (passage egg5,HK2,man1,HK4,man1,HEK3 - not purely egg-grown, recorded): illness 13/15, shedding 15/15, seroconversion 14/15; simultaneous 19-person unimmunized control group on the 10^3.2 TCID50 A2/Hong Kong/68 challenge: illness 1/15 vs 9/19 (P<0.06), isolate distribution P<0.05, >=4-fold rise 4/15 vs 14/19; protection tracked heterologous antibody tier (infection 4/6, 2/5, 0/4; P<0.05 Yates). Sham arm: no (recorded explicitly on the page; no placebo quote exists in the paper). Leaps recorded: "indistinguishable from naturally occurring human influenza" rests on textbook clinical comparison (Stuart-Harris), not a natural-case arm; surveillance and interspecies-exchange sentences extrapolate beyond the experiments. Influenza ladder rung 7 gained its earliest full-text row; [[synthesis/viral-disease-causation-evidence-ladder]] influenza note extended. Item 11 (second-lab measles re-isolation) re-exhausted - fatcat API timed out again, OpenAlex shows no OA locations for Ruckle & Rogers 1957, archive.org 'sim' collection has no J Immunol volume 78 scans, WHO IRIS holds no early measles-isolation paper, Europe PMC measles-isolation title search 1954-1970 returns only closed Science papers and BMJ news notes - remains `unverifiable` with route history updated. Lead left for future runs: Couch/Douglas/Kasel/Riggs/Knight, Nature 1969 (in press), the A2/Hong Kong/68 human inoculation-methods paper cited in the Kasel & Couch reference list. GAP 3 (items 6/7) untouched this run and still `unverifiable`. No existing conclusion changed; index regenerated.

## [2026-11-10] ingest | Kim 2012 Kenya PBIDS household cohort and Lowen 2007 cage-separated guinea-pig transmission (queue items 12 and 13: GAP 3 anchor + GAP 2 animal half)
The four remaining queue candidates (5, 6, 7, 11) remained unreachable this run - Internet Archive was offline all run (CDX/Wayback down), OUP bronze is Cloudflare-403 to curl and to the real browser (challenge loops, no Turnstile iframe surfaced), r.jina.ai CAPTCHA-blocked, hub.hku.hk Cloudflare-challenged in the browser, Unpaywall/OpenAlex report closed with no repository copies, HathiTrust's API rejects ISSN queries, Google Scholar 403 - so items 5 and 6 returned to `unverifiable` with run-8 route notes, and GAP 3/GAP 2-animal were filled by two fully open substitutes added to the queue as items 12 and 13. Item 12: Kim CY, Breiman RF, et al., "Secondary Household Transmission of 2009 Pandemic Influenza A (H1N1) Virus among an Urban and Rural Population in Kenya, 2009-2010", PLoS ONE 2012;7(6):e38166, PMID 22701610, DOI 10.1371/journal.pone.0038166, PMC3372521, filed as [[sources/kim-2012-kenya-household-pdm09-transmission-cohort]] from the complete Europe PMC full text, including the published Correction (PMC3966769, Table 4 row swap; PMC text carries the corrected values). Evidence fields: prospective PBIDS cohort (biweekly/weekly household morbidity visits), 115 (Kibera) + 66 (Lwak) RT-PCR-confirmed pH1N1 index patients, comparator is 4 randomly selected comparison households per case household matched by children <5 with a same-window interview ("Comparison households did not have laboratory-confirmed pH1N1 cases..." quoted), secondary endpoint named exactly (laboratory-confirmed pH1N1 infection or ILI within <=8 days of index onset; ILI = self-reported cough or sore throat plus self-reported fever), results 27/584 (4.6%) vs 62/2,272 (2.7%) RR 1.8 (1.1-2.8) in Kibera and 29/352 (8.2%) vs 43/1,289 (3.3%) RR 2.6 (1.6-4.3) in Lwak, serial interval 4.0/3.2 d, corrected Table 4 (Lwak <5y 22.5% vs 5.9%, RR 3.8); authors' own limitation quoted (self-reported ILI secondary cases, cannot distinguish household from outside acquisition, 28-26% of confirmed index infections would not have met the ILI definition); leap recorded (abstract names "pH1N1 household transmission" beyond the timed-ILI endpoint). This is the vault's first full-text GAP 3 row, standing in for the still-unreachable Seattle Virus Watch IV (item 6) and Tecumseh XIII (item 7). Item 13: Lowen AC, Mubareka S, Steel J, Palese P, "Influenza Virus Transmission Is Dependent on Relative Humidity and Temperature", PLoS Pathog 2007;3(10):e151, PMID 17953482, DOI 10.1371/journal.ppat.0030151, PMC2034399, filed as [[sources/lowen-2007-guinea-pig-humidity-temperature-transmission]] from complete full text: 20 duplicate experiments, donors intranasal 10^3 PFU A/Panama/2007/99 (H3N2), recipients behind wire grids ("the guinea pigs cannot come into physical contact with each other" quoted), no sham-inoculation arm (recorded explicitly; negative contrasts are 0/4 at 20C/80% RH and 0/4 at 30C/35% RH), endpoints plaque-assay nasal-wash titers (day 2 to day 12 p.i.) plus HI seroconversion, transmission 3-4/4 at 20% and 35% RH, 1/4 at 50%, 3/4 at 65%, 0/4 at 80% RH at 20C; 75-100% at 5C/35-50% RH; mechanism extended peak shedding (3.93 vs 2.21 days >=10^6 PFU/ml, p<0.0005); no disease endpoint (model asymptomatic) and the "weather conditions in the dynamics of influenza" conclusion flagged as the authors' epidemiological extrapolation. This fills the animal half of GAP 2 left open by the unreachable Herlocher 2004 ferret paper (item 5, re-exhausted again). [[synthesis/influenza-influenza-virus-evidence-ladder]] gained a controlled-animal-natural-route rung and a prospective-household-cohort rung (sources 8 to 10); [[synthesis/viral-disease-causation-evidence-ladder]] influenza notes extended (sources 121 to 123). Items 7 and 11 untouched and remain `unverifiable`. No existing conclusion changed.
