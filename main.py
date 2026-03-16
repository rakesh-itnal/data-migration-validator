from src.load_data import load_csv_data
from src.fetch_api import fetch_api_data
from src.validator import find_missing_records
from src.validator import find_duplicate_records
from src.validator import find_name_mismatches
from src.report import generate_report

def main():

    source_df = load_csv_data("data/source_customers.csv")

    target_df = fetch_api_data()

    missing = find_missing_records(source_df, target_df)

    duplicates = find_duplicate_records(source_df)

    mismatches = find_name_mismatches(source_df, target_df)

    generate_report(missing, duplicates, mismatches)

if __name__ == "__main__":
    main()