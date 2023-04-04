import pandas as pd
import matplotlib.pyplot as plt

# Read Excel data into a pandas DataFrame
df = pd.read_excel('sales_data.xlsx')

# Create bar chart of sales by category
sales_by_category = df.groupby('Category')['Sales'].sum()
ax = sales_by_category.plot(kind='bar', color='blue', alpha=0.7, figsize=(8,6))
ax.set_title('Sales by Category', fontsize=18)
ax.set_xlabel('Category', fontsize=14)
ax.set_ylabel('Sales (USD)', fontsize=14)
ax.tick_params(axis='x', labelsize=12)
ax.tick_params(axis='y', labelsize=12)
plt.tight_layout()
plt.show()

# Create line chart of sales over time
df['Date'] = pd.to_datetime(df['Date'])
time_sales = df.groupby('Date')['Sales'].sum()
ax = time_sales.plot(color='green', alpha=0.7, figsize=(8,6))
ax.set_title('Sales over Time', fontsize=18)
ax.set_xlabel('Date', fontsize=14)
ax.set_ylabel('Sales (USD)', fontsize=14)
ax.tick_params(axis='x', labelsize=12)
ax.tick_params(axis='y', labelsize=12)
plt.tight_layout()
plt.show()
