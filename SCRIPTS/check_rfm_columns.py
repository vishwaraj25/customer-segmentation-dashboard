import pandas as pd

# Define file path
file_path = "/Users/vishwarajsaxena/Desktop/Project1/DATA/cleaned_customer_segmentation.xlsx"  # Update if needed

# Load the Excel file
df = pd.read_excel(file_path, engine="openpyxl")

# Print column names
print("Column Names in Dataset:\n", df.columns)

# Display first few rows
print("\nSample Data:\n", df.head())

# Rename 'InvoiceDate' → 'OrderDate' for consistency
if "InvoiceDate" in df.columns:
    df.rename(columns={"InvoiceDate": "OrderDate"}, inplace=True)

# Convert 'OrderDate' to datetime
df["OrderDate"] = pd.to_datetime(df["OrderDate"], errors="coerce")

# Check for missing values in key columns
required_columns = {"CustomerID", "OrderDate", "TotalPrice"}
missing_columns = required_columns - set(df.columns)

if missing_columns:
    print(f"\n⚠️ Missing columns after renaming: {missing_columns}")
else:
    print("\n✅ All required columns exist. Ready for RFM analysis!")

# Check for nulls
null_counts = df[required_columns].isnull().sum()
print("\nMissing values per column:\n", null_counts)
