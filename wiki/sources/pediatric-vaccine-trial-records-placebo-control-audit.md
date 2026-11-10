---
title: Pediatric Vaccine Trial Records Placebo-Control Audit
category: source
summary: Abstract-level audit of vaccine clinical-trial records cited by the CHD placebo-control article, focused on comparator type and endpoint scope.
tags:
  - abstract-metadata
  - clinical-trials
  - comparator-choice
  - pediatric-trials
  - pediatric-vaccines
  - placebo-controls
  - safety
  - trial-record-audit
  - vaccine-safety
  - vaccine-trials
  - vaccines
sources: 20
updated: 2026-05-05
claim_status: exploratory
claim_type: methodological
source_tier: tier-1
---

# Pediatric Vaccine Trial Records Placebo-Control Audit

## TL;DR
Lens found all 18 PubMed-indexed trial records cited by [[sources/vaccine-makers-do-not-use-placebos-to-test-the-safety-of-their-vaccines-for-kids]]. At the abstract and metadata level, most cited trials are active-comparator vaccine trials, while several rotavirus and HPV records are placebo-labeled but do not identify the placebo composition in the abstract. This supports the narrower methodological point that comparator choice must be named before making safety claims; it does not by itself prove a general claim about all pediatric vaccine safety testing.

> [!warning] Warning
> This page is a trial-design audit, not medical advice.

## Search method
- Tool: Lens scholarly search helper, exact PMID search against the 18 trial citations preserved in the raw CHD source.
- Supplement: PubMed XML abstracts were used when Lens metadata did not expose study design, endpoints, or results.
- Boundary: This page records what the trial abstracts and metadata show. Where a placebo composition is not visible in the abstract, the comparator inertness remains unresolved until the full paper or regulatory file is reviewed.
- Counter-search: Lens keyword searches for pediatric vaccine trials with `placebo`, `saline`, `randomized`, and `safety` found additional placebo-labeled trial leads, including at least one child influenza trial with saline and excipient placebo arms.

## What question these records can answer
- They can identify the trial design, population, intervention, comparator named in the abstract, endpoints, and reported abstract-level result.
- They can show whether a cited trial was an active-comparator study, placebo-labeled study, timing/schedule study, or dose-regimen study.
- They cannot establish rare adverse-event rates, long-term net health effects, or absolute safety unless the trial design and endpoint actually measured those questions.
- They cannot prove that a placebo was inert when the abstract only says `placebo` without naming its contents.

## Comparator audit of cited trials

| PMID | Trial | Population | Design | Comparator class | Safety endpoint in abstract | Other endpoint | Abstract-level result | Placebo-control limitation |
|---|---|---|---|---|---|---|---|---|
| [8823852](https://pubmed.ncbi.nlm.nih.gov/8823852/) | Comparative safety and immunogenicity of two recombinant hepatitis B vaccines, 1996; Lens `021-797-828-729-954`; DOI `10.1097/00006454-199607000-00006` | Healthy infants vaccinated at 2, 4, and 6 months | Randomized comparative trial; blinding not visible in abstract | Active vaccine comparator: Engerix-B vs Recombivax HB | Adverse reactions by parent report, interviews, and medical-record review | Anti-HBs antibody response | Adverse reactions were mild and not significantly different; antibody responses differed earlier but both groups reached high seroprotection after dose 3 | No inert or untreated arm; answers relative safety and immunogenicity between two Hep B vaccines |
| [20173677](https://pubmed.ncbi.nlm.nih.gov/20173677/) | Two strategies for hepatitis B vaccination in healthy urban adolescents, 2010; Lens `009-718-190-128-267`; DOI `10.1097/INF.0b013e3181d285c7` | Urban adolescents aged 12 to 17 | Multicenter randomized trial | Active vaccine comparator: Recombivax HB vs Twinrix Hep A/B | Safety data collected | Hep B and Hep A antibody responses | Hep B response was 87.2% with Recombivax HB and 94.6% with Twinrix; difference was not statistically significant in the abstract | No inert placebo; comparator adds active Hep A antigen |
| [8337029](https://pubmed.ncbi.nlm.nih.gov/8337029/) | Effectiveness and safety of PRP-T Hib vaccine in young infants, 1993; Lens `197-911-848-268-955`; DOI `10.1542/peds.92.2.272` | 10,317 infants aged 6 to 15 weeks; all also received DTP | Randomized, double-blind controlled clinical trial | Active vaccine comparator: recombinant Hep B control vaccine plus DTP | 72-hour reactions, between-dose events, hospitalizations, outpatient visits, morbidity, mortality | Invasive Hib disease | Some reactions were higher with PRP-T; morbidity, mortality, and hospitalization were similar; invasive Hib cases were 0 in PRP-T vs 3 in control | Strong comparative trial, but not an inert-placebo trial |
| [9194110](https://pubmed.ncbi.nlm.nih.gov/9194110/) | COMVAX Hib/Hep B vaccine in healthy infants, 1997; Lens `063-043-230-800-19X`; DOI `10.1097/00006454-199706000-00010` | 882 healthy infants about 2 months old | Open, multicenter randomized clinical trial | Active vaccine comparator: COMVAX vs PedvaxHIB plus Recombivax HB | Safety and tolerability after injections | Anti-PRP and anti-HBs antibody concentrations | No serious adverse experiences were attributed; common diary-card events were usually mild and transient | Open-label active-comparator trial; no inert control |
| [3550021](https://pubmed.ncbi.nlm.nih.gov/3550021/) | Hib polysaccharide vs polysaccharide-diphtheria toxoid conjugate vaccines, 1987; Lens `002-050-076-072-755`; DOI `10.1016/s0022-3476(87)80540-1` | 585 children aged 15 to 24 months | Randomized comparative clinical trial; abstract unavailable in PubMed | Active vaccine comparator: PRP vs PRP-D Hib vaccines | Adverse-reaction details not available from PubMed abstract | Immunogenicity inferred from title and trial focus | Abstract-level result not available from PubMed | Both arms were active Hib vaccines according to the title and raw citation; full paper needed for endpoints and results |
| [3495775](https://pubmed.ncbi.nlm.nih.gov/3495775/) | Acellular pertussis vs whole-cell pertussis booster, 1987; Lens `002-626-948-048-533`; DOI `10.1097/00006454-198704000-00004` | 120 children aged 18 to 24 months previously primed with whole-cell DTP | Randomized comparative booster trial | Active vaccine comparator: acellular DTP vs whole-cell DTP | Adverse effects, fever, local reactions, major sequelae | Serologic responses | Whole-cell DTP produced more adverse effects; no major sequelae were reported; antibody differences were mixed | No inert placebo; relative reactogenicity only |
| [3340474](https://pubmed.ncbi.nlm.nih.gov/3340474/) | Simultaneous MMR with DTP and OPV boosters, 1988; Lens `031-141-296-726-605`; DOI `10.1542/peds.81.2.237` | Children receiving MMR/DTP/OPV timing schedules | Double-blind and placebo-controlled with respect to DTP/OPV timing | Partial inert/timing placebo, but both groups received active vaccines by schedule | Serious vaccine-associated reactions and minor side effects | Seroconversion and titers | Seroconversion to MMR exceeded 96% in both groups; serious reactions were low and similar; some minor effects were higher with simultaneous administration | Useful placebo blinding for timing, not an untreated or inert comparison of the full vaccine set |
| [8438810](https://pubmed.ncbi.nlm.nih.gov/8438810/) | Acellular BIKEN vs whole-cell pertussis vaccines, 1993; Lens `112-038-283-210-256`; DOI `10.1001/archpedi.1993.02160270052017` | 246 children aged 15 to 20 months previously primed with whole-cell DTP | Randomized, double-blind multicenter study | Active vaccine comparator: DT-aP lots vs WC-DTP | Local and systemic reactions at 6, 24, 48, and 72 hours; acetaminophen use | Pertussis, tetanus, and diphtheria antibody assays | DT-aP produced fewer local/systemic reactions and less acetaminophen use | Active-comparator booster trial; no inert control |
| [3537248](https://pubmed.ncbi.nlm.nih.gov/3537248/) | Bovine rotavirus vaccine RIT 4237 in 3-month-old infants, 1986; Lens `047-839-713-841-504`; DOI `10.1016/s0022-3476(86)80271-2` | 54 inner-city infants | Randomized, double-blind, three-arm trial | Placebo-labeled comparator; composition not visible in PubMed/Lens abstract | Ill effects after dosing | Neutralizing antibody titers and seroconversion | Higher antibody titers and 87% cumulative seroconversion were reported; no ill effects reported | Placebo inertness cannot be verified from abstract-level data |
| [1995721](https://pubmed.ncbi.nlm.nih.gov/1995721/) | Two candidate rotavirus vaccines in a Native American population, 1991; Lens `084-553-978-163-217`; DOI `10.1093/infdis/163.3.483` | Navajo infants aged 2 to 5 months | Randomized, double-blind, placebo-controlled trial | Placebo-labeled comparator; composition not visible in PubMed/Lens abstract | Safety is named, but detailed adverse-event endpoints are not in the abstract | Rotavirus diarrhea over 17 months | Rotavirus diarrhea occurred in 10.2% rhesus, 10.4% RIT 4237, and 8.4% placebo groups; neither vaccine was efficacious | Placebo composition and detailed safety findings require full paper review |
| [8545227](https://pubmed.ncbi.nlm.nih.gov/8545227/) | High-dose rhesus-human reassortant rotavirus vaccines, 1996; Lens `096-602-271-505-723` | 1,278 healthy infants aged 5 to 25 weeks | Randomized, double-blind, placebo-controlled multicenter field trial | Placebo-labeled comparator; composition not visible in PubMed/Lens abstract | Reactions during 5 days after vaccination | Rotavirus gastroenteritis, severe illness, dehydrating illness | Reactions did not differ among groups; tetravalent vaccine reduced rotavirus episodes and severe/dehydrating illness | Placebo inertness unresolved from abstract; solicited safety window was short |
| [8072818](https://pubmed.ncbi.nlm.nih.gov/8072818/) | Three bivalent Streptococcus pneumoniae glycoprotein conjugate vaccines, 1994; Lens `017-491-441-384-377`; DOI `10.1097/00006454-199405000-00007` | 118 children aged 18 to 30 months | Randomized comparison | Active vaccine comparator: experimental conjugates vs licensed pneumococcal vaccine | Safety assessed, but abstract detail is limited | Serotype-specific antibody titers | Conjugation, polysaccharide size, and linkage affected antibody response | Active-comparator study; no inert control |
| [8866803](https://pubmed.ncbi.nlm.nih.gov/8866803/) | Pentavalent pneumococcal conjugate pilot trial in Gambian infants, 1996; Lens `053-628-903-974-276`; DOI `10.1097/00006454-199604000-00010` | 90 Gambian infants | Controlled pilot trial; randomization/blinding not visible in abstract | Active vaccine comparator: Hib vaccine controls | Local and systemic reactions | Antibody titers by ELISA | No serious reactions were reported; antibody titers rose after vaccination | Small active-control pilot; no inert comparator |
| [9521941](https://pubmed.ncbi.nlm.nih.gov/9521941/) | Heptavalent pneumococcal vaccine conjugated to CRM197 in US infants, 1998; Lens `000-805-054-849-906`; DOI `10.1542/peds.101.4.604` | 212 healthy 2-month-old infants | Randomized trial | Active vaccine comparator: investigational meningococcal group C conjugate | Active safety surveillance for 3 days after each dose, local reactions, fever | Pneumococcal antibody concentrations | Local reactions were not increased; fever was common in both groups; most infants reached antibody thresholds after 3 doses | Active comparator plus routine coadministered vaccines; short solicited safety window |
| [10749457](https://pubmed.ncbi.nlm.nih.gov/10749457/) | Heptavalent pneumococcal conjugate vaccine efficacy, safety, and immunogenicity, 2000; Lens `042-299-982-568-001`; DOI `10.1097/00006454-200003000-00003` | 37,868 children | Randomized 1:1 double-blind trial | Active vaccine comparator: meningococcus type C CRM197 conjugate | Safety named, but abstract gives limited adverse-event detail | Invasive vaccine-serotype disease and otitis media outcomes | Vaccine-serotype invasive disease efficacy was 97.4% in fully vaccinated children; otitis-media reductions were smaller | Strong disease-efficacy trial, but active comparator prevents inert-placebo safety inference |
| [10819345](https://pubmed.ncbi.nlm.nih.gov/10819345/) | Nonavalent pneumococcal conjugate with DTP in Gambian infants, 2000; Lens `002-883-009-978-596`; DOI `10.1097/00006454-200005000-00014` | 207 Gambian infants | Randomized trial | Active vaccine comparator: inactivated polio vaccine | Day 1, 2, and 7 visits for local/systemic reactions | Pneumococcal and routine-vaccine antibody responses; carriage | No serious reactions were reported; pneumococcal antibody responses were high; carriage reduction was not significant | Active IPV control and routine coadministration; no inert comparator |
| [8684876](https://pubmed.ncbi.nlm.nih.gov/8684876/) | One vs two injections of Oka/Merck varicella vaccine, 1996; Lens `015-529-094-508-619`; DOI `10.1097/00006454-199601000-00011` | About 2,000 healthy children aged 12 months to 12 years | Randomized dose-regimen comparison | No inert placebo; one-dose vs two-dose varicella vaccine schedule | Clinical reactions, varicelliform rash, fever, injection-site reactions | Seroconversion and antibody titers | Both regimens were generally well tolerated; two doses increased antibody titers | All subjects received active varicella vaccine exposure |
| [17494925](https://pubmed.ncbi.nlm.nih.gov/17494925/) | Quadrivalent HPV vaccine against high-grade cervical lesions, 2007; Lens `089-070-953-411-89X`; DOI `10.1056/nejmoa061741` | 12,167 women aged 15 to 26 | Randomized, double-blind phase 3 trial | **Resolved from full text (2026-11-10):** "a visually indistinguishable aluminum-containing placebo" — the AAHS adjuvant without antigen; double-blinded but not an inert comparator. See [[sources/future-ii-study-group-2007-quadrivalent-hpv-cin2-rct]] | Injection-site AEs 84.4% vs 77.9%; serious AEs similar between arms | CIN2/3, adenocarcinoma in situ, or cervical cancer related to HPV-16/18 (HPV DNA required in lesion tissue; blinded consensus pathology) | VE 98% per-protocol susceptible (1 vs 42), 44% ITT type-specific, 17% ITT any type; zero cancers in either arm; no effect on prevalent infection/lesions | Comparator is adjuvant-matched, not inert: systemic safety vs a true placebo is untested by this trial; cancer prevention is an extrapolation from precursor lesions |

## Additional placebo-control leads from Lens

These were not part of the CHD citation list, but they matter because they show that `pediatric vaccine trial` plus `placebo` is not empty as a search category.

| PMID | Trial | Population | Comparator signal | Why it matters |
|---|---|---|---|---|
| [19395948](https://pubmed.ncbi.nlm.nih.gov/19395948/) | Live attenuated influenza vaccine in vaccine-naive children, 2009; Lens `065-725-782-126-640`; DOI `10.1097/inf.0b013e31819219b8` | Children aged 6 to under 36 months | Abstract names both excipient placebo and saline placebo arms | This is a direct counterexample to an absolute claim that child vaccine trials never use saline or placebo controls, though it is one influenza trial and not a universal safety answer |
| [31769402](https://pubmed.ncbi.nlm.nih.gov/31769402/) | Live oral cholera vaccine CVD 103-HgR in children and adolescents, 2020; Lens `032-598-317-061-494`; DOI `10.4269/ajtmh.19-0241` | Children and adolescents aged 6 to 17 years | Placebo-controlled, double-blind trial; placebo composition not visible in PubMed abstract | This is a placebo-labeled pediatric vaccine trial, but inertness remains unresolved from the abstract alone |

## What this wiki currently concludes
- The CHD source correctly points to a real methodological issue: many cited trials used active vaccine comparators or schedule/dose comparisons rather than inert controls.
- The trial records do not support a blanket conclusion that pediatric vaccine trials never use placebo or saline controls; the Lens counter-search found child vaccine trials with placebo-labeled and saline arms.
- For the cited trials, the defensible claim is trial-specific: name the comparator, endpoint, result, and limitation before making safety claims.
- Placebo-labeled records are not automatically inert-placebo records. Inertness must be checked from the full paper, protocol, package insert, or regulatory file.
- These trial records also do not answer the broader question of whether vaccinated children are more healthy than not vaccinated children, because the audited endpoints are mostly disease-specific, immunogenicity-based, or short-term safety measures rather than broader overall-health comparisons.

## Related
- [[sources/vaccine-makers-do-not-use-placebos-to-test-the-safety-of-their-vaccines-for-kids]]
- [[concepts/placebo-controls]]
- [[concepts/clinical-endpoints]]
- [[concepts/surrogate-endpoints]]
- [[comparisons/disease-prevention-vs-health-outcomes]]
- [[synthesis/vaccinated-children-more-healthy-question]]