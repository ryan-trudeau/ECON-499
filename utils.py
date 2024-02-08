import os
import pandas as pd

def create_table_from_csv(csv_file: str, conn) -> pd.DataFrame:
    """
    Function to determine the schema of a CSV file and create a table.

    Parameters:
    csv_file (str): The path to the CSV file.
    conn: The connection object to the database.

    Returns:
    pd.DataFrame: The DataFrame created from the CSV file.
    """
    table_name = os.path.splitext(os.path.basename(csv_file))[0]
    df = pd.read_csv(csv_file)  
    df.to_sql(table_name, conn, if_exists='replace', index=False)

    return df

def create_table_from_pandas_df(df: pd.DataFrame, table_name: str, conn) -> pd.DataFrame:
   
    df.to_sql(table_name, conn, if_exists='replace', index=False)


def calculate_null_percentage(df: pd.DataFrame, output_csv: str):
    """
    Calculate the percentage of null values in each column of a DataFrame.

    Parameters:
    df (pd.DataFrame): The DataFrame to calculate null percentages for.
    output_csv (str): The path to save the result DataFrame as a CSV file.
    """
    total_rows = len(df)
    column_names = []
    null_percentages = []

    for col in df.columns:
        null_count = df[col].isnull().sum()
        null_percentage = (null_count / total_rows) * 100

        column_names.append(col)
        null_percentages.append(null_percentage)

    column_names.insert(0, 'row count')
    null_percentages.insert(0, total_rows)

    result_df = pd.DataFrame({'Column Name': column_names, '% Nulls': null_percentages})
    result_df.to_csv(output_csv, index=False)