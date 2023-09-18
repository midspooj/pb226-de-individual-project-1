import polars as pl
import matplotlib.pyplot as plt

def generate_scatter_plot(csv_path):
    # Assuming you have a CSV file with the COVID-19 data.
    df = pl.read_csv(csv_path) 
    
    plt.figure(figsize=(10, 6))

    # Scatter plot for Deaths vs Confirmed
    plt.scatter(df["Confirmed"], df["Deaths"], color='blue', label='Deaths')
    
    # Scatter plot for Recovered vs Confirmed
    plt.scatter(df["Confirmed"], df["Recovered"], color='green', label='Recovered')
    
    # Scatter plot for Active vs Confirmed
    plt.scatter(df["Confirmed"], df["Active"], color='red', label='Active')

    plt.title("Scatter Plot for COVID-19 Cases")
    plt.xlabel("Confirmed")
    plt.ylabel("Counts")
    plt.legend()
    plt.tight_layout()
    plt.show()
    
    #get the summary stats for the four columns
    
    # df = pl.read_csv(csv_path)
    
    # Selecting relevant columns
    df = df.select(["Confirmed", "Deaths", "Recovered", "Active"])
    
    # Calculate summary statistics
    summary_stats = df.describe()
    # print(summary_stats)
    # print("sd")

    return plt, summary_stats

# Call the function with the actual path to your CSV file
og_csv_path = r'https://raw.githubusercontent.com/midspooj/pb226-de-miniproject-3/main/country_wise_latest.csv'
# generate_scatter_plot(csv_path)
plot, og_summary_stats = generate_scatter_plot(og_csv_path)

