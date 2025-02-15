import pandas as pd

# Define file path
file_path = "/Users/vishwarajsaxena/Desktop/Project1/DATA/cleaned_customer_segmentation.xlsx"

# Load the dataset
df = pd.read_excel(file_path)

# Display dataset info
print("\n--- Data Overview ---")
print(df.info())

# Display first 5 rows
print("\n--- First 5 Rows ---")
print(df.head())

# Check for missing values
print("\n--- Missing Values ---")
print(df.isnull().sum())

# Check for duplicates
duplicate_count = df.duplicated().sum()
print(f"\n--- Duplicate Rows: {duplicate_count} ---")

# Check summary statistics
print("\n--- Summary Statistics ---")
print(df.describe())

print("\nData verification completed.")
