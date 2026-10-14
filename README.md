# In silico design of a multi-epitope vaccine candidate against _Klebsiella pneumoniae_ targeting the outer membrane lipoprotein [Pal]

**Author:** [Adene] · **Status:** Computational study; no experimental validation

---
### Overview

This repository documents a reverse-vaccinology workflow for designing a multi-epitope vaccine (MEV) against _Klebsiella pneumoniae_. The target is Pal; a peptidoglycan-associated outer membrane lipoprotein. Predictions come from free web servers, and short Python scripts handle the filtering. Raw server outputs are stored unedited so every result can be checked.

Two constructs were designed: **MEV-1**, with the cholera toxin B subunit as adjuvant, and **MEV-2**, with human β-defensin 2. Both were evaluated for physicochemical properties, structural quality, TLR4 docking, flexibility, codon-optimised expression in _E. coli_, in silico cloning and simulated immune response.

---
### Workflow
<img src="results/Workflow-chart.png" alt="Workflow Diagram" width="800">


---
### Results
**1. Target and localization:** The Peptidoglycan-Associated Lipoprotein (Pal) was selected as the primary antigenic target from the outer membrane virulence factors of _Klebsiella pneumoniae_, **10** sequences ranging from 170 to 185 amino acids in length were obtained from NCBI, and a consensus sequence was derived using the MUSCLE algorithm in MEGA 12. Subcellular localization and signal peptide analyses via PSORTb and SignalP support its outer membrane placement and identified a Sec/SPII signal peptide cleavage site between positions 21 and 22. Consequently, the signal peptide was computationally truncated to yield a mature 153-amino acid sequence.


NCBI search string [ _Klebsiella pneumoniae_ Pal ATCC 13883]


Sequence Alignment on MEGA 12
<img src="results/raw_images/MEGA_ 01.png" alt="MEGA" width="800">
PSORTb Localisation scores and SignalP output plot

| Cytoplasmic          | 0.00  |
| -------------------- | ----- |
| Cytoplasmic Membrane | 0.00  |
| Periplasmic          | 0.00  |
| Outer Membrane       | 10.00 |
| Extracellular        | 0.00  |
<img src="results/SignalP output_Consesus_plot.png" alt="SignalP Diagram" width="800">

**2. Epitopes & Filtering:** Linear B-cell, MHC-I, and MHC-II epitopes were predicted from the consesus Pal sequence utilizing the IEDB servers, employing the BepiPred v3.0, NetMHCpan EL 4.1, and NetMHCIIpan EL 4.1 algorithms across 27 human alleles. To ensure maximum immunogenic efficacy, the initial datasets comprising **3,915** MHC-I and **756** MHC-II predicted epitopes were narrowed down to 37 and 21 top binders respectively, with **4** predicted B-cell epitopes, and filtered via custom Python scripts, VaxiJen v2.1 (threshold 0.3), ToxinPred 3.0, and AlgPred 2.0. This screening yielded zero viable MHC-I candidates, but successfully isolated five MHC-II epitopes and one B-cell epitope that strictly met all required thresholds for antigenicity, non-toxicity, and non-allergenicity.


B-Cell passing Epitope

| Peptide                                    | Antigenicity      | Toxicity  | Allergenicity         |
| ------------------------------------------ | ----------------- | --------- | --------------------- |
| NKNASNDQSGEGMLGAGTGMDANGNGGNMSSEEQARLQMQQL | Probable antigen. | Non-Toxin | Probable Non-Allergen |


MHCII Passing Epitopes

| Peptide         | Antigenicity | Toxicity  | Allergenicity | Immunogenicity |
| --------------- | ------------ | --------- | ------------- | -------------- |
| DKYDIRSDFAAMLDA | antigen      | Non-Toxin | Non-Allergen  | Immunogen      |
| LGERRANAVKMYLQG | antigen      | Non-Toxin | Non-Allergen  | Immunogen      |
| NGNGGNMSSEEQARL | antigen      | Non-Toxin | Non-Allergen  | Immunogen      |
| AMLDAHANFLRSNPS | antigen      | Non-Toxin | Non-Allergen  | Immunogen      |
| VYFDLDKYDIRSDFA | antigen      | Non-Toxin | Non-Allergen  | Immunogen      |


**3. Construct Design:** A 3-dimensional prediction of consesus Pal protein was obtained via AlphaFold and Epitope surface exposure was validated via Pymol. Two multi-epitope vaccine candidates were manually constructed by assembling the validated epitopes with GPGPG linkers and conjugating them via EAAAK linkers to either Cholera enterotoxin subunit B (MEV-1) or Human beta-defensin 2 (MEV-2) adjuvants, with the native signal peptides of both adjuvants cleaved. Initial physicochemical assessments via Expasy ProtParam indicated structural instability, prompting the integration of a 109-amino acid _E. coli_ Thioredoxin (Trx) chaperone tag to restore thermodynamic stability, terminating with a 6xHis-tag. Final evaluations confirmed that both complete MEV sequences exhibit optimal structural parameters, classifying them as stable, hydrophilic candidates.
Secondary structure profiles were first established using SOPMA, followed by 3D tertiary structure modeling via AlphaFold and validated through SWISS-MODEL, yielding favored Ramachandran plots (>91%)

Consesus Structure with surface exposed Epitopes coloured
<img src="results/Structures/Pymol/surface-all.png" alt="Epi-pose" width="800">
(NOTE: See "results/Structures/Pymol" for individual surface exposure)


MEV Design Chain-- [Adjuvant] - EAAAK - [MHC-II] - GPGPG - [B-cell] – HHHHHH


Expasy data for both constructs

| Physiochemical Properties               | MEV-1                  | MEV-2                  |
| --------------------------------------- | ---------------------- | ---------------------- |
| Total Number of Amino Acids             | 320                    | 258                    |
| Molecular Weight (MW)                   | 34902.51 Da / 34.9 kDa | 27591.39 Da / 27.6 kDa |
| Theoretical pI (Isoelectric Point)      | 5.88                   | 6.49                   |
| Instability Index (II)                  | 32.29                  | 31.75                  |
| Aliphatic Index                         | 79.72                  | 74.61                  |
| GRAVY (Grand Average of Hydropathicity) | -0.386                 | -0.367                 |


SOMPA Secondary Structure Data MEV-1
<img src="results/Structures/SOPMA/MEV-1.png" alt="mev" width="800">
SOMPA Secondary Structure Data MEV-2
<img src="results/Structures/SOPMA/MEV-2.png" alt="mev" width="800">
AlphaFold Tertiary structure prediction for MEV-1
<img src="results/Structures/AlphaFold/MEVs/MEV-1-Alp.png" alt="mev" width="800">

AlphaFold Tertiary structure prediction for MEV-2
<img src="results/Structures/AlphaFold/MEVs/MEV-2-Alp.png" alt="mev" width="800">

SWISS-MODEL validation and energy requirements.

| Parameter               | MEV-1       | MEV-2       |
| ----------------------- | ----------- | ----------- |
| Ramachandran Favoured   | 92.45%      | 91.02%      |
| MolProbity Score        | 1.95        | 2.00        |
| Clash Score             | 4.95        | 3.93        |
| QMEANDisCo Global Score | 0.58 ± 0.05 | 0.53 ± 0.05 |
| QMEAN Z-Score           | -1.96       | -1.20       |

MEV-1 Ramachandran plot and quality comparison graph
<img src="results/Structures/SWISS-MODEL/MEV-1-01.png" alt="mev" width="800">
<img src="results/Structures/SWISS-MODEL/MEV-1-QC.png" alt="mev" width="800">
MEV-2 Ramachandran plot and quality comparison graph
<img src="results/Structures/SWISS-MODEL/MEV-2-01.png" alt="mev" width="800">
<img src="results/Structures/SWISS-MODEL/MEV-2-QC.png" alt="mev" width="800">

**4. Evaluation:** To evaluate immune receptor interaction, molecular docking against a processed human TLR-4 monomer (chain A) was executed on the HawkDock server. Both constructs demonstrated suitable binding affinities, with MEV-1 and MEV-2 producing strong binding free energies of -24.05 kcal/mol and -51.36 kcal/mol, and docking scores of -5323.90 and -3867.47 respectively, which were subsequently mapped and visualized using PyMOL.

Consolidated interaction table

| Construct | Receptor          | Docking Score | TLR4 (Chain A) Interface Residues                                                                                                                                                     | MEV Interface Residues                                                                                                 |
| --------- | ----------------- | ------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------- |
| MEV-1     | TLR4, (PDB: 4G8A) | -5323.90      | Lys21 Phe28 Ser45 Tyr46 Phe49 Pro52 Glu68 His203 His230 Arg231 Glu260 Glu261 Tyr377 Glu399 His400 Ile424 Glu448                                                                       | Ala88 Ala89 Thr90 Glu102 Ala106 Asn107 Gln112 Pro249 Gly250 Pro251 Gly252 Glu255 Gln266 Pro269 Gly270                  |
| MEV-2     | TLR4, (PDB: 4G8A) | -3867.47      | Arg238 Glu244 Tyr266 Leu267 Asp268 Tyr269 Tyr270 Thr293 Lys315 Lys336 Gly337 Asn339 Asn383 Gly384 Asn407 His432 Arg434 Gly454 Asn455 Ser456 Phe457 Glu459 Asn460 Gln481 Glu483 Gln484 | Met239 Ser240 Ser241 Glu242 Glu243 Gln244 Ala245 Leu247 Gln248 Gln250 Gln251 Leu252 His253 His254 His255 His256 His257 |

MEV-1[TLR4] complex
<img src="results/Structures/Docking/complex_docking_MEV1.png" alt="mev" width="800">
MEV-2[TLR4] complex
<img src="results/Structures/Docking/complex_docking_MEV2.png" alt="mev" width="800">
MEV structure in purple and TLR4 fragment in cyan


**5. Downstream analysis:** Normal mode analysis to determine the structural flexibility of the constructs was run, and both sequences were subsequently codon-optimized for _E. coli_ expression, successfully elevating their GC content into the viable optimal range without altering the amino acid sequence. The optimized genes were _in silico_ cloned into the pET-28a(+) expression vector via NdeI and XhoI restriction sites using Benchling, while extended 1,000-step multi-dose C-ImmSim simulations predicted the induction of long-lasting cellular and humoral immune memory.

The correlation, deformation, displacement, and eigen plots were recorded for both:
MEV-1
<img src="results/Normal-mode-analysis/MEV-1/MEV-1I.jpg" alt="mev" width="800">

And MEV-2
<img src="results/Normal-mode-analysis/MEV-2/MEV-2I.jpg" alt="mev" width="800">
Mode and deformation energies were also noted

| MEV-1 | MODE | DEFORMATION ENERGY |     | MEV-2 | MODE | DEFORMATION ENERGY |
| ----- | ---- | ------------------ | --- | ----- | ---- | ------------------ |
|       | 7    | 0.185              |     |       | 7    | 0.01               |
|       | 8    | 0.198              |     |       | 8    | 0.004              |
|       | 9    | 0.831              |     |       | 9    | 0.024              |
|       | 10   | 0.364              |     |       | 10   | 0.042              |

Codon optimization was carried out for E-coli expression and DNA sequence was obtained without altering the Amino acid sequence. 

|                                  | MEV-1             | MEV-2             |
| -------------------------------- | ----------------- | ----------------- |
| Sequence Length                  | 960 nt (bp)       | 774 nt (bp)       |
| GC Content (Before Optimization) | 31.1%             | 33.3%             |
| GC Content (After Optimization)  | 49.9%             | 52.5%             |
| Codon Modifications              | 186 of 320 codons | 153 of 258 codons |

cloning was achieved using the pET-28a(+) expression vector utilizing the NdeI and XhoI restriction sites.
<img src="results/Cloning/pET-28a_MEV-1.png" alt="mev" width="800">
<img src="results/Cloning/pET-28a_MEV-2.png" alt="mev" width="800">
