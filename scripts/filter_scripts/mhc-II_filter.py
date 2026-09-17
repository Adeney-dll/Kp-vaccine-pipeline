import pandas as pds

def top_binders():
    raw_data = pds.read_csv('C:/Users/DELL/Desktop/Programs/Kp-vaccine-pipeline/data/epitope_values/T-helper_epitopes.csv')

    strong_binders = raw_data[raw_data['netmhciipan_el percentile'] <= 10.0].copy()

    unique_peptides = strong_binders['peptide'].drop_duplicates()

    unique_peptides.to_csv('C:/Users/DELL/Desktop/Programs/Kp-vaccine-pipeline/data/Refined_epitope_values/mhcii_filtered_peptides.csv', index=False, header=['Peptide'])

    print(f"Total raw predictions: {len(raw_data)}")
    print(f"Top unique candidates isolated: {len(unique_peptides)}")

if __name__ == "__main__":
    top_binders()
