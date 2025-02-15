import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# File path to cleaned dataset
file_path = '/Users/vishwarajsaxena/Desktop/Project1/DATA/cleaned_customer_segmentation.xlsx'

# Load data
df = pd.read_excel(file_path, parse_dates=['InvoiceDate'])

# Remove extreme outliers (99th percentile)
upper_limit = df['TotalPrice'].quantile(0.99)
df_filtered = df[df['TotalPrice'] <= upper_limit]

# Apply log transformation to reduce skewness
df_filtered['LogTotalPrice'] = np.log1p(df_filtered['TotalPrice'])

# Plot the updated histogram
plt.figure(figsize=(8, 5))
sns.histplot(df_filtered['LogTotalPrice'], bins=50, kde=True)
plt.title("Distribution of Log-Transformed Total Price")
plt.xlabel("Log(Total Price)")
plt.ylabel("Frequency")
plt.show()

print("EDA completed successfully.")
