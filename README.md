# In silico design of a multi-epitope vaccine candidate against _Klebsiella pneumoniae_ targeting the outer membrane lipoprotein Pal

**Author:** [Name] · **Affiliation:** [Department, Institution] · **Status:** Computational study; no experimental validation

> **Drafting key (delete before publishing).** `[FIGURE n — image]` marks places where an image says more than text. `[TABLE n]` marks content that reads better as a table. Square brackets elsewhere mark details to fill in from your files.

---

## Abstract

Carbapenem-resistant _Klebsiella pneumoniae_ is a critical-priority pathogen on the WHO 2024 bacterial priority list [1]. This repository documents a reproducible reverse-vaccinology workflow built from free web servers and short Python scripts. The peptidoglycan-associated lipoprotein Pal was selected as the target. A consensus sequence from ten _K. pneumoniae_ Pal sequences was checked for localization, B-cell and T-cell epitopes were predicted, and candidates were filtered for antigenicity, toxicity and allergenicity. Five MHC-II epitopes and one B-cell epitope passed all filters. They were joined with one of two adjuvants (cholera toxin B subunit or human β-defensin 2) and a thioredoxin tag to form two constructs, MEV-1 and MEV-2. Both were predicted to be antigenic and non-allergenic, had comparable model quality, and docked to TLR4. All results are predictions and need experimental testing.

## 1. Background

[Two to three sentences on the burden of carbapenem-resistant _K. pneumoniae_ and the state of vaccine development. Add 1–2 citations.]

Outer membrane proteins OmpA, LppA and Pal were compared as candidate antigens using three published studies [2–4]. Pal was chosen because [state the reasons given in those studies, e.g. conservation across strains, reported immunogenicity].

## 2. Methods

All steps used free web servers or short Python scripts (`scripts/`). Raw server outputs are kept unedited in `data/`.

**[TABLE 1] Tools and settings**

|Stage|Tool|Settings and notes|
|---|---|---|
|Sequence retrieval|NCBI Protein|Over 73,000 records returned for [search string]; 10 sequences of 170–185 aa kept|
|Consensus|MUSCLE [5] in MEGA 12 [6]|Default settings; 174-aa consensus|
|Localization|PSORTb 3.0 [7]|Gram-negative setting|
|Signal peptide|SignalP 6.0 [8]|Residues 1–21 removed with a Python script, leaving a 153-aa mature sequence|
|B-cell epitopes|IEDB [9], BepiPred-3.0 [10]|Default parameters|
|MHC-I epitopes|IEDB, NetMHCpan EL 4.1 [11]|27 human alleles; defaults|
|MHC-II epitopes|IEDB, NetMHCIIpan EL [11]|27 human alleles; defaults; [confirm version string in the result file]|
|Top-binder selection|Python script|[state the cut-off, e.g. %rank threshold]|
|Antigenicity|VaxiJen [12]|Threshold 0.3; peptides under 6 aa excluded|
|Toxicity|ToxinPred 3.0 [13]|[model and threshold]|
|Allergenicity|AlgPred 2.0 [14]|[model and threshold]|
|Physicochemical properties|ExPASy ProtParam [15]|Instability index below 40 taken as stable|
|Secondary structure|SOPMA [16]|Default settings|
|Tertiary structure|AlphaFold Server [17]|Confidence scores recorded|
|Model assessment|SWISS-MODEL structure assessment [18]|Ramachandran, MolProbity, clashscore, QMEANDisCo|
|Docking|HawkDock [19]; PyMOL|TLR4 [PDB ID], chain A only; [state HawkDock version]|

**Construct design.** Constructs were assembled manually in the order _adjuvant – EAAAK – MHC-II epitopes – GPGPG – B-cell epitope – HHHHHH_. MEV-1 used cholera toxin B subunit and MEV-2 used human β-defensin 2. Adjuvant signal peptides (positions 1–21 and 1–23, respectively) were removed after SignalP analysis. Both initial constructs gave an instability index above 40, so a 109-aa _E. coli_ thioredoxin tag was added at [position]. [State the linker used between MHC-II epitopes.]

> **[FIGURE 1 — image]** Workflow diagram: one box per stage (retrieval → localization → epitope prediction → filtering → construct design → structure → docking), each labelled with its tool and the number of sequences or epitopes remaining. _This can replace most of the Methods prose if you want it shorter._

## 3. Results

### 3.1 Target and localization

PSORTb assigned the consensus sequence to the outer membrane with a score of 10.00, and all other sites scored 0. SignalP 6.0 predicted a lipoprotein (Sec/SPII) signal peptide with a probability of 0.994 and a cleavage site between positions 21 and 22. These results are consistent with an outer membrane lipoprotein.

> **[FIGURE 2 — image]** Two panels side by side: the PSORTb result graphic and the SignalP 6.0 probability plot with the cleavage site marked. Use the screenshots in your `result_images` folder. _Do not describe these in text beyond the two sentences above._

### 3.2 Epitope screening

Epitope prediction produced 3,915 MHC-I and [756 — confirm exact count] MHC-II peptides. After top-binder selection and the antigenicity, toxicity and allergenicity filters, no MHC-I epitope remained, five MHC-II epitopes remained, and one of four B-cell epitopes remained.

> **[FIGURE 3 — image]** Funnel or stacked bar chart showing the counts at each filtering step for the three epitope classes (predicted → top binders → passed all filters). _A short script with matplotlib can generate this from your result files._

**[TABLE 2] Final epitopes.** Columns: ID, class, sequence, position, VaxiJen score, toxicity call, allergenicity call. _Keep as a table; sequences are hard to read in prose._

### 3.3 Epitope location on Pal

Several epitopes overlap. The MHC-II epitope mhcii-3 lies within the B-cell epitope, and mhcii-1 is partly covered by mhcii-4 and mhcii-5.

> **[FIGURE 4 — image]** PyMOL render of the AlphaFold model of mature Pal with each epitope in a different colour and a legend. _This is the clearest way to show the overlaps; the sentence above can then be shortened._

### 3.4 Vaccine constructs

> **[FIGURE 5 — image]** Linear schematic of MEV-1 and MEV-2 as coloured blocks (tag, adjuvant, EAAAK, MHC-II epitopes, GPGPG, B-cell epitope, His-tag) with residue numbers. _Draw this in any vector tool (for example Inkscape or diagrams.net)._

**[TABLE 3] Predicted properties.** Columns: construct, length, molecular weight, pI, instability index (before and after the thioredoxin tag), aliphatic index, GRAVY, VaxiJen score, allergenicity. VaxiJen scores were 0.557 (MEV-1) and 0.636 (MEV-2); both constructs were predicted to be non-allergens. [Fill the remaining values from your ProtParam files.]

### 3.5 Structure assessment

**[TABLE 4] Model quality**

|Parameter|MEV-1 (CTB)|MEV-2 (HBD-2)|
|---|---|---|
|Ramachandran favoured|92.45%|91.02%|
|MolProbity score|1.95|2.00|
|Clashscore|4.95|3.93|
|QMEANDisCo global|0.58 ± 0.05|0.53 ± 0.05|
|QMEAN Z-score|−1.96|−1.20|

> **[FIGURE 6 — image]** The two AlphaFold models (coloured by domain) next to their Ramachandran plots from SWISS-MODEL. _Put the numbers in Table 4, not in the figure caption._

### 3.6 Docking with TLR4

**[TABLE 5] HawkDock results**

|Complex|HawkDock score|MM/GBSA binding free energy (kcal/mol)|
|---|---|---|
|MEV-1 – TLR4|−5323.90|−24.05|
|MEV-2 – TLR4|−3867.47|−51.36|

MEV-1 had the more negative docking score, whereas MEV-2 had the lower MM/GBSA binding free energy. [State which measure you give more weight to and why.]

> **[FIGURE 7 — image]** PyMOL renders of both complexes (TLR4 in one colour, construct in another) with a zoomed inset of the interface and the main contacts labelled. _Add the contact table from your PyMOL analysis as a supplementary file._

## 4. Limitations

- Pal sits in the inner leaflet of the outer membrane and faces the periplasm, so antibody access to its epitopes on an intact cell is uncertain [cite a source on Pal topology].
- No MHC-I epitope passed the filters, so the constructs contain no predicted CD8⁺ T-cell epitopes. [State whether thresholds were varied.]
- VaxiJen was developed for whole proteins, so scores for short peptides should be read with caution. [Give the reason for using 0.3 rather than the default 0.4 for bacterial targets.]
- TLR4 was docked as a monomer without MD-2, which limits how far the binding energies can be interpreted. Docking scores are not measured affinities.
- The thioredoxin tag was needed to bring the instability index below 40, so the stability prediction depends on the tag.
- Every result comes from web-server predictions. Expression, immunogenicity assays and challenge studies would be needed to test the candidates.

## 5. Reproducing this work

Repository layout: `data/` (sequences and raw server outputs), `scripts/` ([list scripts and what each does]), `results/` (filtered tables and figures). Install dependencies with `pip install -r requirements.txt`, then run [commands in order]. Web-server job links can expire, so the exported result files in `data/` are the permanent record.