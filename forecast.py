import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

# Read sales data from Excel file into a pandas DataFrame
df = pd.read_excel('sales_data.xlsx', parse_dates=['Date'], index_col='Date')

# Create a new DataFrame with monthly sales totals
monthly_sales = df.resample('M')['Sales'].sum().reset_index()

# Split the data into training and testing sets
train_data = monthly_sales.loc[monthly_sales['Date'] < '2023-01-01']
test_data = monthly_sales.loc[monthly_sales['Date'] >= '2023-01-01']

# Create a linear regression model
model = LinearRegression()

# Fit the model to the training data
model.fit(train_data.index.values.reshape(-1,1), train_data['Sales'])

# Make predictions on the test data
predictions = model.predict(test_data.index.values.reshape(-1,1))

# Plot the actual and predicted sales
plt.plot(monthly_sales['Date'], monthly_sales['Sales'], label='Actual')
plt.plot(test_data['Date'], predictions, label='Predicted')
plt.title('Monthly Sales Forecast', fontsize=18)
plt.xlabel('Date', fontsize=14)
plt.ylabel('Sales (USD)', fontsize=14)
plt.legend(fontsize=12)
plt.show()
