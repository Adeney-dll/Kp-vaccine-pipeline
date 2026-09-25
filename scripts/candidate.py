#mhci filtering
import pandas as pds

def final():
    epitopes = pds.read_csv('data/immunological_filter/mhci.csv')

    candidates = epitopes[
        (epitopes['antigenicity'] == 'antigen')&
        (epitopes['toxicity'] == 'Non-Toxin')&
        (epitopes['allergenicity'] == 'Non-Allergen')&
        (epitopes['immunogenicity'] == 'IMMUNOGEN')
        ]

    output_path = 'results/final_candidates/final_mhci.csv'
    candidates.to_csv(output_path, index=False)

    print(f"Total sequences analyzed: {len(epitopes)}")
    print(f"Final vaccine candidates passing all tests: {len(candidates)}")

if __name__ == "__main__":
    final()
