import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.cluster import KMeans, AgglomerativeClustering
from sklearn.preprocessing import StandardScaler
import os


rfm_path = "/Users/vishwarajsaxena/Desktop/Project1/DATA/rfm_scores.csv"
output_path = "/Users/vishwarajsaxena/Desktop/Project1/DATA/clustered_rfm.csv"
plot_path = "/Users/vishwarajsaxena/Desktop/Project1/DATA/customer_clusters.png"


df = pd.read_csv(rfm_path)


rfm_features = df[['Recency', 'Frequency', 'Monetary']]


scaler = StandardScaler()
rfm_scaled = scaler.fit_transform(rfm_features)


kmeans = KMeans(n_clusters=4, random_state=42, n_init=10)
df['KMeans_Cluster'] = kmeans.fit_predict(rfm_scaled)


agglo = AgglomerativeClustering(n_clusters=4)
df['Hierarchical_Cluster'] = agglo.fit_predict(rfm_scaled)


df.to_csv(output_path, index=False)


plt.figure(figsize=(10, 6))
sns.scatterplot(x=df['Recency'], y=df['Frequency'], hue=df['KMeans_Cluster'], palette="viridis", s=100, alpha=0.8)
plt.xlabel("Recency")
plt.ylabel("Frequency")
plt.title("Customer Clusters (K-Means)")
plt.legend(title="Cluster")
plt.grid(True, linestyle="--", alpha=0.7)
plt.savefig(plot_path)
plt.show()

print("Customer segmentation completed! Clustered data saved and visualization generated.")
