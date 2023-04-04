import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Read Excel data into a pandas DataFrame
df = pd.read_excel('sales_data.xlsx')

# Calculate key metrics
total_sales = df['Sales'].sum()
average_sales = df['Sales'].mean()
max_sales = df['Sales'].max()
min_sales = df['Sales'].min()

# Create a bar chart of sales by product category
category_sales = df.groupby('Category')['Sales'].sum().sort_values()
fig, ax = plt.subplots(figsize=(8, 6))
ax.barh(category_sales.index, category_sales.values, color='green', alpha=0.7)
ax.set_title('Sales by Category')
ax.set_xlabel('Sales')
ax.set_ylabel('Category')

# Create a scatter plot of sales by profit
fig, ax = plt.subplots(figsize=(8, 6))
ax.scatter(df['Profit'], df['Sales'], color='red', alpha=0.7)
ax.set_title('Sales vs. Profit')
ax.set_xlabel('Profit')
ax.set_ylabel('Sales')

# Create a heatmap of sales by region and product category
region_category_sales = df.groupby(['Region', 'Category'])['Sales'].sum().unstack()
fig, ax = plt.subplots(figsize=(8, 6))
sns.heatmap(region_category_sales, annot=True, cmap='YlGnBu')
ax.set_title('Sales by Region and Category')
ax.set_xlabel('Category')
ax.set_ylabel('Region')

# Print key metrics
print('Total sales: ', total_sales)
print('Average sales: ', average_sales)
print('Max sales: ', max_sales)
print('Min sales: ', min_sales)

# Show the plots
plt.show()
