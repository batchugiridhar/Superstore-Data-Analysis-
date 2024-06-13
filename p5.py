import streamlit as st
import pandas as pd
import plotly.express as px
@st.cache_data
def load_data():
    return pd.read_excel("/home/sensen/Downloads/sss.xlsx")  # Update the file path accordingly
df = load_data()
st.title("Superstore Data Analysis: Top 10 States by Order Count")
st.write("Data Preview:")
st.write(df.head())
if 'State' in df.columns:
    state_order_count = df['State'].value_counts().reset_index()
    state_order_count.columns = ['State', 'Order Count']
    top_10_states = state_order_count.head(10)
    fig = px.pie(top_10_states, values='Order Count', names='State', 
                 title='Top 10 States by Order Count')
    st.plotly_chart(fig)
else:
   st.error("The dataset must contain 'State' column.")

