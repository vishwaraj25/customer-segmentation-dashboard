import pandas as pd

# Load the clustered RFM file
rfm_data = pd.read_csv("/Users/vishwarajsaxena/Desktop/Project1/DATA/clustered_rfm.csv")

# Print column names to verify
print("Columns in RFM Data:", rfm_data.columns)

# Choose the correct cluster column (modify this based on your clustering method)
cluster_column = "KMeans_Cluster"  # Change to "Hierarchical_Cluster" if needed

# Group by the selected cluster column
cluster_summary = rfm_data.groupby(cluster_column).agg({
    'Recency': ['mean', 'median'],
    'Frequency': ['mean', 'median'],
    'Monetary': ['mean', 'median']
}).reset_index()

# Display the summary
print(cluster_summary)
