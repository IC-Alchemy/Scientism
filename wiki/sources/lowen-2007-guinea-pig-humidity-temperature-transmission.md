---
title: Influenza Virus Transmission Is Dependent on Relative Humidity and Temperature
category: source
summary: 2007 PLoS Pathogens controlled guinea-pig transmission study (Lowen, Mubareka, Steel, Palese) showing aerosol-route transmission of A/Panama/2007/99 (H3N2) between cage-separated animals - no physical contact possible - is highly efficient at 5 degrees C and blocked at 30 degrees C, with transmission efficiency tracking humidity; endpoints are plaque-assay nasal-wash titers and HI seroconversion, with no disease endpoint.
tags:
  - animal-transmission
  - influenza
  - influenza-virus
  - natural-route-transmission
  - controlled-experiment
sources: 1
updated: 2026-11-10
claim_status: supported
claim_type: empirical
source_tier: tier-1
evidence_role: controlled natural-route animal transmission with route separation and environment control; GAP 2 animal anchor for influenza
pmid: 17953482
pmcid: PMC2034399
doi: 10.1371/journal.ppat.0030151
---

# Influenza Virus Transmission Is Dependent on Relative Humidity and Temperature

## Source type
- Role in this vault: controlled natural-route animal transmission experiment with explicit route separation (wire-grid cages, no physical contact) and controlled temperature/humidity; fills the animal half of GAP 2 (controlled natural-route transmission) in [[synthesis/source-verification-queue]] for influenza, replacing the unreachable Herlocher 2004 ferret paper (queue item 5, still `unverifiable`).
- Journal/year: *PLoS Pathogens*, 2007;3(10):e151
- Authors: Anice C. Lowen, Samira Mubareka, John Steel, Peter Palese (Icahn/Mount Sinai; Ralph S. Baric was the handling editor)
- Source basis in hand: complete open-access full text from Europe PMC (PMC2034399), including Methods, Results, Discussion, and the methods supplement description; all numbers below are from that full text.

> [!warning] Warning
> This page is for research analysis only. It is not medical advice.

## Evidence fields
| Field | Extraction |
|---|---|
| Study type | Controlled transmission experiments in an environmental chamber; 20 replicate experiments, each in duplicate ("transmission under each set of conditions was assessed in duplicate") |
| Subject / sample | Female Hartley strain guinea pigs, 300-350 g (Charles River); 8 animals per experiment: 4 intranasally inoculated donors, 4 naive recipients |
| Exposure / inoculation | Donors inoculated day 0 intranasally with 10^3 PFU influenza A/Panama/2007/99 (H3N2, MDCK-cell propagated; 150 ul per nostril in PBS + 0.3% BSA). At 24 h post-infection, donors were caged opposite naive animals: "each of the eight guinea pigs was placed in a 'transmission cage'... modified by replacing one side panel with a wire grid... such that the wire grids opposed each other... In this arrangement, the guinea pigs cannot come into physical contact with each other." Co-housing ran 7 days inside a Caron 6030 chamber at controlled RH (20-80%) and temperature (5, 20, or 30 degrees C); "air flowed freely between shelves, allowing transmission to occur from any infected to any naive animal", with airflow directed toward naive animals |
| Comparator / control | Sham arm: **no** sham inoculation; the design contrasts exposure conditions rather than arms. The four naive animals serve as unexposed-baseline recipients (nasal washes taken from day 2 post-inoculation, before which no virus should be detectable), and the condition matrix itself provides negative contrasts: 0/4 transmission at 80% RH (20 degrees C) and 0/4 at 30 degrees C/35% RH. Cross-contamination was controlled procedurally: "sentinel animals were handled before inoculated animals, gloves were changed between cages, and work surfaces were sanitized between guinea pigs" |
| Endpoint | Named exactly: virus in nasal wash samples "titrated by plaque assay" on Madin Darby canine kidney cells, collected on day 2 post-inoculation and every second day through day 12 post-inoculation; seroconversion "assessed by hemagglutination inhibition assay" from serum collected before infection and on day 17 post-infection. Transmission outcome = infection detection in a naive animal (titer + seroconversion, Table S1). There is **no disease endpoint**: "influenza virus-infected guinea pigs did not display detectable symptoms of disease (e.g., weight loss, fever, sneezing, coughing) during the experiments described" |
| Result | At 20 degrees C: transmission "highly efficient (occurred to three or four of four exposed guinea pigs)" at 20% and 35% RH; 1/4 at 50% RH; 3/4 at 65% RH; 0/4 at 80% RH. At 5 degrees C: 75-100% transmission at 35% and 50% RH; 50% at 65% and 80% RH (differences vs 20 degrees C significant at 50% and 80% RH, Fisher's exact test p<0.05). At 30 degrees C / 35% RH: no transmission (0/4, two experiments). Mechanism: peak shedding extended at 5 degrees C - mean last day with nasal-wash titer >=10^6 PFU/ml was 3.93 +/- 0.63 d at 5 degrees C vs 2.21 +/- 0.61 d at 20 degrees C (p<0.0005); innate-immune gene induction in nasal turbinates was comparable between temperatures |
| Main limitation | No disease endpoint - guinea pigs are an asymptomatic-shedding model, so this study can support transmission claims only, never influenza-illness claims; authors' own caveat that "aerosol" here is defined to include "respiratory droplets of all sizes", so the experiments do not isolate small-particle airborne route; transmission events cannot exclude secondary transmission between exposed animals ("others could be the result of secondary transmission from a previously infected, exposed guinea pig"); chamber environments (constant RH, constant temperature, airflow) are not household conditions; single virus strain (H3N2 Pan/99) |

## Which gap and ladder rung this fills
- Queue GAP 2 (controlled natural-route transmission), animal half: route-separated natural exposure (respiratory aerosols/droplets in shared air) under controlled conditions, with a replication-level (plaque assay) infection endpoint and negative-condition contrasts. Substitutes for Herlocher et al. 2004 (ferret contact-transfer, JID 190(9):1627-1630), which remains `unverifiable` - OUP/PDF Cloudflare-403 including in the real browser, Unpaywall/OpenAlex report closed with no repository copy, and the Internet Archive was offline this run (see [[synthesis/source-verification-queue]]).
- Influenza ladder: new rung "controlled animal natural-route transmission" in [[synthesis/influenza-influenza-virus-evidence-ladder]], sitting between the 1933 uncontrolled ferret co-housing row and the human household RCT row; cross-cutting note added in [[synthesis/viral-disease-causation-evidence-ladder]].

## What the experiment can answer
- That influenza A/H3N2 virus shed by inoculated guinea pigs infected naive guinea pigs across a physical-contact barrier in shared air, at rates that track ambient humidity and temperature - under the authors' definition that aerosol includes droplets of all sizes.
- That the same strain, exposure geometry, and inoculum produce transmission at 5 degrees C but none at 30 degrees C in this system, and none at 20 degrees C/80% RH - i.e., environment-dependent transmission, with increased peak-shedding duration as the measured mechanism.
- That transmission was repeatedly produced without any physical contact, addressing the 1933 ferret co-housing limitation where contact and air routes were confounded.

## What it cannot answer
- Disease causation: no symptoms of influenza were measurable in guinea pigs; this model cannot test whether natural-route transmission produces influenza illness, only whether infection markers transmit.
- Which droplet-size class carried the infection (fine aerosols vs large droplets settling between 5 cm-applied grid cages); the authors use "aerosol" for all sizes and say so.
- Human epidemiology: chamber conditions, constant humidity, and guinea-pig physiology are not human households; seasonal "weather" effects in humans are a separate inferential step (see below).
- Generalization across strains: one H3N2 vaccine-lineage strain was tested.

## Inferential leaps to watch
- The authors' closing claim - "We provide direct, experimental evidence to support the role of weather conditions in the dynamics of influenza" - moves from chamber-controlled guinea-pig experiments to human seasonal epidemiology. The experiment shows humidity/temperature dependence in one animal system for one strain; the epidemiological extrapolation is the authors' inference, not a measured endpoint of these experiments.
- Calling the spread "aerosol spread" in the abstract while the methods define "aerosol" as droplets of all sizes blurs the droplet-size claim the title-era literature later fought over.
- Treating 10^3 PFU intranasal donors as models of natural index cases: donors are lab-inoculated, and no natural index arm exists.

## Related
- [[sources/smith-andrewes-laidlaw-1933-virus-obtained-from-influenza-patients]] - the uncontrolled 1933 ferret co-housing precursor
- [[sources/rosenau-1919-experiments-to-determine-mode-of-spread-of-influenza]] - the negative human natural-exposure experiments this rung eventually answers
- [[sources/cowling-2009-household-facemask-hand-hygiene-rct]] - the human controlled natural-route counterpart
- [[synthesis/influenza-influenza-virus-evidence-ladder]]
- [[synthesis/viral-disease-causation-evidence-ladder]]
- [[synthesis/source-verification-queue]]
