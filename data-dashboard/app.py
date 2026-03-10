import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.title("Data Visualization Dashboard")

uploaded_file = st.file_uploader("Upload CSV File", type=["csv"])

if uploaded_file:

    df = pd.read_csv(uploaded_file)

    st.write("Dataset Preview")
    st.write(df.head())

    st.subheader("Dataset Information")
    st.write("Rows:", df.shape[0])
    st.write("Columns:", df.shape[1])
    st.write("Column Types")
    st.write(df.dtypes)

    column = st.selectbox("Choose column for chart", df.columns)

    if df[column].dtype != "object":
        fig, ax = plt.subplots()
        df[column].hist(ax=ax)
        st.pyplot(fig)

    st.subheader("Create Custom Chart")

x_column = st.selectbox("Select X axis", df.columns)
y_column = st.selectbox("Select Y axis", df.columns)

if st.button("Generate Chart"):
    
    fig, ax = plt.subplots()
    ax.bar(df[x_column], df[y_column])
    
    plt.xticks(rotation=45)

    st.pyplot(fig)