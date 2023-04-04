import pandas as pd
import matplotlib.pyplot as plt

# Read Excel data into a pandas DataFrame
df = pd.read_excel('data.xlsx')

# Create a bar chart of sales by region
region_sales = df.groupby('Region')['Sales'].sum()
fig, ax = plt.subplots(figsize=(8, 6))
ax.bar(region_sales.index, region_sales.values, color='blue', alpha=0.7)
ax.set_title('Sales by Region')
ax.set_xlabel('Region')
ax.set_ylabel('Sales')

# Create a horizontal bar chart of sales by category
category_sales = df.groupby('Category')['Sales'].sum().sort_values()
fig, ax = plt.subplots(figsize=(8, 6))
ax.barh(category_sales.index, category_sales.values, color='green', alpha=0.7)
ax.set_title('Sales by Category')
ax.set_xlabel('Sales')
ax.set_ylabel('Category')

# Create a stacked bar chart of sales by region and category
region_category_sales = df.groupby(['Region', 'Category'])['Sales'].sum().unstack()
fig, ax = plt.subplots(figsize=(8, 6))
region_category_sales.plot(kind='bar', stacked=True, ax=ax, alpha=0.7)
ax.set_title('Sales by Region and Category')
ax.set_xlabel('Region')
ax.set_ylabel('Sales')

# Show the plots
plt.show()
