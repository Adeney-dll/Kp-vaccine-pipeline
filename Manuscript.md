### In silico design of a multi-epitope vaccine candidate against Klebsiella pneumoniae targeting the outer membrane lipoprotein Pal

Fatuyi Adene Adeniyi · Computational Biology Researcher · [27 / 10 / 2026]

<!-- This file holds the full methods, numbers and references. The README carries only the headline results and images. Lines in comment tags are notes to yourself and do not show on GitHub. Target length: 4 to 6 pages. -->
Abstract

Background. [Why K. pneumoniae needs a vaccine: one sentence.] Approach. [Pal as target; reverse vaccinology; two constructs, one per adjuvant.] Findings. [Three or four numbers: epitopes retained (5 MHC-II, 1 B-cell, 0 MHC-I); both constructs under instability index 40; ΔG values; both predicted to raise memory responses.] Conclusion. [One cautious sentence. Computational only.]

1. Introduction
<!-- Three short paragraphs. -->
K. pneumoniae burden and antimicrobial resistance [cite 1, 2].
Why an outer membrane target, and why Pal rather than OmpA or LppA [cite 3 and any Pal-specific work].
Aim: design and computationally evaluate two Pal-based multi-epitope constructs.
<!-- CLARIFY: say whether the work concerns hypervirulent or classical strains. The search string (ATCC 13883) points to the classical type strain. -->
2. Methods

Table 1. Tools, versions and settings (fill the last two columns; add the access date for each web server)

Step	Tool	Version / date	Settings	Ref
Sequence retrieval	NCBI Protein	[date]	"Klebsiella pneumoniae Pal ATCC 13883"; 170–185 aa; n = 10	
Alignment, consensus	MEGA 12 (MUSCLE)	12	defaults	[add MEGA12 and MUSCLE]
Localisation	PSORTb	3.0.3	Gram-negative	[4]
Signal peptide	SignalP	6.0	[organism group]	[5; also cite the SignalP 6.0 paper]
B-cell epitopes	IEDB BepiPred	3.0	defaults	[6, Clifford 2022]
MHC-I	NetMHCpan EL	4.1	27 alleles	[7]
MHC-II	NetMHCIIpan EL	4.1	27 alleles	[7, 8]
Top-binder filter	Python script	[file]	[rank or percentile cut-off]	
Antigenicity	VaxiJen	2.1	threshold 0.3 [reason]	[9]
Toxicity	ToxinPred	3.0	[model]	[10]
Allergenicity	AlgPred	2.0	[model]	[11]
Immunogenicity	[tool]	[version]		[12]
3D structure	AlphaFold	3 (server)		[13]
Physicochemical	ExPASy ProtParam			[14]
Secondary structure	SOPMA		[window, similarity threshold]	[16]
Structure assessment	SWISS-MODEL			[17]
Docking	HawkDock	2	TLR4 chain A, PDB 4G8A	[18, 20]
Flexibility	WEBnm@	2.0		[21]
Codon optimisation	[37° tool or DNA Chisel]		E. coli; GC 40–65%; max homopolymer 7 nt	[22]
In silico cloning	Benchling		pET-28a(+), NdeI/XhoI	[23]
Immune simulation	C-ImmSim		volume 20; seed 12345; 1,000 steps; doses at steps 1, 84, 168	[24, 25]
2.1 Construct assembly
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
References
<!-- Number in order of first citation, and put the matching [n] in the text. In the current README the list starts [1],[2],[3],[15] and then jumps to [4]; the text has no citation markers. Still missing: MEGA 12, MUSCLE, BepiPred 3.0 (in the notes comments, not in the README list), the SignalP 6.0 paper, CTB and HBD-2 sources, TLR4 structure paper for 4G8A, and the Benchling entry (add publisher and URL). Check each DOI before committing. -->

[Paste the verified list here.]
