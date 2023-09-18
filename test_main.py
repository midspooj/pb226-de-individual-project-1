from main import generate_scatter_plot
import polars as pl

def test_generate_scatter_plot():
    # Define the CSV path for testing
    test_csv_path = "https://raw.githubusercontent.com/midspooj/pb226-de-miniproject-3/main/country_wise_latest.csv"

    # Call the function and capture the returned values
    plot, summary_stats = generate_scatter_plot(test_csv_path)

    # Check if plot is not None
    assert plot is not None, "plot should not be None"

    # Check if summary_stats is a DataFrame
    assert isinstance(summary_stats, pl.DataFrame), "summary_stats should be a polars DataFrame"

    # Check if summary_stats has the expected number of columns
    expected_num_columns = 5  # Assuming there are 4 columns in the summary
    assert len(summary_stats.columns) == expected_num_columns, f"summary_stats should have {expected_num_columns} columns"

    # Check if summary_stats has at least one row
    assert len(summary_stats) >= 1, "summary_stats should have at least one row"

# Run the testing function
test_generate_scatter_plot()
    
    

