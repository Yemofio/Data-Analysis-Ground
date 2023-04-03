import pandas as pd

# Load the data into a pandas DataFrame
df = pd.read_csv('data.csv')

# Remove duplicate rows
df.drop_duplicates(inplace=True)

# Remove rows with missing values
df.dropna(inplace=True)

# Remove leading/trailing whitespaces from string columns
df['column_name'] = df['column_name'].str.strip()

# Convert string columns to lowercase
df['column_name'] = df['column_name'].str.lower()

# Remove special characters from string columns
df['column_name'] = df['column_name'].str.replace('[^a-zA-Z0-9\s]+', '')

# Convert column data types
df['column_name'] = pd.to_numeric(df['column_name'], errors='coerce')
df['date_column'] = pd.to_datetime(df['date_column'])

# Fill missing values with the mean or median
df['column_name'].fillna(df['column_name'].mean(), inplace=True)
df['column_name'].fillna(df['column_name'].median(), inplace=True)

# Create new columns based on existing columns
df['new_column'] = df['column_name'] * 2

# Drop unnecessary columns
df.drop(columns=['column_name'], inplace=True)

# Rename columns
df.rename(columns={'old_name': 'new_name'}, inplace=True)

# Save the cleaned data to a new CSV file
df.to_csv('cleaned_data.csv', index=False)
