import pandas as pd
import os

def generate_report(missing, duplicates, mismatches):

    os.makedirs("reports", exist_ok=True)

    summary_data = {
        "Validation Type": [
            "Missing Records",
            "Duplicate Records",
            "Name Mismatches"
        ],
        "Count": [
            len(missing),
            len(duplicates),
            len(mismatches)
        ]
    }

    summary_df = pd.DataFrame(summary_data)

    missing_df = pd.DataFrame({"Missing Customer IDs": list(missing)})
    mismatch_df = pd.DataFrame({"Name Mismatch Customer IDs": mismatches})

    with pd.ExcelWriter("reports/validation_report.xlsx", engine="openpyxl") as writer:

        summary_df.to_excel(writer, sheet_name="Summary", index=False)
        duplicates.to_excel(writer, sheet_name="Duplicate Records", index=False)
        mismatch_df.to_excel(writer, sheet_name="Name Mismatches", index=False)

        workbook = writer.book

        summary_sheet = writer.sheets["Summary"]

        # Adjust column width
        summary_sheet.column_dimensions['A'].width = 25
        summary_sheet.column_dimensions['B'].width = 10

    print("Excel report generated in reports/validation_report.xlsx")