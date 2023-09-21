# Continous Integration with Github Actions: Using Data Handling with Polars

[![Format](https://github.com/midspooj/pb226-de-individual-project-1/actions/workflows/format.yml/badge.svg)](https://github.com/midspooj/pb226-de-individual-project-1/actions/workflows/format.yml)
[![Lint](https://github.com/midspooj/pb226-de-individual-project-1/actions/workflows/lint.yml/badge.svg)](https://github.com/midspooj/pb226-de-individual-project-1/actions/workflows/lint.yml)
[![OnInstall](https://github.com/midspooj/pb226-de-individual-project-1/actions/workflows/install.yml/badge.svg)](https://github.com/midspooj/pb226-de-individual-project-1/actions/workflows/install.yml)
[![Test](https://github.com/midspooj/pb226-de-individual-project-1/actions/workflows/test.yml/badge.svg)](https://github.com/midspooj/pb226-de-individual-project-1/actions/workflows/test.yml)

## Youtube Video Walkthrough - Link: https://youtu.be/IZeC7uZjEQY

## Introduction
Continous Integration with Github Actions performs two important functions:
1. Early Detection of Issues:
CI helps catch bugs, style violations, and integration problems early in the development process, reducing the chances of merging faulty code.

2. Faster Development Cycle:
Developers can merge their changes more frequently, leading to quicker feedback loops and faster delivery of features or bug fixes.

GitHub workflows are essential for automating various tasks in software development.  
In this project, the importance of Continous Integration (CI) with Github Actions is explored:
## Format:

This step ensures that the codebase adheres to a consistent style guide, making it easier to read and maintain.

## Lint:

Linting checks the code for potential errors, bugs, or style violations, helping maintain code quality and consistency.

## Install:

Installing dependencies ensures that the project has all the required libraries and packages to run successfully.

## Test:

Testing involves running automated tests to verify that the code functions correctly and meets the specified requirements.  

All four of these workflows pass for this project, as is seen from the badges on the top of this README file.

# Shared Common Script - Lib.py
The script lib.py contains contains three different functionalities, broken down into functions:
1. load_csv_data: Loads the data from a csv file for processing
2. visualize_scatter_plot: Visualizes a scatter pot using the package matplotlib
3. calculate_summary statistics: Returns the summary statistics of the scatter plot generated

# Python script - descriptive_stats.py

This is a simple python script that imports lib, and uses the functions inside it. 

# Jupyter Notebook - des_stats_notebook.ipynb

A Jupyter Notebook that helps in easy visualization of the code, followed by the scatter plot and the summary statistics table for different parameters.

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
Continuous Integration (CI) with GitHub Actions is crucial for streamlining the development process. It automates tasks like testing, formatting, and dependency management, ensuring that code changes integrate seamlessly and without errors. This leads to faster, more reliable development cycles, enabling teams to deliver high-quality software with confidence and efficiency.











