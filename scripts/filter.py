"""import pandas as pd

def extract_top_binders():
    # 1. Load the raw MHC-I data
    # Ensure the terminal is navigated to your main project directory
    raw_data = pd.read_csv('data/raw/mhci_raw.csv')
    
    # 2. Apply the IEDB biological threshold
    # Column names vary slightly by tool version; verify 'percentile_rank' matches your CSV header
    strong_binders = raw_data[raw_data['percentile_rank'] <= 1.0].copy()
    
    # 3. Isolate the unique sequences 
    unique_peptides = strong_binders['peptide'].drop_duplicates()
    
    # 4. Export the clean, filtered list
    unique_peptides.to_csv('data/raw/mhci_filtered_peptides.csv', index=False, header=['Peptide'])
    
    print(f"Total raw predictions: {len(raw_data)}")
    print(f"Top unique candidates isolated: {len(unique_peptides)}")

if __name__ == "__main__":
    extract_top_binders()
