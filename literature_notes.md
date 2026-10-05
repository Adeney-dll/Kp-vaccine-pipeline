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
     Accepts sequence in fasta format, image result in result_images.
PSORTb scored the consensus sequence a perfect 10, with other components at 0. This validates the sequence is an outer membrane protein.

<!--PSORTb Reference (Yu *et al*., 2010)
    Yu, N. Y., Wagner, J. R., Laird, M. R., Melli, G., Rey, S., Lo, R., Dao, P., Sahinalp, S. C., Ester, M., Foster, L. J., & Brinkman, F. S. L. (2010). PSORTb 3.0: improved protein subcellular localization prediction with refined localization subcategories and predictive capabilities for all prokaryotes. _Bioinformatics_, _26_(13), 1608–1615. https://doi.org/10.1093/bioinformatics/btq249-->

1.2 SignalP v6.0: An advanced machine learning algorithm that reads a sequence and predicts the presence of a signal peptide, if present, then details the type and cleavage site. 
    In a cell, proteins have different places to be upon production, a signal peptide is attached and helps direct the protein to its site then it gets removed. 
    This tool will function as a validation for Psortb, in that, if a signal peptide is identified for this sequence, it shows the protein is actively an outer membrane type that gets transported there and also it helps eliminate the possibility of designing a redundant vaccine targeting a region of the sequence not present in the pathogen within a patient. By identifying the cleavage site within the protein, it will be easy to slice that section and target the parts that actively remain on the cell and within a patient.
SignalP result -- Lipoprotein signal peptide (Sec/SPII) present
             There is a deliberate transporting mechanism for the sequence from the cytoplasm to the outer membrane area, protein is definitely confirmed as an outer membrane protein. 
Cleavage site -- Cleavage site between pos. 21 and 22. 
            Amino acids from 1 to 21 cut off, 22 onwards remains within/upon the cell 
            Probability 0.993814 (over 99% confidence)

<!--SignalP Reference (Nielsen et al., 2024)
    Nielsen, H., Teufel, F., Brunak, S., & Von Heijne, G. (2024). SignalP: The Evolution of a Web Server. In _Methods in molecular biology_ (Vol. 2836, pp. 331–367). https://doi.org/10.1007/978-1-0716-4007-4_17-->

#### Noting
Consensus sequence will now be trimmed from it's original 174 amino acid length to 153.
Trimming was achieved using a short python script. Mature sequence will be used for all future analysis.

### Design stage 2
**NOTE**: Mature Pal sequence probable antigen
#### Epitope Prediction
2.1 The Immune Epitope Database (IEDB) B-cell Prediction Tool on the Next-Generation tool site: IEDB stands as one of the leading platforms for genome analysis, using Bepipred v3.0 prediction method, the platform identifies epitopes or series of peptides able to elicit the reaction of human B-cells.
Residue table, Epitope table and prediction graph were retrieved, parameters were kept at the default.

<!--B-cell reference (Yan *et al*., 2024) General referencing
     Yan, Z., Kim, K., Kim, H., Ha, B., Gambiez, A., Bennett, J., De Almeida Mendes, M. F., Trevizani, R., Mahita, J., Richardson, E., Marrama, D., Blazeska, N., Koşaloğlu-Yalçın, Z., Nielsen, M., Sette, A., Peters, B., & Greenbaum, J. A. (2024). Next-generation IEDB tools: a platform for epitope prediction and analysis. _Nucleic Acids Research_, _52_(W1), W526–W532. https://doi.org/10.1093/nar/gkae407
     
     (Clifford et al., 2022) Bepipred 3.0 reference
     Clifford, J. N., Høie, M. H., Deleuran, S., Peters, B., Nielsen, M., & Marcatili, P. (2022). BepiPred ‐3.0: Improved B‐cell epitope prediction using protein language models. _Protein Science_, _31_(12), e4497. https://doi.org/10.1002/pro.4497-->

2.2 IEDB MHC-I prediction for T-cells: The IEDB platform also aids T-cell epitope prediction. Using the NetMHCpan EL 4.1 algorithm; an advanced machine-learning algorithm powered by artificial neural networks that predicts how strongly a peptide fragment will interact with an MHC Class I molecule.
     All defaults were kept and 27 Human alleles selected for prediction.

<!--T-cell MHC-I reference (Reynisson *et al*., 2020)
     Reynisson, B., Alvarez, B., Paul, S., Peters, B., & Nielsen, M. (2020). NetMHCpan-4.1 and NetMHCIIpan-4.0: improved predictions of MHC antigen presentation by concurrent motif deconvolution and integration of MS MHC eluted ligand data. _Nucleic Acids Research_, _48_(W1), W449–W454. https://doi.org/10.1093/nar/gkaa379-->

2.3  IEDB MHC-II prediction for T-cells: Using the NetMHCIIpan EL 4.1 algorithm; an advanced machine-learning algorithm powered by artificial neural networks that predicts how strongly a peptide fragment will interact with an MHC Class II molecule.
     All defaults were kept and 27 Human alleles selected for prediction.

<!--T-cell MHC-II reference  (Kaabinejadian *et al*., 2022)
     Kaabinejadian, S., Barra, C., Alvarez, B., Yari, H., Hildebrand, W. H., & Nielsen, M. (2022). Accurate MHC motif deconvolution of immunopeptidomics data reveals a significant contribution of DRB3, 4 and 5 to the total DR immunopeptidome. _Frontiers in Immunology_, _13_, 835454. https://doi.org/10.3389/fimmu.2022.835454-->

#### Noting
B and T cell epitopes have been derived and will undergo antigenicity, toxicity, and allergenicity predictions. Only epitopes with a clear antigen score, non toxin, and non allergen will be kept and utilized.

### Design stage 3
Immunogenic filtering
3.1 All epitopes will be filtered to obtain the top binders from the large datasets. These top binders will be subjected to the immunogenic filtering. Top binder acquisition will be achieved using Python scripting.
     The filtering of MHC-I epitopes yielded 37 top binding candidates from a dataset of 3,915 predicted epitopes.
     <!--The scripting was quite a process; in all, several ways to locate and run files within the system or without were analyzed. The scripting file now contains a sub-file for the filtering scripts; one dealing with a more complex code and execution pathway [RP filter] and the other with a relatively simpler one [AP filter], in my opinion.-->
     The filtering of MHC-II epitopes yielded 21 top binding candidates from a dataset of over 756 predicted epitopes.
Top binding candidates were compiled and placed within the refined epitope value sub data file and will undergo immunological testing.

3.2 Top binders will be manually run through vaxijen predictive software for qualities needed.
     Antigenicity was predicted using Vaxijen v2.1 with threshold at 0.3. Epitopes below 6 amino acids were deemed to short to produce viable results. It evaluates whether a sequence can actually provoke the immune system to produce antibodies. 
         <!--(Doytchinova & Flower, 2007)
         Doytchinova, I. A., & Flower, D. R. (2007). VaxiJen: a server for prediction of protective antigens, tumour antigens and subunit vaccines. _BMC Bioinformatics_, _8_(1), 4. https://doi.org/10.1186/1471-2105-8-4-->
    Toxicity was predicted using ToxinPred 3.0
         <!--(Rathore et al., 2024)
         Rathore, A. S., Choudhury, S., Arora, A., Tijare, P., & Raghava, G. P. (2024). ToxinPred 3.0: An improved method for predicting the toxicity of peptides. _Computers in Biology and Medicine_, _179_, 108926. https://doi.org/10.1016/j.compbiomed.2024.108926-->
    Allergenicity was predicted using AlgPred 2.0
         <!--(Sharma et al., 2020)
         Sharma, N., Patiyal, S., Dhall, A., Pande, A., Arora, C., & Raghava, G. P. S. (2020). AlgPred 2.0: an improved method for predicting allergenic proteins and mapping of IgE epitopes. _Briefings in Bioinformatics_, _22_(4). https://doi.org/10.1093/bib/bbaa294-->
    Immunogenicity was predicted using vaxijen 2.0
         <!--(Dimitrov et al., 2020)
         Dimitrov, I., Zaharieva, N., & Doytchinova, I. (2020). Bacterial immunogenicity prediction by machine learning methods. _Vaccines_, _8_(4), 709. https://doi.org/10.3390/vaccines8040709-->
#### NOTE:
Vaxijen 2.1 restricts batch predictions behind a paywall and single analysis is limited to an undisclosed number of proteins (between 10 to 20 probably)

3.3 Final epitope filtering was achieved via python scripting:
     mhci results produced 0 candidates that passed all four criteria out of 37 top binders
     mhcii results produced 5 candidates that passed all four criteria out of 21 top binders
     b-cell results produced 1 candidate that passed all 3 criteria out of 4 top binders


### Design stage 4
3D structure mapping
4.1 Alphafold server: The 3 dimensional structure of the mature Pal outer membrane protein was visualized and confidence score recorded. 
     <!--(Abramson et al., 2024)
     Abramson, J., Adler, J., Dunger, J., Evans, R., Green, T., Pritzel, A., Ronneberger, O., Willmore, L., Ballard, A. J., Bambrick, J., Bodenstein, S. W., Evans, D. A., Hung, C., O’Neill, M., Reiman, D., Tunyasuvunakool, K., Wu, Z., Žemgulytė, A., Arvaniti, E., . . . Jumper, J. M. (2024). Accurate structure prediction of biomolecular interactions with AlphaFold 3. _Nature_, _630_(8016), 493–500. https://doi.org/10.1038/s41586-024-07487-w-->

4.2 Epitope mapping has revealed overlaping regions between epitopes.
     B-cell epitope - visible
     mhcii-1 - visible, overshadowed by mhcii-4 and 5
     mhcii-2 - visible
     mhcii-3 - within B-cell epitope
     mhcii-4 - visible
     mhcii-5 - visible
MEV (Multi-Epitope vaccine) construction will be manual

4.3 MEV design chain 
[Adjuvant] - EAAAK - [MHC-II] - GPGPG - [B-cell] – HHHHHH
Adjuvant -- Cholera enterotoxin subunit B and Human beta-defensin 2
Two vaccine candidates will be constructed, one with each adjuvant. Raw adjuvant protein sequences have been obtained via NCBI and confirmation of signal peptides will be handled via SignalP
CTB result -- Signal peptide (Sec/SPI) present (0.999 likelihood)
              Cleavage site between pos. 21 and 22. (cutting from aa 1 to 21)
HBD-2 result -- Signal peptide (Sec/SPI) present (0.9997 likelihood)
              Cleavage site between pos. 23 and 24. (cutting from aa 1 to 23)

### Design stage 5
Vaccine candidates have been constructed and testing and validation will commence
5.1 Expasy ProtParam: To determine the physiochemical properties of the candidates, the sequences were analyzed via this platform to obtain the following: 
- **Total Number of Amino Acids** 
- **Molecular Weight (MW)** - Provided in Dalton within the files, divide by 1000 to get kDa (kilo-Dalton)
- **Theoretical pI (Isoelectric Point):** The precise pH at which your protein carries a net neutral charge. This dictates exactly what chemical buffers a lab would need to purify your protein using ion-exchange chromatography.
- **Instability Index (II):** The definitive proof of stability. We are looking for this number to drop below 40.0.
- **Aliphatic Index:** This measures the volume occupied by aliphatic side chains (alanine, valine, isoleucine, and leucine). Higher scores indicate high thermostability, meaning the vaccine won't denature at room temperature.
- **GRAVY (Grand Average of Hydropathicity):** A negative score mathematically proves the protein is hydrophilic and will dissolve seamlessly into human blood serum rather than repelling water.
         <!--(Gasteiger et al., 2005)
         Gasteiger, E., Hoogland, C., Gattiker, A., Duvaud, S., Wilkins, M. R., Appel, R. D., & Bairoch, A. (2005). Protein identification and analysis tools on the ExPASY server. In _Humana Press eBooks_ (pp. 571–607). https://doi.org/10.1385/1-59259-890-0:571-->
##### NOTE: Initial analysis produced unstable indexes for both candidates, further editing proved ineffective. The use of a Thioredoxin (Trx) stability tag was implemented.
Thioredoxin (Trx) is a naturally occurring, highly soluble _E. coli_ protein used globally in recombinant biotechnology as a molecular chaperone.
         <!--(LaVallie et al., 1993)
         LaVallie, E. R., DiBlasio, E. A., Kovacic, S., Grant, K. L., Schendel, P. F., & McCoy, J. M. (1993). A Thioredoxin Gene Fusion Expression System That Circumvents Inclusion Body Formation in the E. coli Cytoplasm. _Nature Biotechnology_, _11_(2), 187–193. https://doi.org/10.1038/nbt0293-187-->
Note- The Trx sequence utilized is 109 aa long.
Upon addition of the stabilizer tag, both candidates displayed suitable properties.

Other factors: 
Antigenicity - Probable antigen, Score: 0.5572180025793119 for MEV-1
            Probable antigen, Score: 0.6355006892820295 for MEV-2
Allergenicity - Both non-allergens

| Parameter                        | MEV-1 [CTB] | MEV-2 [HBD-2] |
| -------------------------------- | ----------- | ------------- |
| Expasy Physiochemical properties | -           | +             |
| Antigenicity                     | -           | +             |
