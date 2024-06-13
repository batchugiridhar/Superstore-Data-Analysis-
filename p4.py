import streamlit as st
import pandas as pd
import plotly.express as px
@st.cache_data
def load_data():
    return pd.read_excel("/home/sensen/Downloads/sss.xlsx")  # Update the file path accordingly
df = load_data()
st.title("Superstore Data Analysis: Ship Mode by Segment")
st.write("Data Preview:")
st.write(df.head())
if 'Ship Mode' in df.columns and 'Segment' in df.columns:
    ship_mode_segment_count = df.groupby(['Ship Mode', 'Segment']).size().reset_index(name='Order Count')
    fig = px.bar(ship_mode_segment_count, x='Ship Mode', y='Order Count', color='Segment', 
                 title='Ship Mode by Segment', 
                 labels={'Order Count': 'Number of Orders', 'Ship Mode': 'Ship Mode', 'Segment': 'Segment'},
                 barmode='group')
    fig.update_layout(xaxis_tickangle=-45)
    st.plotly_chart(fig)
else:
    st.error("The dataset must contain 'Ship Mode' and 'Segment' columns.")

