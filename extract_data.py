import os
import sqlite3
import pandas as pd

from utils import create_table_from_csv, calculate_null_percentage
import sys
import os

def find_and_write_directory():
    """
    Find the repository directory and write it to a params file.
    """
    repo_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    params_file = os.path.join(repo_dir, "params", "params.py")
    
    with open(params_file, "w") as file:
        file.write(f"repo_dir = \"{repo_dir}\"")
find_and_write_directory()

sys.path.append('../params/')
from params import repo_dir


# Define the path to your CSV files folder
csv_folder = f'{repo_dir}/data/raw/'

# Create directories if they don't exist
directories = [f'{repo_dir}/data/exports', f'{repo_dir}/data/database_files', f'{repo_dir}/data/summary_stats']
for directory in directories:
    print("Creating directory", directory)
    os.makedirs(directory, exist_ok=True)

# Create a SQLite database or connect to an existing one
db_file = f'{repo_dir}/data/database_files/pitchbook.db'
conn = sqlite3.connect(db_file)


# Loop through CSV files in the folder and create tables
for csv_file in os.listdir(csv_folder):
    if csv_file.endswith('.csv'):
        csv_file_path = os.path.join(csv_folder, csv_file)
        df = create_table_from_csv(csv_file_path,conn)
        print(f"Table created for {csv_file}")

        calculate_null_percentage(df, f"{repo_dir}/data/summary_stats/{csv_file.replace('.csv','')}_nulls.csv")

# Commit changes and close the database connection
conn.commit()
conn.close()

print("All CSV files loaded into the SQLite database.")




