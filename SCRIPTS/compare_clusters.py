import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load clustered RFM data
file_path = '/Users/vishwarajsaxena/Desktop/Project1/DATA/clustered_rfm.csv'
df = pd.read_csv(file_path)

# Define clusters
cluster_columns = ['KMeans_Cluster', 'Hierarchical_Cluster']
rfm_metrics = ['Recency', 'Frequency', 'Monetary']

# Set Seaborn style
sns.set(style="whitegrid")

# Create subplots
fig, axes = plt.subplots(2, 3, figsize=(15, 10))
fig.suptitle("Cluster Comparison: K-Means vs Hierarchical", fontsize=16, fontweight="bold")

for i, cluster_col in enumerate(cluster_columns):
    for j, metric in enumerate(rfm_metrics):
        ax = axes[i, j]
        cluster_means = df.groupby(cluster_col).mean()[metric]

        # Create bar plot
        sns.barplot(x=cluster_means.index, y=cluster_means.values, ax=ax, palette="viridis")

        # Add data labels
        for p in ax.patches:
            ax.annotate(f"{p.get_height():,.0f}", 
                        (p.get_x() + p.get_width() / 2, p.get_height()), 
                        ha='center', va='bottom', fontsize=10, fontweight='bold')

        # Set title and labels
        ax.set_title(f"{metric} by {cluster_col}", fontsize=12, fontweight="bold")
        ax.set_xlabel(cluster_col)
        ax.set_ylabel(metric)
        ax.grid(True, linestyle="--", alpha=0.7)

# Adjust layout and save figure
plt.tight_layout(rect=[0, 0, 1, 0.95])
output_path = "/Users/vishwarajsaxena/Desktop/Project1/DATA/cluster_comparison_updated.png"
plt.savefig(output_path, dpi=300)
plt.show()

print(f"Updated visualization saved at: {output_path}")
