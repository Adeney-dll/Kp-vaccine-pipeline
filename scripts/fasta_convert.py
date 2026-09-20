"""import pandas as pds

def csv_fasta():
    epitopes = pds.read_csv('C:/Users/DELL/Desktop/Programs/Kp-vaccine-pipeline/data/Refined_epitope_values/mhci_filtered_peptides.csv')
    output_file = ('C:/Users/DELL/Desktop/Programs/Kp-vaccine-pipeline/data/Refined_epitope_values/mhci.FASTA')

    with open(output_file, 'w') as file:
        for index, row in epitopes.iterrows():
            file.write(f">Peptide_{index + 1}\n")
            file.write(f"{row['Peptide']}\n")

print("FASTA conversion complete!")

if __name__ == "__main__":
    csv_fasta()"""


import pandas as pds

def csv_fasta():
    epitopes = pds.read_csv('C:/Users/DELL/Desktop/Programs/Kp-vaccine-pipeline/data/Refined_epitope_values/mhcii_filtered_peptides.csv')
    output_file = ('C:/Users/DELL/Desktop/Programs/Kp-vaccine-pipeline/data/Refined_epitope_values/mhcii.FASTA')

    with open(output_file, 'w') as file:
        for index, row in epitopes.iterrows():
            file.write(f">Peptide_{index + 1}\n")
            file.write(f"{row['Peptide']}\n")

print("FASTA conversion complete!")

if __name__ == "__main__":
    csv_fasta()
