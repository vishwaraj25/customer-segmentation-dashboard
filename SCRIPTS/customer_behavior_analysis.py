import pandas as pd

# Load cleaned dataset
file_path = "/Users/vishwarajsaxena/Desktop/Project1/DATA/cleaned_customer_segmentation.xlsx"
df = pd.read_excel(file_path, engine="openpyxl")

# Convert 'InvoiceDate' to datetime
df["InvoiceDate"] = pd.to_datetime(df["InvoiceDate"], errors="coerce")

# Remove null values in critical columns
df = df.dropna(subset=["CustomerID", "InvoiceDate", "TotalPrice"])

# Set analysis date (assume latest date in dataset)
analysis_date = df["InvoiceDate"].max()

# Calculate RFM metrics
rfm = df.groupby("CustomerID").agg({
    "InvoiceDate": lambda x: (analysis_date - x.max()).days,  # Recency
    "InvoiceNo": "count",  # Frequency
    "TotalPrice": "sum"  # Monetary Value
})

# Rename columns
rfm.columns = ["Recency", "Frequency", "Monetary"]

# Assign RFM scores (1-5) using quantiles
rfm["R_Score"] = pd.qcut(rfm["Recency"], 5, labels=[5, 4, 3, 2, 1])
rfm["F_Score"] = pd.qcut(rfm["Frequency"], 5, labels=[1, 2, 3, 4, 5])
rfm["M_Score"] = pd.qcut(rfm["Monetary"], 5, labels=[1, 2, 3, 4, 5])

# Combine into RFM Score
rfm["RFM_Score"] = rfm["R_Score"].astype(str) + rfm["F_Score"].astype(str) + rfm["M_Score"].astype(str)

# Save RFM table
rfm.to_csv("/Users/vishwarajsaxena/Desktop/Project1/DATA/rfm_scores.csv")

print("\n RFM Analysis Complete! Results saved as 'rfm_scores.csv'")
