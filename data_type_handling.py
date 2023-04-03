import pandas as pd

# Load the data
df = pd.read_csv('sales_data.csv')

# Check for missing values
print(df.isnull().sum())

# Fill missing values with the mean of the column
df.fillna(df.mean(), inplace=True)

# Drop duplicate rows
df.drop_duplicates(inplace=True)

# Convert data types
df['Market Size (in billions)'] = pd.to_numeric(df['Market Size (in billions)'])
df['Growth'] = pd.to_numeric(df['Growth'].str.rstrip('%'))
df['Volume (in billions)'] = pd.to_numeric(df['Volume (in billions)'])
df['BP revenue ( in billions)'] = pd.to_numeric(df['BP revenue ( in billions)'])
df['Internet users'] = pd.to_numeric(df['Internet users'].str.rstrip('%'))
df['Online shopper mean age'] = pd.to_numeric(df['Online shopper mean age'])
df['Net online spend'] = pd.to_numeric(df['Net online spend'])
df['Average spend per purchase'] = pd.to_numeric(df['Average spend per purchase'])
df['Maximum Gross Purchases (MGP)'] = pd.to_numeric(df['Maximum Gross Purchases (MGP)'])
df['MGP for Electronics'] = pd.to_numeric(df['MGP for Electronics'])
df['Average Accepted Price'] = pd.to_numeric(df['Average Accepted Price'])
df['Highest Accepted Price'] = pd.to_numeric(df['Highest Accepted Price'])

# Convert growth to decimal format
df['Growth'] = df['Growth'] / 100

# Check data types
print(df.dtypes)
