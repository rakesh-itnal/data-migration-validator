import pandas as pd

def load_csv_data(file_path):

    df = pd.read_csv(file_path)

    print("CSV data loaded successfully.")

    return df