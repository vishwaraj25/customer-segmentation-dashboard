import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from fpdf import FPDF

# Define file paths
graphs = {
    "avg_order_value_distribution": "/mnt/data/avg_order_value_distribution_fixed.png",
    "avg_order_value_boxplot": "/mnt/data/avg_order_value_boxplot.png",
    "cluster_comparison_kmeans_and_hierarchical": "/mnt/data/cluster_comparison_kmeans_and_hierarchical.png",
    "cluster_comparison_scatter": "/mnt/data/cluster_comparison_scatter.png",
    "cluster_profile": "/mnt/data/clut_prof.png",
    "customer_cluster_rfm": "/mnt/data/customer_cluster_rfm.png",
    "distribution_log_price": "/mnt/data/Distribution_of_log_transformed_price.png",
    "heat_map": "/mnt/data/heat_map.png",
    "purchase_frequency_distribution": "/mnt/data/purchase_frequency_distribution_fixed.png",
    "top_10_customers": "/mnt/data/top_10_customers.png"
}

# Define insights
graph_insights = {
    "avg_order_value_distribution": "Looking at the graph, the average order value is right-skewed, suggesting a few high-value purchases. A log transformation may help normalize the distribution.",
    "avg_order_value_boxplot": "The boxplot highlights several outliers in order values, indicating potential high-value customers or data anomalies.",
    "cluster_comparison_kmeans_and_hierarchical": "Both clustering techniques show similar segmentations, but K-Means provides a more distinct separation between clusters.",
    "cluster_comparison_scatter": "From the scatter plot, we see that customer segments are well-separated based on the selected features, validating the clustering approach.",
    "cluster_profile": "Each customer cluster shows distinct behaviors, with some groups making frequent purchases while others focus on high-value transactions.",
    "customer_cluster_rfm": "RFM analysis reveals that some clusters have frequent buyers, whereas others contain less frequent but high-value customers.",
    "distribution_log_price": "Applying a log transformation normalizes the price distribution, making it easier to detect patterns and anomalies.",
    "heat_map": "The heatmap illustrates strong correlations between Recency, Frequency, and Monetary values, reinforcing the RFM model's reliability.",
    "purchase_frequency_distribution": "The purchase frequency distribution shows that most customers make few purchases, with only a small fraction being high-frequency buyers.",
    "top_10_customers": "The top 10 customers contribute significantly to revenue, suggesting that a loyalty program for them could drive more engagement."
}

# Generate PDF report
pdf = FPDF()
pdf.set_auto_page_break(auto=True, margin=15)

pdf.add_page()
pdf.set_font("Arial", style='B', size=16)
pdf.cell(200, 10, "Customer Segmentation Report", ln=True, align='C')
pdf.ln(10)

pdf.set_font("Arial", size=12)
pdf.multi_cell(0, 10, "This report presents an analysis of customer segmentation using clustering techniques and RFM analysis. The insights provide a data-driven understanding of customer behaviors.")
pdf.ln(5)

for title, path in graphs.items():
    pdf.add_page()
    pdf.set_font("Arial", style='B', size=14)
    pdf.cell(200, 10, title.replace("_", " ").title(), ln=True, align='C')
    pdf.ln(5)
    pdf.image(path, x=15, w=180)
    pdf.ln(5)
    
    pdf.set_font("Arial", size=12)
    pdf.multi_cell(0, 10, graph_insights[title])
    pdf.ln(5)

pdf.output("/mnt/data/customer_segmentation_report.pdf")
