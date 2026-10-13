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

**2. Epitopes:** Linear B-cell, MHC-I, and MHC-II epitopes were predicted from the consesus Pal sequence utilizing the IEDB servers, employing the BepiPred v3.0, NetMHCpan EL 4.1, and NetMHCIIpan EL 4.1 algorithms across 27 human alleles. To ensure maximum immunogenic efficacy, the initial datasets comprising **3,915** MHC-I and **756** MHC-II predicted epitopes were narrowed down to 37 and 21 top binders respectively, with **4** predicted B-cell epitopes, and filtered via custom Python scripts, VaxiJen v2.1 (threshold 0.3), ToxinPred 3.0, and AlgPred 2.0. This screening yielded zero viable MHC-I candidates, but successfully isolated five MHC-II epitopes and one B-cell epitope that strictly met all required thresholds for antigenicity, non-toxicity, and non-allergenicity.


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


Consesus Structure with surface exposed Epitopes coloured
<img src="results/Structures/Pymol/surface-all.png" alt="Epi-pose" width="800">
(NOTE: See "results/Structures/Pymol" for individual surface exposure)


Expasy data for both constructs

| Physiochemical Properties               | MEV-1                  | MEV-2                  |
| --------------------------------------- | ---------------------- | ---------------------- |
| Total Number of Amino Acids             | 320                    | 258                    |
| Molecular Weight (MW)                   | 34902.51 Da / 34.9 kDa | 27591.39 Da / 27.6 kDa |
| Theoretical pI (Isoelectric Point)      | 5.88                   | 6.49                   |
| Instability Index (II)                  | 32.29                  | 31.75                  |
| Aliphatic Index                         | 79.72                  | 74.61                  |
| GRAVY (Grand Average of Hydropathicity) | -0.386                 | -0.367                 |


**4. Evaluation:** The tertiary structures of both MEV constructs were modeled using AlphaFold and rigorously validated via SWISS-MODEL, yielding highly favored Ramachandran plots (>91%) and optimal energy stability scores that confirmed their structural viability. To evaluate immune receptor interaction, molecular docking against a processed human TLR-4 monomer (chain A) was executed on the HawkDock server. Both constructs demonstrated robust binding affinities, with MEV-1 and MEV-2 producing strong binding free energies of -24.05 kcal/mol and -51.36 kcal/mol, respectively, which were subsequently mapped and visualized using PyMOL.