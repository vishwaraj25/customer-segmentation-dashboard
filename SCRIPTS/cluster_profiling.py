import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Load clustered RFM data
file_path = '/Users/vishwarajsaxena/Desktop/Project1/DATA/clustered_rfm.csv'
df = pd.read_csv(file_path)

# Define clusters to analyze
cluster_columns = ['KMeans_Cluster', 'Hierarchical_Cluster']

# Create summary for each clustering method
for cluster_col in cluster_columns:
    if cluster_col in df.columns:
        cluster_summary = df.groupby(cluster_col).agg({
            'Recency': ['mean', 'median'],
            'Frequency': ['mean', 'median'],
            'Monetary': ['mean', 'median'],
            'RFM_Score': ['mean']
        }).reset_index()
        
        # Save summary as CSV
        summary_path = f'/Users/vishwarajsaxena/Desktop/Project1/DATA/{cluster_col}_summary.csv'
        cluster_summary.to_csv(summary_path, index=False)
        print(f"Cluster Summary for {cluster_col} saved at {summary_path}\n")
        
        # Visualizing Cluster Distributions
        plt.figure(figsize=(10, 6))
        sns.boxplot(x=cluster_col, y='RFM_Score', data=df, palette='coolwarm')
        plt.title(f'RFM Score Distribution by {cluster_col}')
        plt.xlabel('Cluster')
        plt.ylabel('RFM Score')
        plt.show()
    else:
        print(f"Column '{cluster_col}' not found in data. ")