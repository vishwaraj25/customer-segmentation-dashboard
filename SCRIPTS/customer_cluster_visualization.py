import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


rfm_data = pd.read_csv('/Users/vishwarajsaxena/Desktop/Project1/DATA/clustered_rfm.csv')


cluster_summary = rfm_data.groupby('KMeans_Cluster').agg({
    'Recency': 'mean',
    'Frequency': 'mean',
    'Monetary': 'mean'
}).reset_index()


plt.figure(figsize=(10, 5))
cluster_summary.set_index('KMeans_Cluster').plot(kind='bar', figsize=(10, 6))
plt.title('Customer Clusters - Mean Recency, Frequency, Monetary')
plt.xlabel('Cluster')
plt.ylabel('Mean Value')
plt.xticks(rotation=0)
plt.legend(title='Metric')
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.savefig('/Users/vishwarajsaxena/Desktop/Project1/OUTPUT/cluster_comparison.png')
plt.show()


plt.figure(figsize=(8, 6))
sns.heatmap(cluster_summary.set_index('KMeans_Cluster').corr(), annot=True, cmap='coolwarm', fmt=".2f")
plt.title('Correlation Heatmap of RFM Metrics')
plt.savefig('/Users/vishwarajsaxena/Desktop/Project1/OUTPUT/cluster_correlation_heatmap.png')
plt.show()
