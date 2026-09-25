#b-cell filtering
import pandas as pds

def final():
    epitopes = pds.read_csv('data/immunological_filter/B-Cell.csv')

    candidates = epitopes[
        (epitopes['antigenicity'] == 'Probable antigen.')&
        (epitopes['toxicity'] == 'Non-Toxin')&
        (epitopes['allergenicity'] == 'Probable NON-ALLERGEN')
        ]

    output_path = 'results/final_candidates/final_bcell.csv'
    candidates.to_csv(output_path, index=False)

    print(f"Total sequences analyzed: {len(epitopes)}")
    print(f"Final vaccine candidates passing all tests: {len(candidates)}")

if __name__ == "__main__":
    final()

