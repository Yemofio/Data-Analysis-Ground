# Create a new column for total revenue
df['Total Revenue'] = df['Market Size (in billions)'] * df['BP revenue ( in billions)']

# Convert the growth rate to a decimal
df['Growth'] = df['Growth'] / 100

# Create a new column for the total number of online shoppers
df['Total Online Shoppers'] = df['Internet users'] * df['Online shopper mean age'] * df['Online shopper mean age'] / 1000

# Create a new column for the total online spend
df['Total Online Spend'] = df['Net online spend'] * df['Total Online Shoppers']

# Create a new column for the average price per purchase
df['Average Price per Purchase'] = df['Total Online Spend'] / df['Total Online Shoppers']

# Create a new column for the maximum gross purchases for electronics
df['MGP for Electronics'] = df['Maximum Gross Purchases (MGP)'] * df['Volume (in billions)'] * df['Top product (electronics)']
