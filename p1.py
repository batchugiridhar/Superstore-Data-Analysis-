import streamlit as st
import pandas as pd
import plotly.express as px
@st.cache_data  # Use st.cache_data instead of st.cache
def load_data():
    return pd.read_excel("/home/sensen/Downloads/sss.xlsx")  # Update the file path accordingly
df = load_data()
st.title("Superstore Data Analysis: Number of Orders by Region and Segment")
st.write("Data Preview:")
st.write(df.head())
if 'Region' in df.columns and 'Segment' in df.columns:
    orders_count = df.groupby(['Region', 'Segment']).size().reset_index(name='Order Count')
    fig = px.bar(orders_count, x='Region', y='Order Count', color='Segment', barmode='group', 
                 title='Number of Orders by Region and Segment', 
                 labels={'Order Count': 'Number of Orders', 'Region': 'Region', 'Segment': 'Segment'})
    fig.update_layout(xaxis_tickangle=-45)
    st.plotly_chart(fig)
else:
    st.error("The dataset must contain 'Region' and 'Segment' columns.")

