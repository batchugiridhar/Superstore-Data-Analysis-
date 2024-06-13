import streamlit as st
import pandas as pd
import plotly.express as px
@st.cache_data  # Use st.cache_data instead of st.cache
def load_data():
    return pd.read_excel("/home/sensen/Downloads/sss.xlsx")  # Update the file path accordingly
df = load_data()
st.title("Superstore Data Analysis: Order Count by Category and Sub-Category")
st.write("Data Preview:")
st.write(df.head())
if 'Category' in df.columns and 'Sub-Category' in df.columns:
    orders_count = df.groupby(['Category', 'Sub-Category']).size().reset_index(name='Order Count')
    fig = px.bar(orders_count, x='Category', y='Order Count', color='Sub-Category', barmode='group', 
                 title='Order Count by Category and Sub-Category', 
                 labels={'Order Count': 'Number of Orders', 'Category': 'Category', 'Sub-Category': 'Sub-Category'})
    fig.update_layout(xaxis_tickangle=-45)
    st.plotly_chart(fig)
else:
    st.error("The dataset must contain 'Category' and 'Sub-Category' columns.")

