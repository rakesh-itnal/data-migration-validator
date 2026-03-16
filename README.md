# Data Migration Validation Tool

This project is a Python-based tool that validates data consistency during system migrations.

In many real-world software systems, data is often migrated from an old system to a new platform. During this process, issues like missing records, duplicate entries, or mismatched data can occur. This tool simulates that scenario and performs validation checks between source data and target system data.

The goal of this project is to demonstrate how Python can be used to automate migration validation and generate reports that help engineers quickly identify problems.

---

## Features

- Reads source customer data from a CSV file
- Fetches target system data from a REST API
- Detects missing records during migration
- Identifies duplicate records in the dataset
- Finds mismatched records between source and target systems
- Generates an automated Excel validation report

---

## Technologies Used

- Python
- Pandas
- Requests (for API calls)
- OpenPyXL (for Excel report generation)

---

## Project Structure


data-migration-validator

data/
source_customers.csv

src/
load_data.py
fetch_api.py
validator.py
report.py

reports/

main.py
requirements.txt
README.md


---

## How the Project Works

The validation process follows this workflow:

Source System (CSV file)
↓
Migration Process
↓
Target System (API)
↓
Validation Checks
↓
Excel Validation Report

The system performs the following checks:

1. Missing records  
2. Duplicate entries  
3. Data mismatches  

---

## Installation

Clone the repository:


git clone https://github.com/YOUR\_USERNAME/data-migration-validator.git


Navigate into the project folder:


cd data-migration-validator


Create a virtual environment:


python -m venv venv


Activate the environment:


venv\Scripts\activate


Install dependencies:


pip install -r requirements.txt


---

## Running the Project

Run the main script:


python main.py


After running the script, a validation report will be generated inside the **reports** folder.

---

## Example Output

The tool generates an Excel report that summarizes migration validation results.

Example summary:

Validation Type | Count
Missing Records | 1
Duplicate Records | 1
Name Mismatches | 0

---

## What I Learned From This Project

While building this project I learned:

- How to process datasets using pandas
- How to work with REST APIs in Python
- How to perform data validation checks
- How to automate report generation using Python

This project helped me understand how migration validation tools work in real software systems.

---

## Possible Future Improvements

Some improvements that could be added later:

- HTML dashboard for validation reports
- Database migration validation
- Schema validation checks
- Email notifications for migration failures