import pandas as pd
import sqlite3
import sys
import os

sys.path.append('../params/')
from params import repo_dir

# Read the Excel file
excel_file = f'{repo_dir}/documentation/Pitchbook Data Dictionary.xlsx'

df = pd.read_excel(excel_file,sheet_name=None, skiprows=4)

# Create a SQLite database
database_name = f'{repo_dir}/data/database_files/schema_description.db'
if os.path.exists(database_name):
    # Delete the database file
    os.remove(database_name)

conn = sqlite3.connect(database_name)
cursor = conn.cursor()

def create_table_from_pandas_df(df: pd.DataFrame, table_name: str, conn) -> pd.DataFrame:
   
    df.to_sql(table_name, conn, if_exists='replace', index=False)

# Iterate over each sheet in the Excel file
for sheet_name, sheet_data in df.items():
    if sheet_name not in ['TrackingChanges', 'Summary']:
        nulls_file = f'{repo_dir}/data/summary_stats/{sheet_name}_nulls.csv'
        if not os.path.exists(nulls_file):
            files = os.listdir(f'{repo_dir}/data/summary_stats')
            for file in files:
                if file.startswith(sheet_name):
                    nulls_file = f'{repo_dir}/data/summary_stats/{file}'
                    break
        df_nulls = pd.read_csv(nulls_file)
        extracted_data = sheet_data.merge(df_nulls, on='Column Name', how='left')
        n = df_nulls[df_nulls['Column Name'] == 'row count']['% Nulls'].values[0]
        extracted_data['Obesrvations'] = n
        # Extract data starting from row 5
        # extracted_data = rename_columns(sheet_data)
        # Set the table name as the sheet name
        table_name = sheet_name.replace(' ', '_')
        print("Creating table for", table_name)
        create_table_from_pandas_df(extracted_data, table_name, conn)

# Commit the changes and close the connection
conn.commit()
conn.close()



