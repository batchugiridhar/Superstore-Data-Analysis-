import streamlit as st
import pandas as pd
import plotly.express as px
@st.cache_data
def load_data():
    return pd.read_excel("/home/sensen/Downloads/sss.xlsx")  # Update the file path accordingly
df = load_data()
st.title("Superstore Data Analysis: Number of Orders by Ship Mode")
st.write("Data Preview:")
st.write(df.head())
if 'Ship Mode' in df.columns and 'Order ID' in df.columns:
    orders_by_ship_mode = df.groupby('Ship Mode')['Order ID'].count().reset_index(name='Order Count')
    fig = px.pie(orders_by_ship_mode, values='Order Count', names='Ship Mode', 
                 title='Number of Orders by Ship Mode')
    st.plotly_chart(fig)
else:
    st.error("The dataset must contain 'Ship Mode' column.")

