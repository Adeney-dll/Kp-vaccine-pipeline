# In silico design of a multi-epitope vaccine candidate against _Klebsiella pneumoniae_ targeting the outer membrane lipoprotein [Pal]

**Author:** [Adene] · **Status:** Computational study; no experimental validation

---
### Overview

This repository documents a reverse-vaccinology workflow for designing a multi-epitope vaccine (MEV) against _Klebsiella pneumoniae_. The target is Pal, a peptidoglycan-associated outer membrane lipoprotein. Predictions come from free web servers, and short Python scripts handle the filtering. Raw server outputs are stored unedited so every result can be checked.

Two constructs were designed: **MEV-1**, with the cholera toxin B subunit as adjuvant, and **MEV-2**, with human β-defensin 2. Both were evaluated for physicochemical properties, structural quality, TLR4 docking, flexibility, codon-optimised expression in _E. coli_, in silico cloning and simulated immune response.

| Stage                                | Purpose                                                                                | Main tools                                                |
| ------------------------------------ | -------------------------------------------------------------------------------------- | --------------------------------------------------------- |
| 1. Target selection and localization | Choose Pal and confirm it is an outer membrane protein with a cleavable signal peptide | NCBI Protein, MEGA 12 (MUSCLE), PSORTb 3.0.3, SignalP 6.0 |
| 2. Epitope prediction                | Predict B-cell and T-cell epitopes on the mature sequence                              | IEDB: BepiPred-3.0, NetMHCpan EL 4.1, NetMHCIIpan EL      |
| 3. Immunogenic filtering             | Keep antigenic, non-toxic, non-allergenic epitopes                                     | Python, VaxiJen, ToxinPred 3.0, AlgPred 2.0               |
| 4. Construct design                  | Map epitopes and assemble MEV-1 and MEV-2                                              | AlphaFold Server, SignalP 6.0                             |
| 5. Construct evaluation              | Check stability, structure and model quality                                           | ProtParam, SOPMA, AlphaFold Server, SWISS-MODEL           |
| 6. Docking and downstream analyses   | Dock to TLR4, test flexibility, optimise codons, clone, simulate immune response       | HawkDock v2, PyMOL, WEBnm@, Benchling, C-ImmSim           |
