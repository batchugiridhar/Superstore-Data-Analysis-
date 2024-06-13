import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Title of the app
st.title("Superstore Data Analysis: Number of Orders by Region and Segment")

# Upload file
uploaded_file = st.file_uploader("Choose a file", type=["csv", "xlsx"])

if uploaded_file is not None:
    # Read the uploaded file
    if uploaded_file.name.endswith('.csv'):
        df = pd.read_csv(uploaded_file)
    else:
        df = pd.read_excel(uploaded_file)

    st.write("Data Preview:")
    st.write(df.head())

    # Ensure the necessary columns are present
    if 'Region' in df.columns and 'Segment' in df.columns and 'Order ID' in df.columns:
        # Group by region and segment while counting the number of orders
        order_count = df.groupby(['Region', 'Segment'])['Order ID'].count().reset_index()
        order_count.rename(columns={'Order ID': 'Number of Orders'}, inplace=True)

        st.write("Number of Orders by Region and Segment:")
        st.write(order_count)

        # Plotting
        fig, ax = plt.subplots()
        sns.barplot(data=order_count, x='Region', y='Number of Orders', hue='Segment', ax=ax)
        ax.set_title("Number of Orders by Region and Segment")
        ax.set_ylabel("Number of Orders")
        ax.set_xlabel("Region")
        plt.xticks(rotation=45)
        st.pyplot(fig)
    else:
        st.error("The dataset must contain 'Region', 'Segment', and 'Order ID' columns.")

