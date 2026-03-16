def find_missing_records(source_df, target_df):

    source_ids = set(source_df["customer_id"])
    target_ids = set(target_df["id"])

    missing = source_ids - target_ids

    return missing


def find_duplicate_records(source_df):

    duplicates = source_df[source_df.duplicated("email")]

    return duplicates


def find_name_mismatches(source_df, target_df):

    mismatches = []

    for index, row in source_df.iterrows():

        cid = row["customer_id"]

        target_row = target_df[target_df["id"] == cid]

        if not target_row.empty:

            target_name = target_row.iloc[0]["name"]

            if row["name"] != target_name:
                mismatches.append(cid)

    return mismatches