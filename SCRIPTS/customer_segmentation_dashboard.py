import streamlit as st
import pandas as pd
import plotly.express as px
import os

# Set Streamlit page configuration
st.set_page_config(page_title="Customer Segmentation Dashboard", layout="wide")

# Define file paths
DATA_DIR = os.path.join(os.path.dirname(__file__), "DATA")
CLUSTERED_RFM_FILE = os.path.join(DATA_DIR, "clustered_rfm.csv")

# Load Data
@st.cache_data
def load_data():
    if os.path.exists(CLUSTERED_RFM_FILE):
        return pd.read_csv(CLUSTERED_RFM_FILE)
    else:
        st.error(f"File not found: {CLUSTERED_RFM_FILE}")
        return pd.DataFrame()

df = load_data()

# Debugging - Ensure Data is Loaded
if not df.empty:
    st.write("### 🔍 Data Preview:")
    st.write(df.head())  # Check if data loads properly
    st.write("### 📊 Column Names:", df.columns.tolist())  # Show column names
else:
    st.stop()

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
    st.header("📊 Purchase Frequency Distribution")
    fig = px.histogram(df, x="Frequency", nbins=50, title="Customer Purchase Frequency")
    st.plotly_chart(fig)
    
elif selected_graph == "Customer Clusters Based on RFM":
    st.header("📊 Customer Clusters Based on RFM")
    if all(col in df.columns for col in ["Recency", "Monetary", "KMeans_Cluster"]):
        fig = px.scatter(df, x="Recency", y="Monetary", color="KMeans_Cluster", title="Customer Clusters")
        st.plotly_chart(fig)
    else:
        st.error("⚠️ Required columns not found in dataset.")

elif selected_graph == "Cluster Comparison Scatter Plot":
    st.header("📊 Cluster Comparison Scatter Plot")
    if all(col in df.columns for col in ["Recency", "Frequency", "KMeans_Cluster"]):
        fig = px.scatter(df, x="Recency", y="Frequency", color="KMeans_Cluster", title="Cluster Comparison")
        st.plotly_chart(fig)
    else:
        st.error("⚠️ Required columns not found in dataset.")

elif selected_graph == "Recency vs Frequency Analysis":
    st.header("📊 Recency vs Frequency Analysis")
    if all(col in df.columns for col in ["Recency", "Frequency"]):
        fig = px.scatter(df, x="Recency", y="Frequency", title="Recency vs Frequency")
        st.plotly_chart(fig)
    else:
        st.error("⚠️ Required columns not found in dataset.")

elif selected_graph == "Monetary vs Frequency Analysis":
    st.header("📊 Monetary vs Frequency Analysis")
    if all(col in df.columns for col in ["Monetary", "Frequency"]):
        fig = px.scatter(df, x="Monetary", y="Frequency", title="Monetary vs Frequency")
        st.plotly_chart(fig)
    else:
        st.error("⚠️ Required columns not found in dataset.")

elif selected_graph == "RFM Score Distribution":
    st.header("📊 RFM Score Distribution")
    if "RFM_Score" in df.columns:
        fig = px.histogram(df, x="RFM_Score", nbins=20, title="RFM Score Distribution")
        st.plotly_chart(fig)
    else:
        st.error("⚠️ Required column not found in dataset.")

elif selected_graph == "Cluster Size Comparison":
    st.header("📊 Cluster Size Comparison")
    if "KMeans_Cluster" in df.columns:
        cluster_counts = df["KMeans_Cluster"].value_counts().reset_index()
        cluster_counts.columns = ["Cluster", "Count"]
        fig = px.bar(cluster_counts, x="Cluster", y="Count", title="Cluster Size Comparison")
        st.plotly_chart(fig)
    else:
        st.error("⚠️ Required column not found in dataset.")

elif selected_graph == "Final Summary":
    st.header("📌 Final Summary: Key Insights")
    st.write("### Key Takeaways")
    st.write("- Majority of customers are one-time buyers.")
    st.write("- Some customers spend high amounts but purchase infrequently.")
    st.write("- Cluster segmentation can help target marketing strategies.")
    st.write("- Recommendations: Re-engagement campaigns, loyalty programs, etc.")
