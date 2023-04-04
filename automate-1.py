import pandas as pd
import matplotlib.pyplot as plt

# Read Excel data into a pandas DataFrame
df = pd.read_excel('sales_data.xlsx')

# Create bar chart of sales by category
sales_by_category = df.groupby('Category')['Sales'].sum()
sales_by_category.plot(kind='bar', color='blue', alpha=0.7)
plt.title('Sales by Category')
plt.xlabel('Category')
plt.ylabel('Sales')
plt.show()

# Create line chart of sales over time
df['Date'] = pd.to_datetime(df['Date'])
time_sales = df.groupby('Date')['Sales'].sum()
time_sales.plot(color='green', alpha=0.7)
plt.title('Sales over Time')
plt.xlabel('Date')
plt.ylabel('Sales')
plt.show()
