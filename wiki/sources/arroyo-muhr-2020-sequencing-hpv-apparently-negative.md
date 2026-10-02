---
title: Sequencing detects human papillomavirus in some apparently HPV-negative invasive cervical cancers
category: source
summary: RNA-enriched deep sequencing detected HPV sequences in 48 of 92 PCR-negative cervical cancers, with splice junctions in 12 cases indicating transcriptionally active viral material.
tags:
  - assay-boundary
  - cervical-cancer
  - deep-sequencing
  - failed-detection
  - hpv
  - hpv-negative-tumors
  - rna-sequencing
sources: 1
updated: 2026-10-01
claim_status: unresolved
claim_type: empirical
source_tier: tier-1
evidence_role: assay-boundary sequencing paper with transcriptional-activity endpoints
pmid: 31859615
---

# Sequencing detects HPV in apparently HPV-negative invasive cervical cancers (Arroyo Mühr et al. 2020, J Gen Virol)

## Source type
- Role in this vault: assay-boundary paper; the RNA-enriched companion to the 2020 Br J Cancer deep-sequencing paper
- Journal/year: *Journal of General Virology*, 2020
- Source basis in hand: PubMed abstract only; full text not obtained

## Evidence fields
| Field | Extraction |
|---|---|
| Study type | Blinded-panel deep sequencing of randomly selected PCR-negative and PCR-positive cervical cancers, with blank-block negative controls |
| Subject / sample | From the 2,850-case Swedish database: 92 HPV PCR-negative cervical cancers, 34 HPV PCR-positive cervical cancers, four blank-block pools |
| Intervention or exposure | Extraction, reverse transcription, rRNA depletion (mRNA enrichment), NovaSeq 6000 sequencing; non-human reads queried against HPV proteins |
| Comparator / control | PCR-positive tumors and blank-block pools as assay controls |
| Endpoint | HPV sequence detection; exon/intron ratio (DNA vs RNA content); splice-junction detection |
| Result | Median 23 million paired reads per sample. HPV was detected in 31/34 PCR-positive cases. Among PCR-negative cases, 48/92 (52.2%) contained HPV sequences, HPV33 most often (14/48). Exon/intron ratios indicated both DNA and RNA were present; splice junctions were detected in 12 cases. |
| Main limitation | Abstract-level record; no PMCID located in this pass; low-level detections and contamination controls beyond blank pools are not visible in the abstract; detection of transcripts does not establish a causal role in each tumor. |

## What the abstract can answer
- Whether HPV nucleic acid, including RNA with splice junctions (a marker of transcription), is present in a subset of PCR-negative cervical cancers: yes, in 52.2% of the sampled negatives, with 12 cases showing splice junctions.
- That some cervical cancers contain HPV that is difficult to detect by the PCR assays used — an assay boundary, directly stated by the authors.

## What full text would still need to establish
- Contamination auditing beyond blank pools; depth thresholds; which of the 48 detections had transcriptional support.

## Later inferential-leap risk
Splice junctions show transcription, not causation. The leap to "active infection caused these tumors" must pass through the integration and progression rungs of [[synthesis/cervical-cancer-hpv-evidence-ladder]]; conversely, the 44 PCR-negatives still negative by sequencing do not establish an HPV-independent class either, given tissue-quality and depth limits.

## Vault conclusion
Abstract-level: RNA-enriched sequencing detected HPV sequences in 48 of 92 PCR-negative cervical cancers, including 12 cases with splice junctions, extending the failed-detection boundary from DNA to transcriptionally active viral material.

## Connections
- Part of the HPV boundary set in [[synthesis/failed-virus-causation-attempts-register]]
- Companion: [[sources/arroyo-muhr-2020-deep-sequencing-pcr-negative]] (same group's 392-case sequencing pass)
- Anchors [[synthesis/cervical-cancer-hpv-evidence-ladder]]