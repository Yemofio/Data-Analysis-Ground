import pandas as pd

# Read data from CSV file
df = pd.read_csv('example_data.csv')

# Display first 5 rows of the data
print(df.head())

# Display summary statistics for numeric columns
print(df.describe())

# Group data by country and calculate mean net online spend
grouped_data = df.groupby('Country')['Net online spend'].mean()

# Display grouped data
print(grouped_data)
