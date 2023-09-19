#python script to call all the functions inside lib.py

import lib

def execute_all_functions():

    # Load CSV Data
    og_csv_path = r'https://raw.githubusercontent.com/midspooj/pb226-de-miniproject-3/main/country_wise_latest.csv'
    df = lib.load_csv_data(og_csv_path)

    # Visualize Scatter Plot
    lib.visualize_scatter_plot(df)

    # Calculate Summary Statistics
    summary_stats = lib.calculate_summary_statistics(df)
    return summary_stats

if __name__ == "__main__":
    results = execute_all_functions()
    print(results)
