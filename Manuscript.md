## In silico design of a multi-epitope vaccine candidate against *Klebsiella pneumoniae* targeting the outer membrane lipoprotein Pal

Fatuyi Adene Adeniyi · Computational Biology Researcher · [27 / 10 / 2026]

<!-- This file holds the full methods, numbers and references. The README carries only the headline results and images. -->

---

#### Abstract
*Klebsiella pneumoniae* remains one of world's most significant organisms, it's high pathogenicity inducing numerous diseases, such as liver abscesses, bacteremias, pneumonia, and urinary tract infections, which constitute a major threat to hospitals catering to the immunocompromised and the community. No licensed vaccine is available.
Using a reverse-vaccinology workflow, built from free web servers and short Python filtering scripts, to design a multi-epitope vaccine against the outer membrane lipoprotein Pal. A consensus of ten Pal sequences was confirmed as an outer membrane lipoprotein (PSORTb outer membrane score 10.00; SignalP 6.0 Sec/SPII signal peptide, cleavage after residue 21). B-cell, MHC-I and MHC-II epitopes were predicted and filtered for antigenicity, toxicity and allergenicity (and immunogenicity for MHC-II). Two constructs were assembled, one with cholera toxin B subunit (MEV-1) and one with human β-defensin 2 (MEV-2) as adjuvant, each with a thioredoxin tag.
One B-cell and five MHC-II epitopes passed all filters; none of the 37 MHC-I candidates did. Both constructs had instability indices below 40 (32.29 and 31.75) and more than 91% of residues in favoured Ramachandran regions. Docking to TLR4 gave binding free energies of −24.05 kcal/mol (MEV-1) and −51.36 kcal/mol (MEV-2). Codon optimisation raised GC content from 31.1% to 49.9% and from 33.3% to 52.5%, and both genes were cloned virtually into pET-28a(+). Immune simulation predicted a substantial rise in memory response.
Both constructs meet the computational criteria applied here and are candidates for further testing. All results are predictions; no laboratory validation was done.

---

#### Introduction
_Klebsiella pneumoniae_ is a Gram-negative bacterium that causes pneumonia, urinary tract infections and bloodstream infections, mainly in hospitalised and immunocompromised patients **[1]**. Hypervirulent strains add invasive community-acquired disease **[2]**. Its virulence depends on the capsule, lipopolysaccharide, fimbriae and siderophores **[1–2]**. As treatment options narrow, prevention becomes more attractive, yet no licensed vaccine exists.

Capsule and lipopolysaccharide vary widely between isolates, which makes them difficult vaccine targets. Outer membrane proteins are generally more conserved. The Pal protein is one of these: a lipoprotein anchored in the outer membrane that links it to the peptidoglycan layer. Other outer membrane proteins were assessed such as: OmpA and LppA, the Pal protein was settled on due to sparse literature on reverse vaccinology on this target **[3]**.

Multi-epitope vaccines join selected B-cell and T-cell epitopes with short linkers and an adjuvant, giving a small, defined antigen that can be produced in _E. coli_. Computational pipelines allow many candidates to be screened before any laboratory work. Here such pipeline was applied to Pal, two constructs were designed that differ in adjuvant, and evaluated for stability, structure, TLR4 binding, expression design and simulated immune response. The work is computational only and does not test the vaccines experimentally.


#### Methods
Table 1. Tools and settings

| Step                     | Tool             | Version | Settings                                                      | Ref       |
| ------------------------ | ---------------- | ------- | ------------------------------------------------------------- | --------- |
| Sequence retrieval       | NCBI Protein     |         | Klebsiella pneumoniae Pal ATCC 13883"; 170–185 aa; n = 10     | [4]       |
| Alignment                | MEGA 12 (MUSCLE) | 12      | defaults                                                      | [5] [6]   |
| Localisation             | PSORTb           | 3.0.3   | Gram-negative                                                 | [7]       |
| Signal peptide           | SignalP          | 6.0     | Sec/SPII                                                      | [8]       |
| B-cell epitopes          | IEDB BepiPred    | 3.0     | defaults                                                      | [9]       |
| MHC-I                    | NetMHCpan EL     | 4.1     | 27 alleles                                                    | [10]      |
| MHC-II                   | NetMHCIIpan EL   | 4.1     | 27 alleles                                                    | [10] [11] |
| Antigenicity             | VaxiJen          | 2.1     | threshold 0.3                                                 | [12]      |
| Toxicity                 | ToxinPred        | 3.0     | defaults                                                      | [13]      |
| Allergenicity            | AlgPred          | 2.0     | defaults                                                      | [14]      |
| Immunogenicity           | Vaxijen          | 2.0     | defaults                                                      | [15]      |
| 3D structure             | AlphaFold        | 3       |                                                               | [16]      |
| Physicochemical Property | ExPASy ProtParam |         |                                                               | [17]      |
| Secondary structure      | SOPMA            |         |                                                               | [18]      |
| Structure assessment     | SWISS-MODEL      |         |                                                               | [19]      |
| Docking                  | HawkDock         | 2       | TLR4 chain A, PDB 4G8A                                        | [20] [21] |
| Flexibility              | WEBnm@           | 2.0     |                                                               | [22]      |
| Codon optimisation       | DNA Chisel       |         | E. coli; GC 40–65%; max homopolymer 7 nt                      | [23]      |
| In silico cloning        | Benchling        |         | pET-28a(+), NdeI/XhoI                                         | [24]      |
| Immune simulation        | C-ImmSim         |         | volume 20; seed 12345; 1,000 steps; doses at steps 1, 84, 168 | [25] [26] |

##### Construct assembly
<!-- NEW FIGURE: construct schematic (Fig. 3) with residue ranges. -->
Epitope order, linkers (EAAAK between adjuvant and epitopes, GPGPG between epitopes), His-tag.
Adjuvant sequences (accession numbers) with signal peptides removed (CTB: residues 1–21; HBD-2: 1–23).
Thioredoxin tag (109 aa): position in the construct, reason for adding it, and whether it stays in the final candidate [15].
Whether the 6xHis-tag was removed for the C-ImmSim input, and whether Trx was kept.
2.2 Acceptance criteria
<!-- One short table of the thresholds you used, with a source for each. This lets the Results pass/fail table stand alone. -->
Metric	Threshold	Source
Instability index	< 40	[ref]
Ramachandran favoured	> 90%	[ref]
MolProbity	< 2.0	[ref]
Clashscore	< 5.0	[ref]
QMEANDisCo global	[about 0.6]	[ref]
QMEAN Z-score	between −2 and +2	[ref]
<!-- The notes describe these metrics with words like "proves" and "same quality as a crystal structure". Use "is consistent with" instead. -->
3. Results
3.1 Target selection and mature sequence
<!-- Fig. 2: MEGA alignment; SignalP plot. Short text: 10 sequences, 174 aa consensus, outer membrane score 10.00, signal peptide cleavage 21/22, mature 153 aa. -->
3.2 Epitope prediction and filtering
<!-- Fig. 4: funnel chart (new). Table 2: the six passing epitopes. -->
Counts at each step, per class.
Which criterion removed the MHC-I candidates.
Position of each retained epitope on the mature sequence, and the overlap noted in the notes (mhcii-3 lies inside the B-cell epitope; mhcii-1 is partly covered by mhcii-4 and mhcii-5). Say how the overlap was handled in the construct.
3.3 Construct properties
<!-- Table 3: ProtParam (length, MW, pI, instability, aliphatic, GRAVY) for both constructs, before and after adding Trx. Showing the pre-Trx values is the clearest way to justify the tag. The raw values are not in the current README. --> <!-- Fig. 5: AlphaFold models with pLDDT colouring. Table 4: SOPMA percentages. -->
3.4 Structural validation
<!-- Table 5: your SWISS-MODEL table, with a pass/borderline column against Section 2.2. Borderline items at present: MEV-2 MolProbity 2.00; MEV-1 clashscore 4.95; QMEAN Z for MEV-1 (−1.96); QMEANDisCo 0.58 and 0.53 against a reference near 0.6. -->
3.5 Docking with TLR4
<!-- Fig. 6: complexes. Table 6: docking score and ΔG; residue table in an appendix or <details> block. -->
Report the two metrics separately and say which one supports the conclusion.
State which parts of each construct contact the receptor (adjuvant, epitope, linker or tag).
3.6 Flexibility, codon optimisation and cloning
<!-- Fig. 7: normal mode plots. Table 7: codon optimisation (include 972 and 786 bp inserts and the 5,289 bp backbone). Fig. 8: plasmid maps. -->
One sentence interpreting the normal mode values.
Digest and ORF checks: fragment sizes, in-frame with T7 promoter, no premature stop.
3.7 Simulated immune response
<!-- Fig. 9: C-ImmSim panels A to F for each construct (the README shows one combined image per construct). -->
What differed between MEV-1 and MEV-2 in antibody titre, B-cell memory, T-helper and cytotoxic T-cell counts, and cytokines.
4. Discussion
Which construct is the better lead, and why (use the pass/borderline table).
What the Trx tag does to the design: stability gain versus a large non-epitope component.
How the findings compare with published in silico Klebsiella vaccine designs [add two or three references].
Next steps: BLASTp of the epitopes against the human proteome, conservation across more K. pneumoniae genomes, population coverage, molecular dynamics, expression test.
<!-- Reviewers of this kind of study usually ask for the human-proteome check and conservation analysis; mention them even if not done. -->
5. Limitations
Computational only; no expression, safety or immunogenicity data.
Prediction tools depend on their training data; several score thresholds are conventions, not proofs.
Docking used a TLR4 monomer without MD-2; no reference docking for comparison.
C-ImmSim used default HLA alleles and a generic host.
6. Conclusion

[Two sentences, no new claims.]

Data and code availability

Scripts, inputs and raw outputs: scripts/, data/, results/ in this repository.

Figure plan
Fig.	Content	File	Status
1	Workflow	results/Workflow-chart.png	exists
2	Alignment and SignalP	results/raw_images/, results/	exists, rename files
3	Construct schematic	results/Construct_schematic.png	to make
4	Epitope funnel	results/Epitope_funnel.png	to make
5	AlphaFold and SOPMA	results/Structures/	exists, add pLDDT
6	Docking complexes	results/Structures/Docking/	exists
7	Normal modes	results/Normal-mode-analysis/	exists
8	Plasmid maps	results/Cloning/	exists
9	Immune simulation	results/Immune-Simulation/	exists


#### References
[1] Abbas, R., Chakkour, M., Dine, H. Z. E., Obaseki, E. F., Obeid, S. T., Jezzini, A., Ghssein, G., & Ezzeddine, Z. (2024). General Overview of Klebsiella pneumonia: Epidemiology and the Role of Siderophores in Its Pathogenicity. Biology, 13(2), 78. https://doi.org/10.3390/biology13020078

[2] Zhu, J., Wang, T., Chen, L., & Du, H. (2021). Virulence Factors in Hypervirulent Klebsiella pneumoniae. _Frontiers in Microbiology_, _12_, 642484. https://doi.org/10.3389/fmicb.2021.642484

[3] Paczosa, M. K., & Mecsas, J. (2016). Klebsiella pneumoniae: Going on the Offense with a Strong Defense. _Microbiology and Molecular Biology Reviews_, _80_(3), 629–661. https://doi.org/10.1128/mmbr.00078-15

[4] Sayers, E. W., Bolton, E. E., Fine, A. M., Kelly, C., Kim, S., Landrum, M., Lathrop, S., Malheiro, A., Murphy, T. D., Phan, L., Pujar, S., Trawick, B. W., Schneider, V. A., & Pruitt, K. D. (2025). Database resources of the National Center for Biotechnology Information in 2026. _Nucleic Acids Research_, _54_(D1), D20–D27. https://doi.org/10.1093/nar/gkaf1060

[5] Kumar, S., Stecher, G., Suleski, M., Sanderford, M., Sharma, S., & Tamura, K. (2024). MEGA12: Molecular Evolutionary Genetic Analysis Version 12 for Adaptive and Green Computing. _Molecular Biology and Evolution_, _41_(12). https://doi.org/10.1093/molbev/msae263

[6] Edgar, R. C. (2004). MUSCLE: multiple sequence alignment with high accuracy and high throughput. _Nucleic Acids Research_, _32_(5), 1792–1797. https://doi.org/10.1093/nar/gkh340

[7] Yu, N. Y., Wagner, J. R., Laird, M. R., Melli, G., Rey, S., Lo, R., Dao, P., Sahinalp, S. C., Ester, M., Foster, L. J., & Brinkman, F. S. L. (2010). PSORTb 3.0: improved protein subcellular localization prediction with refined localization subcategories and predictive capabilities for all prokaryotes. _Bioinformatics_, _26_(13), 1608–1615. https://doi.org/10.1093/bioinformatics/btq249

[8] Nielsen, H., Teufel, F., Brunak, S., & Von Heijne, G. (2024). SignalP: The Evolution of a Web Server. In _Methods in molecular biology_ (Vol. 2836, pp. 331–367). https://doi.org/10.1007/978-1-0716-4007-4_17

[9] Yan, Z., Kim, K., Kim, H., Ha, B., Gambiez, A., Bennett, J., De Almeida Mendes, M. F., Trevizani, R., Mahita, J., Richardson, E., Marrama, D., Blazeska, N., Koşaloğlu-Yalçın, Z., Nielsen, M., Sette, A., Peters, B., & Greenbaum, J. A. (2024). Next-generation IEDB tools: a platform for epitope prediction and analysis. _Nucleic Acids Research_, _52_(W1), W526–W532. https://doi.org/10.1093/nar/gkae407

[10] Reynisson, B., Alvarez, B., Paul, S., Peters, B., & Nielsen, M. (2020). NetMHCpan-4.1 and NetMHCIIpan-4.0: improved predictions of MHC antigen presentation by concurrent motif deconvolution and integration of MS MHC eluted ligand data. _Nucleic Acids Research_, _48_(W1), W449–W454. https://doi.org/10.1093/nar/gkaa379

[11] Kaabinejadian, S., Barra, C., Alvarez, B., Yari, H., Hildebrand, W. H., & Nielsen, M. (2022). Accurate MHC motif deconvolution of immunopeptidomics data reveals a significant contribution of DRB3, 4 and 5 to the total DR immunopeptidome. _Frontiers in Immunology_, _13_, 835454. https://doi.org/10.3389/fimmu.2022.835454

[12] Doytchinova, I. A., & Flower, D. R. (2007). VaxiJen: a server for prediction of protective antigens, tumour antigens and subunit vaccines. _BMC Bioinformatics_, _8_(1), 4. https://doi.org/10.1186/1471-2105-8-4

[13] Rathore, A. S., Choudhury, S., Arora, A., Tijare, P., & Raghava, G. P. (2024). ToxinPred 3.0: An improved method for predicting the toxicity of peptides. _Computers in Biology and Medicine_, _179_, 108926. https://doi.org/10.1016/j.compbiomed.2024.108926

[14] Sharma, N., Patiyal, S., Dhall, A., Pande, A., Arora, C., & Raghava, G. P. S. (2020). AlgPred 2.0: an improved method for predicting allergenic proteins and mapping of IgE epitopes. _Briefings in Bioinformatics_, _22_(4). https://doi.org/10.1093/bib/bbaa294

[15] Dimitrov, I., Zaharieva, N., & Doytchinova, I. (2020). Bacterial immunogenicity prediction by machine learning methods. _Vaccines_, _8_(4), 709. https://doi.org/10.3390/vaccines8040709

[16] Abramson, J., Adler, J., Dunger, J., Evans, R., Green, T., Pritzel, A., Ronneberger, O., Willmore, L., Ballard, A. J., Bambrick, J., Bodenstein, S. W., Evans, D. A., Hung, C., O’Neill, M., Reiman, D., Tunyasuvunakool, K., Wu, Z., Žemgulytė, A., Arvaniti, E., . . . Jumper, J. M. (2024). Accurate structure prediction of biomolecular interactions with AlphaFold 3. _Nature_, _630_(8016), 493–500. https://doi.org/10.1038/s41586-024-07487-w

[17] Gasteiger, E., Hoogland, C., Gattiker, A., Duvaud, S., Wilkins, M. R., Appel, R. D., & Bairoch, A. (2005). Protein identification and analysis tools on the ExPASY server. In _Humana Press eBooks_ (pp. 571–607). https://doi.org/10.1385/1-59259-890-0:571

[18] Geourjon, C., & Deléage, G. (1995). SOPMA: significant improvements in protein secondary structure prediction by consensus prediction from multiple alignments. _Computer Applications in the Biosciences_, _11_(6), 681–684. https://doi.org/10.1093/bioinformatics/11.6.681

[19] Waterhouse, A. M., Studer, G., Robin, X., Bienert, S., Tauriello, G., & Schwede, T. (2024). The structure assessment web server: for proteins, complexes and more. _Nucleic Acids Research_, _52_(W1), W318–W323. https://doi.org/10.1093/nar/gkae270

[20] Berman, H. M. (2000). The Protein Data Bank. _Nucleic Acids Research_, _28_(1), 235–242. https://doi.org/10.1093/nar/28.1.235

[21] Zhang, X., Jiang, L., Weng, G., Shen, C., Zhang, O., Liu, M., Zhang, C., Gu, S., Wang, J., Wang, X., Du, H., Zhang, H., Zhang, K., Wang, E., & Hou, T. (2025). HawkDock version 2: an updated web server to predict and analyze the structures of protein–protein complexes. _Nucleic Acids Research_, _53_(W1), W306–W315. https://doi.org/10.1093/nar/gkaf379

[22] Tiwari, S. P., Fuglebakk, E., Hollup, S. M., Skjærven, L., Cragnolini, T., Grindhaug, S. H., Tekle, K. M., & Reuter, N. (2014). WEBnm@ v2.0: Web server and services for comparing protein flexibility. _BMC Bioinformatics_, _15_(1), 427. https://doi.org/10.1186/s12859-014-0427-6

[23] Zulkower, V., & Rosser, S. (2020). DNA Chisel, a versatile sequence optimizer. _Bioinformatics_, _36_(16), 4508–4509. https://doi.org/10.1093/bioinformatics/btaa558

[24] Benchling. (2026).

[25] Rapin, N., Lund, O., & Castiglione, F. (2011). Immune system simulation online. _Bioinformatics_, _27_(14), 2013–2014. https://doi.org/10.1093/bioinformatics/btr335

[26] Basak, S., Deb, D., Narsaria, U., Kar, T., Castiglione, F., Sanyal, I., Bade, P. D., & Srivastava, A. P. (2021). In silico designing of vaccine candidate against Clostridium difficile. _Scientific Reports_, _11_(1), 14215. https://doi.org/10.1038/s41598-021-93305-6


