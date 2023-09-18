import sys
import os
import polars as pl
import pandas as pd

# Add the relative path to the "src" folder so that we can import lib.py
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'src'))

# Import the functions from lib.py
from lib import load_csv_data, visualize_scatter_plot, calculate_summary_statistics

class TestLib(unittest.TestCase):
    def setUp(self):
        self.csv_path = r'https://raw.githubusercontent.com/midspooj/pb226-de-miniproject-3/main/country_wise_latest.csv'
        self.df = load_csv_data(self.csv_path)

    def test_load_csv_data(self):
        self.assertIsInstance(self.df, pl.DataFrame, "load_csv_data should return a polars DataFrame")

    def test_calculate_summary_statistics(self):
        summary_stats = calculate_summary_statistics(self.df)
        self.assertIsInstance(summary_stats, pl.DataFrame, "calculate_summary_statistics should return a polars DataFrame")
        self.assertSetEqual(set(summary_stats.columns), {'summary', 'Confirmed', 'Deaths', 'Recovered', 'Active'}, "Incorrect columns in summary statistics")

    def test_visualize_scatter_plot(self):
        # This function doesn't return anything, so we'll use assertions based on matplotlib's figures.
        self.assertIsNone(visualize_scatter_plot(self.df), "visualize_scatter_plot should return None")

if __name__ == '__main__':
    unittest.main()
