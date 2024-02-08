# PitchBook Data Analysis

## Getting started

1. Clone the repository:
    ```bash
    git clone https://github.com/username/repository.git
    ```

2. Create a folder called `data/raw`  and place the unzipped raw data in the folder.

## Usage

1. Navigate to the `preprocessing` subfolder:
    ```bash
    cd preprocessing
    ```

2. Run the `main.py` file:
    ```bash
    python main.py
    ```


### What main.py does

The `main.py` script in Python orchestrates the execution of three separate Python scripts to perform a series of data processing and database operations. Each script is executed sequentially, and their functionalities are detailed below:

#### 1. `extract_data.py` 
This Python script automates the process of setting up a data processing environment, including directory creation, database management, and data transformation. 

- The script starts by finding the root directory of the repository.
- It writes this directory path into a `params.py` file for future reference.
- It defines a set of directories to be created within the repository, including directories for exports, database files, and summary statistics.
- These directories are created if they don't already exist, ensuring that the necessary file structure is in place for data processing.
- Establishes a connection with a SQLite database named `pitchbook.db` located in the `/data/database_files/` directory.
- This database is used for storing processed data from CSV files.
- The script iterates through CSV files located in the `/data/raw/` folder.
- For each CSV file, it performs the following operations:
    - Creates a table in the SQLite database from the CSV file.
    - Calculates the percentage of null values for each column in the CSV file and writes these statistics to a new CSV file in the `/data/summary_stats/` directory.

#### 3. `load_summary_stats.py`:
Processes and loads summary statistics from CSV files located in the `/summary_stats/` directory.
 - A new SQLite database (`null_counts.db`) is created.
 - Each CSV file is read, and a corresponding table is created in the SQLite database.


#### 2. `extract_field_descriptions.py`:
Extracts the descriptions of data fields from an Excel file named "Pitchbook Data Dictionary.xlsx".
- The script reads the Excel file, excluding the sheets 'TrackingChanges' and 'Summary'.
- Each sheet is processed to merge data with corresponding null percentage statistics from CSV files in the `/summary_stats/` directory.
- A new SQLite database (`schema_description.db`) is created, and tables are formed for each sheet with the merged data.
- This step enhances the initial data with meta-information and insights on data quality (null percentages).

