import pandas as pd

# Load the dataset
file_path = '/Users/vishwarajsaxena/Desktop/Project1/DATA/customer_segmentation.xlsx'
df = pd.read_excel(file_path, engine='openpyxl')

# Drop rows where CustomerID is missing
df = df.dropna(subset=['CustomerID'])

# Remove duplicates
df = df.drop_duplicates()

# Remove rows with negative or zero Quantity and UnitPrice
df = df[(df['Quantity'] > 0) & (df['UnitPrice'] > 0)]

# Create a new feature: TotalPrice
df['TotalPrice'] = df['Quantity'] * df['UnitPrice']

# Convert InvoiceDate to datetime and extract Year-Month
df['InvoiceDate'] = pd.to_datetime(df['InvoiceDate'])
df['YearMonth'] = df['InvoiceDate'].dt.to_period('M')

# Save the cleaned dataset
cleaned_file_path = '/Users/vishwarajsaxena/Desktop/Project1/DATA/cleaned_customer_segmentation.xlsx'
df.to_excel(cleaned_file_path, index=False)

print("Data cleaning completed. Cleaned file saved at:", cleaned_file_path)
