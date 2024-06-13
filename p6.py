import streamlit as st
import pandas as pd
import plotly.express as px
@st.cache_data
def load_data():
    return pd.read_excel("/home/sensen/Downloads/sss.xlsx")  # Update the file path accordingly
df = load_data()
st.title("Superstore Data Analysis: Order Quantity by Region")
st.write("Data Preview:")
st.write(df.head())
if 'Region' in df.columns and 'Quantity' in df.columns:
    region_order_quantity = df.groupby('Region')['Quantity'].sum().reset_index()
    fig = px.bar(region_order_quantity, x='Region', y='Quantity', 
                 title='Order Quantity by Region',
                 labels={'Quantity': 'Total Order Quantity', 'Region': 'Region'})
    fig.update_layout(xaxis_tickangle=-45)
    st.plotly_chart(fig)
else:
   st.error("The dataset must contain 'Region' and 'Quantity' columns.")

