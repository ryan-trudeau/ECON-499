import subprocess

def main():
    # Run extract_data.py
    print("Extracting data")
    subprocess.run(['python', 'extract_data.py'])

    print("Calculating summary stats")
    # Run load_summary_stats.py
    subprocess.run(['python', 'calculate_summary_stats.py'])
    
    print("Extracting field descriptions")
    # Run extract_field_descriptions.py
    subprocess.run(['python', 'extract_field_descriptions.py'])
if __name__ == "__main__":
    main()
