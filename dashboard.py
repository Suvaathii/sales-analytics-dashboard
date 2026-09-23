import streamlit as st
import pandas as pd

# Page configuration
st.set_page_config(
    page_title="Sales Analytics Dashboard",
    page_icon="📊",
    layout="wide"
)

df = pd.read_csv("sales_data.csv")

# Category filter
st.sidebar.header("Filters")

categories = ["All"] + list(df["Category"].unique())

selected_category = st.sidebar.selectbox(
    "Select Category",
    categories
)

# Filter data
if selected_category == "All":
    filtered_df = df
else:
    filtered_df = df[df["Category"] == selected_category]

# Dashboard title
st.title("📊 Sales Analytics Dashboard")
st.write("Explore sales performance by category.")

# KPI Metrics
st.subheader("📊 Sales Overview")

col1, col2, col3 = st.columns(3)

with col1:
    st.metric(
        "💰 Total Sales",
        f"₹{filtered_df['Sales'].sum():,.0f}"
    )

with col2:
    st.metric(
        "📦 Total Quantity",
        f"{filtered_df['Quantity'].sum():,.0f}"
    )

with col3:
    st.metric(
        "🛍️ Products",
        filtered_df["Product"].nunique()
    )

# Category sales
st.subheader("Sales by Category")

category_sales = filtered_df.groupby("Category")["Sales"].sum()

st.bar_chart(category_sales)

# Product-wise sales
st.subheader("Sales by Product")

product_sales = filtered_df.groupby("Product")["Sales"].sum()

st.bar_chart(product_sales)

# Sales Sequence
st.subheader("📈 Sales Sequence")

sales_sequence = filtered_df["Sales"].reset_index(drop=True)

st.line_chart(sales_sequence)

# Business Insights
st.subheader("💡 Business Insights")

if not filtered_df.empty:
    top_product = (
        filtered_df.groupby("Product")["Sales"]
        .sum()
        .idxmax()
    )

    top_product_sales = (
        filtered_df.groupby("Product")["Sales"]
        .sum()
        .max()
    )

    st.write(
        f"🏆 Top Product: {top_product}"
    )

    st.write(
        f"💰 Top Product Sales: ₹{top_product_sales:,.0f}"
    )

    st.write(
        "📊 Use the category filter to compare product performance."
    )

# Raw data
st.subheader("Sales Data")

st.dataframe(filtered_df)

# Download filtered data
st.subheader("📥 Download Data")

csv = filtered_df.to_csv(index=False)

st.download_button(
    label="Download CSV",
    data=csv,
    file_name="filtered_sales_data.csv",
    mime="text/csv"
)