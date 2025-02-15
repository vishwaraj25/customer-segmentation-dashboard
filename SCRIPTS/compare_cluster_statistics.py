import pandas as pd

# Load the clustered RFM data
file_path = '/Users/vishwarajsaxena/Desktop/Project1/DATA/clustered_rfm.csv'
df = pd.read_csv(file_path)

# Ensure the correct column name is used
cluster_columns = ['KMeans_Cluster', 'Hierarchical_Cluster']

for cluster_col in cluster_columns:
    if cluster_col in df.columns:
        cluster_means = df.groupby(cluster_col).mean()
        print(f"\nCluster Means for {cluster_col}:\n", cluster_means)
    else:
        print(f"Column '{cluster_col}' not found in dataset.")
