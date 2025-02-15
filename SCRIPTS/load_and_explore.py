import pandas as pd

# Define the absolute path to the dataset
file_path = "/Users/vishwarajsaxena/Desktop/Project1/DATA/customer_segmentation.xlsx"

# Load the dataset
df = pd.read_excel(file_path, engine="openpyxl")

# Display basic information about the dataset
print("Dataset Overview:")
print(df.info())
print("\nFirst 5 Rows:")
print(df.head())

# Check for missing values
print("\nMissing Values:")
print(df.isnull().sum())

# Summary statistics
print("\nSummary Statistics:")
print(df.describe())
