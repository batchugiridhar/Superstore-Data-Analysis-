import streamlit as st
import pandas as pd
import plotly.express as px
@st.cache_data
def load_data():
    return pd.read_excel("/home/sensen/Downloads/sss.xlsx")  # Update the file path accordingly
df = load_data()
st.title("Superstore Data Analysis: Order Count by City and State")
st.write("Data Preview:")
st.write(df.head())
if 'City' in df.columns and 'State' in df.columns:
    orders_count = df.groupby(['City', 'State']).size().reset_index(name='Order Count')
    fig = px.scatter(orders_count, x='City', y='Order Count', color='State', 
                     title='Order Count by City and State', 
                     labels={'Order Count': 'Number of Orders', 'City': 'City', 'State': 'State'})
    fig.update_layout(xaxis_tickangle=-45)
    st.plotly_chart(fig)
else:
    st.error("The dataset must contain 'City' and 'State' columns.")

