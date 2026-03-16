import requests
import pandas as pd

def fetch_api_data():

    url = "https://jsonplaceholder.typicode.com/users"

    try:
        response = requests.get(url, timeout=10)

        response.raise_for_status()

        data = response.json()

        df = pd.DataFrame(data)

        print("API data fetched successfully.")

        return df

    except requests.exceptions.RequestException as e:

        print("Error fetching API data:", e)

        print("Using fallback sample API data...")

        fallback_data = [
            {"id":1,"name":"John Doe"},
            {"id":2,"name":"Alice Smith"},
            {"id":3,"name":"Bob Brown"},
            {"id":4,"name":"Emma Wilson"}
        ]

        return pd.DataFrame(fallback_data)