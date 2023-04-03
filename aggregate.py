# import pandas library
import pandas as pd

# read in the data
df = pd.read_csv('example_data.csv')

# group the data by country and calculate the total market size and revenue
grouped_data = df.groupby('Country').agg({'Market Size (in billions)': 'sum', 'BP revenue ( in billions)': 'sum'})

# reset the index to make the 'Country' column a regular column
grouped_data = grouped_data.reset_index()

# print the aggregated data
print(grouped_data)
