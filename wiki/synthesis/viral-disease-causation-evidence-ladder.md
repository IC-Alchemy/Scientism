---
title: Viral Disease Causation Evidence Ladder
category: synthesis
summary: Cross-cutting framework for separating detection, isolation, transmission, animal challenge, molecular, clinical, and intervention evidence in viral disease causation claims.
tags: [virology, causation, methodology, evidence-standard]
sources: 7
updated: 2026-05-14
claim_status: exploratory
claim_type: methodological
---

# Viral Disease Causation Evidence Ladder

> Warning: This page is a methodological synthesis, not medical advice and not a proof page for any single virus-disease pair.

## Current answer
The current vault evidence does not support a blanket statement that viral disease causation has either been globally proven or globally refuted. The better answer is disease-specific and endpoint-specific.

For each claimed viral disease, the vault should ask which rung of evidence is actually in hand and what question that rung can answer.

## Why a ladder is needed
The existing [[synthesis/virus-disease-attribution-audit-worklist]] shows that many diseases have candidate foundational papers, but candidate status is not the same as completed evidence review. The central risk is endpoint compression: a source may show detection, culture, serology, animal disease, or intervention effect, while later summaries retell the result as simple causal closure.

[[sources/rivers-1937-viruses-and-kochs-postulates]] is the key historical bridge. Rivers argued that viruses do not have to satisfy Koch's bacteriology rules literally, but he still required more than mere association: the virus must be shown to be causally involved rather than incidental or coexisting.

[[sources/fredericks-relman-1996-sequence-based-identification-microbial-pathogens]] extends the same caution into molecular evidence. Sequence evidence can be useful, but a sequence hit is not the same as disease causation unless it is tied to controls, localization, timing, biological plausibility, and the disease endpoint.

[[sources/jefferson-2022-hierarchical-framework-transmission-causality-respiratory-viruses]] applies the same problem to respiratory-virus transmission: weak detection evidence and strong transmission evidence should not be treated as interchangeable.

## Evidence ladder
| Rung | Evidence type | What it can answer | What it cannot answer by itself |
| --- | --- | --- | --- |
| 1 | Clinical syndrome description | Whether a named disease pattern was observed. | Whether a virus caused it. |
| 2 | Microscopy, antigen, PCR, RT-qPCR, or sequencing detection | Whether viral material or a viral signal was detected in sampled material. | Whether the detected material was infectious, sufficient, or causal. |
| 3 | Culture, propagation, or isolation workflow | Whether an agent can be propagated or characterized under laboratory conditions. | Whether it caused the original disease in ordinary conditions. |
| 4 | Serology or immune response | Whether the host mounted an immune response associated with the agent. | Whether the agent was necessary, sufficient, or non-incidental. |
| 5 | Animal challenge or experimental exposure | Whether the agent or material can produce disease-like endpoints in a specified host by a specified route. | Whether ordinary human natural-route causation is settled. |
| 6 | Re-isolation or recovery from the experimental host | Whether the agent can be recovered after experimental infection. | Whether this recapitulates natural disease ecology. |
| 7 | Controlled human challenge | Whether exposure under a specified protocol can produce defined clinical or laboratory endpoints. | Whether population-level disease patterns, cofactors, and all real-world transmission are explained. |
| 8 | Prospective cohort, outbreak, or transmission-chain evidence | Whether exposure, infection markers, and disease endpoints align over time in humans. | Whether all alternative causes, cofactors, or measurement artifacts are excluded. |
| 9 | Intervention evidence | Whether blocking, removing, or modifying the agent changes a disease endpoint. | Whether the whole causal story is one-factor, sufficient, or universal. |
| 10 | Replicated cross-method convergence | Whether multiple independent methods point to the same causal model. | It still does not justify ignoring endpoint limits or unfavorable findings. |

## How this applies to current vault rows
### Stronger experimental ladders
- Hepatitis B and hepatitis C have candidate rows that visibly climb from detection or syndrome separation toward chimpanzee challenge and molecular-clone infectivity. See [[synthesis/virus-disease-attribution-audit-worklist]].
- Mumps, rubella, and varicella-zoster candidate rows include animal inoculation, experimental exposure, culture, serology, or fatal-case pathology leads, but they still need full source pages before the vault can grade them.

### Association-heavy ladders
- HPV and cervical cancer, EBV and Burkitt lymphoma, and HHV-8 and Kaposi sarcoma have strong molecular-detection and association leads in the worklist, but those endpoints must be separated from necessity, sufficiency, tumor initiation, and cofactor claims.
- EBV and infectious mononucleosis is a better prospect for prospective timing evidence than EBV and Burkitt lymphoma, because the disease endpoint is acute infection rather than tumor causation.

### Transmission-boundary ladders
- Influenza currently has a primary negative-result boundary in [[sources/rosenau-1919-experiments-to-determine-mode-of-spread-of-influenza]], but that source predates the 1933 influenza-virus identification framework.
- COVID-19 currently has an endpoint-specific audit in [[synthesis/sars-cov-2-covid-causation-audit]]. The key boundary is that PCR and RT-qPCR are detection endpoints, animal inoculation is model-specific pathogenicity, and the audited human challenge evidence is uncontrolled challenge-model evidence rather than sham-controlled clinical causation proof.
- Poliomyelitis has a direct route-boundary lead in [[sources/sabin-olitsky-1938-fate-of-nasally-instilled-poliomyelitis-virus]], but the vault still lacks a complete natural-route failure series.

## Current unresolved assessment
Under this vault's evidence standard, "virus causes disease" should not be accepted or rejected as one global proposition. The phrase has to be expanded into a named disease, named virus, named study design, exposure route, comparator or control, endpoint, result, and limitation.

The current evidence in hand supports a methodological conclusion: viral causation claims often rest on multiple rungs that are rhetorically compressed after the fact. That does not prove the claims false. It means each disease row needs a paper-by-paper ladder reconstruction before it can be marked supported, contradicted, or unresolved.

## Next research targets
1. Ingest [[sources/rivers-1937-viruses-and-kochs-postulates]] into [[concepts/germ-theory]] and [[concepts/virus-isolation]] as the historical viral-causation standard.
2. Pick one disease row with a clear ladder, such as hepatitis B or hepatitis C, and source-ingest each rung from detection through challenge or molecular clone.
3. Pick one association-heavy row, such as HPV/cervical cancer or HHV-8/Kaposi sarcoma, and explicitly separate association, necessity, sufficiency, and cofactor evidence.
4. Continue the failed-attempt register so positive and non-confirmatory experiments remain visible together.

## Related pages
- [[synthesis/virus-disease-attribution-audit-worklist]]
- [[synthesis/virus-causation-inferential-leaps]]
- [[synthesis/failed-virus-causation-attempts-register]]
- [[concepts/germ-theory]]
- [[concepts/virus-isolation]]
- [[concepts/inferential-leap]]
