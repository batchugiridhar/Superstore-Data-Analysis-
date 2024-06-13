import streamlit as st
import pandas as pd
import plotly.express as px
@st.cache_data
def load_data():
    df = pd.read_csv("/home/sensen/Downloads/SSStore.csv")
    df['Order Date'] = pd.to_datetime(df['Order Date'], dayfirst=True)  # Convert 'Order Date' to datetime with dayfirst=True
    return df
def main():
    st.title("Yearly Quantity Sales Analysis")
    df = load_data()
    st.subheader("Data Preview")
    st.write(df.head())
    df['Year'] = df['Order Date'].dt.year
    if 'Category' in df.columns:
        yearly_category_quantity_sales = df.groupby(['Year', 'Category'])['Quantity'].sum().reset_index()
        fig = px.bar(yearly_category_quantity_sales, x='Year', y='Quantity', color='Category',
                     title="Yearly Quantity Sales by Category",
                     labels={'Quantity': 'Total Quantity Sold', 'Year': 'Year', 'Category': 'Category'})
        st.plotly_chart(fig)
    else:
        st.error("The dataset must contain a 'Category' column.")
if __name__ == "__main__":
    main()

