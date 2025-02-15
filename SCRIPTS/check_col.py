import pandas as pd

# Load the dataset
file_path = "/Users/vishwarajsaxena/Desktop/Project1/DATA/your_dataset.csv"  # Change if needed
df = pd.read_csv(file_path)

# Display column names
print("Columns in dataset:", df.columns)
