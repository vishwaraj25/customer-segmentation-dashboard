import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the clustered RFM dataset
file_path = "/Users/vishwarajsaxena/Desktop/Project1/DATA/clustered_rfm.csv"
df = pd.read_csv(file_path)

# Define the cluster columns for comparison
cluster_columns = ["KMeans_Cluster", "Hierarchical_Cluster"]
rfm_metrics = ["Recency", "Frequency", "Monetary"]

# Set plot style
sns.set(style="whitegrid")

# Create bar plots for cluster statistics
for cluster_col in cluster_columns:
    fig, axes = plt.subplots(1, 3, figsize=(18, 5))

    for i, metric in enumerate(rfm_metrics):
        sns.barplot(x=df[cluster_col], y=df[metric], ax=axes[i], palette="viridis")
        axes[i].set_title(f"{metric} by {cluster_col}")
        axes[i].set_xlabel(cluster_col)
        axes[i].set_ylabel(metric)

    plt.tight_layout()
    plt.savefig(f"/Users/vishwarajsaxena/Desktop/Project1/OUTPUT/{cluster_col}_barplot.png")
    plt.show()

# Create box plots for distribution analysis
for cluster_col in cluster_columns:
    fig, axes = plt.subplots(1, 3, figsize=(18, 5))

    for i, metric in enumerate(rfm_metrics):
        sns.boxplot(x=df[cluster_col], y=df[metric], ax=axes[i], palette="coolwarm")
        axes[i].set_title(f"Distribution of {metric} by {cluster_col}")
        axes[i].set_xlabel(cluster_col)
        axes[i].set_ylabel(metric)

    plt.tight_layout()
    plt.savefig(f"/Users/vishwarajsaxena/Desktop/Project1/OUTPUT/{cluster_col}_boxplot.png")
    plt.show()
