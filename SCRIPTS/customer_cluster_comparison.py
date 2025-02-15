import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the clustered RFM dataset
file_path = "/Users/vishwarajsaxena/Desktop/Project1/DATA/clustered_rfm.csv"
rfm_data = pd.read_csv(file_path)

# Create subplots for comparison
fig, axes = plt.subplots(1, 2, figsize=(14, 6))

# Scatter plot for K-Means Clustering
sns.scatterplot(data=rfm_data, x='Recency', y='Frequency', hue='KMeans_Cluster', palette='viridis', ax=axes[0])
axes[0].set_title('K-Means Clustering')

# Scatter plot for Hierarchical Clustering
sns.scatterplot(data=rfm_data, x='Recency', y='Frequency', hue='Hierarchical_Cluster', palette='coolwarm', ax=axes[1])
axes[1].set_title('Hierarchical Clustering')

# Save the comparison plot
output_path = "/Users/vishwarajsaxena/Desktop/Project1/DATA/cluster_comparison_scatter.png"
plt.savefig(output_path)
plt.show()
