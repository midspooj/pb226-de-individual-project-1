import polars as pl
import matplotlib.pyplot as plt

def load_csv_data(csv_path):
    try:
        df = pl.read_csv(csv_path)
        return df
    except Exception as e:
        print(f"Error: {e}")



def visualize_scatter_plot(df):
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
    
def calculate_summary_statistics(df):
    try:
        df = df.select(["Confirmed", "Deaths", "Recovered", "Active"])
        summary_stats = df.describe()
        
        return summary_stats
    except Exception as e:
        print(f"Error: {e}")
        
# Load CSV Data
og_csv_path = r'https://raw.githubusercontent.com/midspooj/pb226-de-miniproject-3/main/country_wise_latest.csv'
df = load_csv_data(og_csv_path)

# Visualize Scatter Plot
visualize_scatter_plot(df)

# Calculate Summary Statistics
summary_stats = calculate_summary_statistics(df)
print(summary_stats)

