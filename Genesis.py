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

# Fill missing values with 0
df.fillna(0, inplace=True)

# Drop rows with missing values
df.dropna(inplace=True)

# Convert market size to millions
df['Market Size (in millions)'] = df['Market Size (in billions)'].apply(lambda x: x * 1000)

# Group by top product and find mean and max revenue
grouped = df.groupby('Top product (electronics)').agg({'BP revenue ( in billions)': ['mean', 'max']})

import matplotlib.pyplot as plt

# Create a bar chart of market size for each country
plt.bar(df['Country'], df['Market Size (in billions)'])
plt.xlabel('Country')
plt.ylabel('Market Size (in billions)')
plt.show()





