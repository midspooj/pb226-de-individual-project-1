# Data Handling With Polars - A COVID-19 Example

## Introduction

In mini-project 3, my primary focus was on testing and leveraging two core features of Polars:

1. **Performance Optimization**  
   Polars is meticulously engineered for high-performance data manipulation, showcasing remarkable efficiency in handling extensive datasets. It's robust capabilities surpass those of traditional libraries like Pandas, making it an excellent choice for large-scale data processing.

2. **Lazy Evaluation Strategy**  
   Polars adopts a lazy evaluation approach, deferring the execution of operations until their results are explicitly required. This methodology contributes to more efficient memory utilization, especially beneficial in scenarios involving complex data processing pipelines.

## Dataset Selection
To rigorously test these features, I opted for a substantially large dataset sourced from Kaggle, which served as a benchmark for evaluating the prowess of Polars in comparison to other data manipulation libraries.

# Dataset Overview

This dataset provides detailed information on the COVID-19 pandemic, including metrics such as deaths, recoveries, active cases, and more, categorized by WHO regions. Sourced from Kaggle and focusing on the year 2022, it serves as a foundation for comprehensive global COVID-19 analysis. The aim is to uncover trends and patterns in the relationships between deaths, recoveries, and active cases worldwide.

# Purpose of the Code

This code conducts a data analysis on COVID-19 statistics obtained from a supplied CSV file. It creates a scatter plot to visually represent the correlations between confirmed cases, deaths, recoveries, and active cases. Furthermore, it calculates summary statistics for these essential metrics using Polars.

## Data Reading and Scatter Plotting

The function `generate_scatter_plot` takes a CSV file path as input.

- It reads the data from the CSV using Polars and generates a scatter plot using Matplotlib.
- Three scatter plots are created:
  - Deaths vs Confirmed (in blue)
  - Recovered vs Confirmed (in green)
  - Active vs Confirmed (in red).
- The plot is displayed with appropriate labels and legend.

## Data Processing and Summary Statistics

- The relevant columns (Confirmed, Deaths, Recovered, Active) are selected using Polars.
- Summary statistics are calculated for these selected columns using `df.describe()`.

## Displaying the Summary Stats

- The summary statistics are returned as a DataFrame. 

#   Results 
The summary statistics generated are as follows:
| describe   | Confirmed     | Deaths       | Recovered     | Active        |
| ---        | ---           | ---          | ---           | ---           |
| str        | f64           | f64          | f64           | f64           |
|------------|---------------|--------------|---------------|---------------|
| count      | 187.0         | 187.0        | 187.0         | 187.0         |
| null_count | 0.0           | 0.0          | 0.0           | 0.0           |
| mean       | 88130.935829  | 3497.518717  | 50631.481283  | 34001.935829  |
| std        | 383318.663831 | 14100.002482 | 190188.189643 | 213326.173371 |
| min        | 10.0          | 0.0          | 0.0           | 0.0           |
| 25%        | 1100.0        | 18.0         | 607.0         | 140.0         |
| 50%        | 5059.0        | 108.0        | 2815.0        | 1600.0        |
| 75%        | 41180.0       | 748.0        | 23242.0       | 9414.0        |
| max        | 4.290259e6    | 148011.0     | 1.846641e6    | 2.816444e6    |  

This is the generated scatterplot for this dataset:  

![image](https://github.com/midspooj/pb226-de-miniproject-3/assets/142264378/14e74138-1a07-4c4c-b7f3-44dbd50ccdc2)  

# Key Takeaways

This assignment provided valuable insights into the significance of Polars, particularly its efficiency in handling large datasets. It served as a practical demonstration of how to choose the appropriate library for specific dataset sizes and complexities, highlighting the importance of selecting the right tool for efficient data manipulation and analysis.











