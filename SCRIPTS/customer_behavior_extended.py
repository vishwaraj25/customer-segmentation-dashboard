import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import os

# File path
file_path = "/Users/vishwarajsaxena/Desktop/Project1/DATA/cleaned_customer_segmentation.xlsx"

# Load the dataset
df = pd.read_excel(file_path)

# Ensure 'TotalPrice' column exists
if "TotalPrice" not in df.columns or "CustomerID" not in df.columns:
    raise ValueError("Required columns missing from dataset.")

# Aggregate total spending per customer
customer_spending = df.groupby("CustomerID")["TotalPrice"].sum().sort_values(ascending=False)

# Top 10 customers by total spending
plt.figure(figsize=(10, 6))
sns.barplot(x=customer_spending.head(10).index.astype(str), y=customer_spending.head(10).values, palette="viridis")
plt.xlabel("Customer ID")
plt.ylabel("Total Spending")
plt.title("Top 10 Customers by Total Spending")
plt.xticks(rotation=45)
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.tight_layout()
plt.savefig("/Users/vishwarajsaxena/Desktop/Project1/DATA/top_10_customers.png")
plt.show()

# Calculate average order value per customer
customer_avg_order = df.groupby("CustomerID")["TotalPrice"].mean()

# Remove extreme outliers (99th percentile)
upper_limit = np.percentile(customer_avg_order, 99)
filtered_avg_order = customer_avg_order[customer_avg_order <= upper_limit]

# Histogram with log scale
plt.figure(figsize=(10, 6))
sns.histplot(filtered_avg_order, bins=50, kde=True, color="blue")
plt.xlabel("Average Order Value (Capped at 99th percentile)")
plt.ylabel("Frequency")
plt.title("Distribution of Average Order Value per Customer (Outliers Removed)")
plt.xscale("log")
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.tight_layout()
plt.savefig("/Users/vishwarajsaxena/Desktop/Project1/DATA/avg_order_value_distribution_fixed.png")
plt.show()

# Box plot for outlier detection
plt.figure(figsize=(8, 4))
sns.boxplot(x=filtered_avg_order, color="blue")
plt.xlabel("Average Order Value")
plt.title("Box Plot of Average Order Value per Customer (Outliers Removed)")
plt.grid(axis='x', linestyle='--', alpha=0.7)
plt.tight_layout()
plt.savefig("/Users/vishwarajsaxena/Desktop/Project1/DATA/avg_order_value_boxplot.png")
plt.show()

# Calculate purchase frequency per customer
purchase_frequency = df["CustomerID"].value_counts()

# Remove extreme outliers (99th percentile)
upper_limit_freq = np.percentile(purchase_frequency, 99)
filtered_freq = purchase_frequency[purchase_frequency <= upper_limit_freq]

# Histogram with better binning
plt.figure(figsize=(10, 6))
sns.histplot(filtered_freq, bins=50, kde=True, color="green")
plt.xlabel("Purchase Frequency (Capped at 99th percentile)")
plt.ylabel("Number of Customers")
plt.title("Distribution of Purchase Frequency (Outliers Removed)")
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.tight_layout()
plt.savefig("/Users/vishwarajsaxena/Desktop/Project1/DATA/purchase_frequency_distribution_fixed.png")
plt.show()

print("Customer behavior analysis completed and graphs saved in the DATA folder.")
