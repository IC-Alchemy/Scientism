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
