import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the dataset
file_path = "/Users/vishwarajsaxena/Desktop/Project1/DATA/clustered_rfm.csv"
df = pd.read_csv(file_path)

# Set plot style
sns.set_style("whitegrid")

# Define the features to visualize
features = ['Recency', 'Frequency', 'Monetary']
cluster_column = 'Hierarchical_Cluster'

# Create subplots for visualization
fig, axes = plt.subplots(1, 3, figsize=(15, 5))

# Generate bar plots for each feature
for i, feature in enumerate(features):
    sns.barplot(
        x=cluster_column, y=feature, data=df, ax=axes[i], 
        hue=cluster_column, palette="viridis", errorbar="sd", legend=False
    )
    axes[i].set_title(f"{feature} by {cluster_column}")

# Adjust layout
plt.tight_layout()
plt.show()
