# IMDB Dataset Analysis
This project uses the IMDB dataset to perform data preprocessing, exploratory data analysis (EDA), and basic statistical analysis using Python.

## Dataset
The analysis uses the IMDB datasets:

``` title.basics.tsv
title.ratings.tsv
```
downloaded using KaggleHub

## Data Preprocessing
- Loaded the IMDB datasets into Pandas DataFrames.
- Merged movie metadata with ratings data.
- Filtered the dataset to include only movies.
- Removed rows with missing values in key columns.
- Converted columns to appropriate data types for analysis.

## Exploratory Data Analysis
- Examined dataset structure using df.info().
- Generated summary statistics using df.describe().
- Analyzed distributions and trends in movie ratings and release years.

## Basic Analysis and Visualizations
- Histogram of average movie ratings.
![histogram](image.png)
- Scatter plot of number of votes vs average rating.
![scatter plot](image-2.png)
- Line plot showing number of movies released per year.
![line plot](image-1.png)
- Identified top-rated movies with a minimum vote threshold.

## Tools Used
- Python
- Pandas
- Matplotlib
- Jupyter Notebook (VS Code)