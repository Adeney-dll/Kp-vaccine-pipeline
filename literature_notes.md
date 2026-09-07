<!-- *Klebsiella pneumoniae* -- components are critical to this bacterium’s pathogenicity—the capsule, lipopolysaccharide, fimbriae, and siderophores.
hvKp strains can produce hypercapsules through several specific virulence genes, such as c-rmpA, c-rmpA2, p-rmpA, p-rmpA2, and wzy-K1
two types of fimbriae are widespread in K. pneumoniae strains Type 1 and 3 fimbriae, which are encoded by the fim and mrkABCD operons -->

Outer membrane proteins will be used [ OmpA. LppA, & Pal] 
Choice confirmed, project will target the Peptidoglycan-Associated Lipoprotein (Pal)

   <!-- Abbas, R., Chakkour, M., Dine, H. Z. E., Obaseki, E. F., Obeid, S. T., Jezzini, A., Ghssein, G., & Ezzeddine, Z. (2024). General Overview of Klebsiella pneumonia: Epidemiology and the Role of Siderophores in Its Pathogenicity. Biology, 13(2), 78. https://doi.org/10.3390/biology13020078

    Paczosa, M. K., & Mecsas, J. (2016). Klebsiella pneumoniae: Going on the Offense with a Strong Defense. _Microbiology and Molecular Biology Reviews_, _80_(3), 629–661. https://doi.org/10.1128/mmbr.00078-15

    Zhu, J., Wang, T., Chen, L., & Du, H. (2021). Virulence Factors in Hypervirulent Klebsiella pneumoniae. _Frontiers in Microbiology_, _12_, 642484. https://doi.org/10.3389/fmicb.2021.642484 -->

#### Manuscript Noting
3 articles were used in selecting which protein candidate to use within this project; the main virulent factors of the chosen *Klebsiella pneumoniae* organism (the hypervirulent strain) include the capsule, lipopolysaccharide, fimbriae, and siderophores. For the project, the outer membrane proteins, OmpA. LppA, & Pal, were highlighted, with the Pal protein being the target for the project.

Protein search on NCBI produced over 73,000 results
Targeting only sequences within 170 to 185 aa proteins -- 10 protein sequences retrieved.

Consensus sequence will be obtained via MEGA 12 
All 10 protein sequences were aligned using the MUSCLE algorithm on MEGA 12 with base settings, the consensus sequence was retrieved and placed with raw data.

### Design stage 1
#### GUI tools
1.1 PSORTb v3.0.3: An open source bioinformatics tool that predicts the Subcellular Localization (SCL) of bacterial proteins. It is generally useful for prokaryotes, more advanced cells like in Humans or animals or the ones like malaria can't be analyzed here.
     It reads the amino acids file provided and predicts where on the cell it should be, it is useful in making sure a target protein is exactly where it is needed to be before other analysis can begin.
     PSORTb scores scores potential locations on a scale from 0 to 10. A score of **10.00** on _Outer Membrane_ means the algorithm has maximum confidence that this protein resides on the exterior surface of the cell.
PSORTb scored the consensus sequence a perfect 10, with other components at 0. This validates the sequence is an outer membrane protein.

<!--PSORTb Reference (Yu *et al*., 2010)
    Yu, N. Y., Wagner, J. R., Laird, M. R., Melli, G., Rey, S., Lo, R., Dao, P., Sahinalp, S. C., Ester, M., Foster, L. J., & Brinkman, F. S. L. (2010). PSORTb 3.0: improved protein subcellular localization prediction with refined localization subcategories and predictive capabilities for all prokaryotes. _Bioinformatics_, _26_(13), 1608–1615. https://doi.org/10.1093/bioinformatics/btq249-->