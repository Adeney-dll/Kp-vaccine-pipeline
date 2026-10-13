# In silico design of a multi-epitope vaccine candidate against _Klebsiella pneumoniae_ targeting the outer membrane lipoprotein [Pal]

**Author:** [Adene] · **Status:** Computational study; no experimental validation

---
### Overview

This repository documents a reverse-vaccinology workflow for designing a multi-epitope vaccine (MEV) against _Klebsiella pneumoniae_. The target is Pal; a peptidoglycan-associated outer membrane lipoprotein. Predictions come from free web servers, and short Python scripts handle the filtering. Raw server outputs are stored unedited so every result can be checked.

Two constructs were designed: **MEV-1**, with the cholera toxin B subunit as adjuvant, and **MEV-2**, with human β-defensin 2. Both were evaluated for physicochemical properties, structural quality, TLR4 docking, flexibility, codon-optimised expression in _E. coli_, in silico cloning and simulated immune response.

---
### Workflow
![[Workflow-chart.png]]Created in  https://BioRender.com

---
### Results
**Target and localization:** The Peptidoglycan-Associated Lipoprotein (Pal) was selected as the primary antigenic target from the outer membrane virulence factors of _Klebsiella pneumoniae_, **10** sequences ranging from 170 to 185 amino acids in length were obtained from NCBI, and a consensus sequence was derived using the MUSCLE algorithm in MEGA 12. Subcellular localization and signal peptide analyses via PSORTb and SignalP support its outer membrane placement and identified a Sec/SPII signal peptide cleavage site between positions 21 and 22. Consequently, the signal peptide was computationally truncated to yield a mature 153-amino acid sequence.


NCBI search string [ _Klebsiella pneumoniae_ Pal ATCC 13883]


PSORTb Localisation scores

| Cytoplasmic          | 0.00  |
| -------------------- | ----- |
| Cytoplasmic Membrane | 0.00  |
| Periplasmic          | 0.00  |
| Outer Membrane       | 10.00 |
| Extracellular        | 0.00  |
