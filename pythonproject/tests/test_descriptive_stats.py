import sys
import os
import polars 

# Add the relative path to the "src" folder so that we can import descriptive_stats.py
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'src'))

# Import the functions from descriptive_stats.py
from descriptive_stats import execute_all_functions

def test_execute_all_functions():
    # Execute all functions
    results = execute_all_functions()

    #Add your assert statements here
    # For example:
    assert isinstance(results, polars.dataframe.frame.DataFrame), "Error: Incorrect data type returned"

if __name__ == '__main__':
    test_execute_all_functions()
