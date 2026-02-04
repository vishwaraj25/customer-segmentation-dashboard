import streamlit as st
import pandas as pd
import plotly.express as px
import os

# Set Streamlit page configuration
st.set_page_config(page_title="Customer Segmentation Dashboard", layout="wide")

# Get the absolute path to the current script
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_DIR = os.path.join(BASE_DIR, "../DATA")  # Adjust based on your folder structure
DATA_FILE = os.path.join(DATA_DIR, "clustered_rfm.csv")  # Adjust if needed

# Debugging: Check if the file exists in the deployment environment
if os.path.exists(DATA_FILE):
    st.success(f" File found at: {DATA_FILE}")
else:
    st.error(f"File NOT found at: {DATA_FILE}. Check your file paths and Git upload.")
    files_in_data = os.listdir(DATA_DIR) if os.path.exists(DATA_DIR) else []
    st.write("📂 Files in DATA folder:", files_in_data)

# Load Data
@st.cache_data
def load_data():
    return pd.read_csv(DATA_FILE)

df = load_data()

# Debugging - Ensure Data is Loaded
st.write("### 🔍 Data Preview:")
st.write(df.head())  # Check if data loads properly
st.write("### 📊 Column Names:", df.columns.tolist())  # Show column names

# Sidebar Navigation
st.sidebar.header("Navigation")
selected_graph = st.sidebar.radio("Select Visualization", [
    "Purchase Frequency Distribution", "Customer Clusters Based on RFM",
    "Cluster Comparison Scatter Plot", "Recency vs Frequency Analysis",
    "Monetary vs Frequency Analysis", "RFM Score Distribution",
    "Cluster Size Comparison", "Final Summary"
])

# Graphs
if selected_graph == "Purchase Frequency Distribution":
    st.header(" Purchase Frequency Distribution")
    fig = px.histogram(df, x="Frequency", nbins=50, title="Customer Purchase Frequency")
    st.plotly_chart(fig)
    st.write("Most customers purchase infrequently, suggesting a large portion of one-time buyers.")

elif selected_graph == "Customer Clusters Based on RFM":
    st.header(" Customer Clusters Based on RFM")
    if all(col in df.columns for col in ["Recency", "Monetary", "KMeans_Cluster"]):
        fig = px.scatter(df, x="Recency", y="Monetary", color="KMeans_Cluster", title="Customer Clusters")
        st.plotly_chart(fig)
    else:
        st.error("Required columns (Recency, Monetary, KMeans_Cluster) not found in dataset.")

elif selected_graph == "Cluster Comparison Scatter Plot":
    st.header("📊 Cluster Comparison Scatter Plot")
    if all(col in df.columns for col in ["Recency", "Frequency", "KMeans_Cluster"]):
        fig = px.scatter(df, x="Recency", y="Frequency", color="KMeans_Cluster", title="Cluster Comparison")
        st.plotly_chart(fig)
    else:
        st.error(" Required columns (Recency, Frequency, KMeans_Cluster) not found in dataset.")

elif selected_graph == "Recency vs Frequency Analysis":
    st.header("📊 Recency vs Frequency Analysis")
    if all(col in df.columns for col in ["Recency", "Frequency"]):
        fig = px.scatter(df, x="Recency", y="Frequency", title="Recency vs Frequency")
        st.plotly_chart(fig)
    else:
        st.error(" Required columns (Recency, Frequency) not found in dataset.")

elif selected_graph == "Monetary vs Frequency Analysis":
    st.header("📊 Monetary vs Frequency Analysis")
    if all(col in df.columns for col in ["Monetary", "Frequency"]):
        fig = px.scatter(df, x="Monetary", y="Frequency", title="Monetary vs Frequency")
        st.plotly_chart(fig)
    else:
        st.error(" Required columns (Monetary, Frequency) not found in dataset.")

elif selected_graph == "RFM Score Distribution":
    st.header("📊 RFM Score Distribution")
    if "RFM_Score" in df.columns:
        fig = px.histogram(df, x="RFM_Score", nbins=20, title="RFM Score Distribution")
        st.plotly_chart(fig)
    else:
        st.error(" Required column (RFM_Score) not found in dataset.")

elif selected_graph == "Cluster Size Comparison":
    st.header("📊 Cluster Size Comparison")
    if "KMeans_Cluster" in df.columns:
        cluster_counts = df["KMeans_Cluster"].value_counts().reset_index()
        cluster_counts.columns = ["Cluster", "Count"]
        fig = px.bar(cluster_counts, x="Cluster", y="Count", title="Cluster Size Comparison")
        st.plotly_chart(fig)
    else:
        st.error(" Required column (KMeans_Cluster) not found in dataset.")

elif selected_graph == "Final Summary":
    st.header(" Final Summary: Key Insights")

    st.subheader("1️ Purchase Frequency Distribution")
    st.write("- Most customers purchase infrequently, indicating many one-time buyers.")
    st.write("- A small percentage of customers purchase regularly, representing loyal shoppers.")

    st.subheader("2️ Customer Segmentation (KMeans & Hierarchical Clustering)")
    st.write("- **KMeans clustering reveals three key groups:**")
    st.write("  -  High-value frequent buyers (high monetary, low recency).")
    st.write("  - Occasional spenders (moderate frequency and monetary value).")
    st.write("  - Inactive customers (high recency, low frequency).")

    st.subheader("3️ Recency vs Frequency Analysis")
    st.write("- High-frequency buyers tend to have lower recency, showing strong engagement.")
    st.write("- Some clusters have high recency but low frequency, indicating lost or inactive customers.")

    st.subheader("4️ Monetary vs Frequency Analysis")
    st.write("- Customers spending higher amounts tend to purchase more frequently.")
    st.write("- Some low-frequency customers still contribute significant revenue, meaning targeted re-engagement could be beneficial.")

    st.subheader("5️ RFM Score Distribution")
    st.write("- The majority of customers have low RFM scores, meaning they are either new or inactive.")
    st.write("- A small high-score segment consists of premium customers who spend frequently and recently.")

    st.subheader("6️ Cluster Size Comparison")
    st.write("- The largest cluster consists of low-value customers, indicating room for marketing improvement.")
    st.write("- The smallest clusters contain high-value and loyal customers, emphasizing the need to retain them.")

    st.subheader(" Business Recommendations")
    st.write("-  Re-engage inactive customers through personalized offers and email campaigns.")
    st.write("-  Reward high-value customers with loyalty programs and exclusive discounts.")
    st.write("-  Convert occasional spenders into loyal customers by providing incentives for frequent purchases.")
    st.write("-  Monitor low-value clusters to understand why they aren't converting into repeat buyers.")

st.sidebar.write("\n")
