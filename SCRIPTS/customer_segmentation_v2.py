import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.cluster import KMeans

# Load the RFM dataset
file_path = "/Users/vishwarajsaxena/Desktop/Project1/DATA/rfm_scores.csv"
df = pd.read_csv(file_path)

# Selecting relevant features for clustering
rfm_features = df[['Recency', 'Frequency', 'Monetary']]

# Applying K-Means clustering
kmeans = KMeans(n_clusters=4, random_state=42)
df['Cluster'] = kmeans.fit_predict(rfm_features)

# Visualizing Clusters
plt.figure(figsize=(10,6))
sns.scatterplot(data=df, x='Recency', y='Frequency', hue='Cluster', palette='viridis', alpha=0.7)
plt.title("Customer Clusters (K-Means)")
plt.legend(title='Cluster')
plt.savefig("/Users/vishwarajsaxena/Desktop/Project1/DATA/customer_clusters_v2.png")
plt.show()

# Save the clustered dataset
df.to_csv("/Users/vishwarajsaxena/Desktop/Project1/DATA/rfm_clusters_v2.csv", index=False)
