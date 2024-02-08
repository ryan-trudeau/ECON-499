import os
import sqlite3
import pandas as pd
import sys
from utils import create_table_from_csv, calculate_null_percentage
import os
sys.path.append('../params/')
from params import repo_dir

# Define the path to your CSV files folder
csv_folder = f'{repo_dir}/data/summary_stats/'

# Create a SQLite database or connect to an existing one
database_name = f'{repo_dir}/data/database_files/null_counts.db'

if os.path.exists(database_name):
    # Delete the database file
    os.remove(database_name)

conn = sqlite3.connect(database_name)


# Loop through CSV files in the folder and create tables
for csv_file in os.listdir(csv_folder):
    if csv_file.endswith('.csv'):
        csv_file_path = os.path.join(csv_folder, csv_file)
        df = create_table_from_csv(csv_file_path,conn)
        print(f"Table created for {csv_file}")

# Commit changes and close the database connection
conn.commit()
conn.close()

print("All CSV files loaded into the SQLite database.")




