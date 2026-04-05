import streamlit as st
import pandas as pd
import plotly.express as px

from llm import generate_insights, ask_question

# -------------------------------
# Page config
# -------------------------------
st.set_page_config(page_title="LLM Dataset Explainer", layout="wide")

st.title("📊 LLM Dataset Explainer")

# -------------------------------
# File upload
# -------------------------------
file = st.file_uploader("Upload a CSV file", type=["csv"])

if file:
    df = pd.read_csv(file)

    # -------------------------------
    # Dataset Preview
    # -------------------------------
    st.subheader("📌 Dataset Preview")
    st.dataframe(df.head())

    # -------------------------------
    # Basic Info
    # -------------------------------
    st.subheader("📊 Dataset Info")
    col1, col2 = st.columns(2)

    with col1:
        st.write(f"Rows: {df.shape[0]}")
    with col2:
        st.write(f"Columns: {df.shape[1]}")

    # -------------------------------
    # Missing Values
    # -------------------------------
    st.subheader("❗ Missing Values")
    missing = df.isnull().sum()
    missing = missing[missing > 0]

    if not missing.empty:
        st.write(missing)
    else:
        st.write("No missing values 🎉")

    # -------------------------------
    # Correlation + Charts
    # -------------------------------
    numeric_df = df.select_dtypes(include='number')

    if not numeric_df.empty:
        st.subheader("📈 Correlation Heatmap")
        corr = numeric_df.corr()

        fig = px.imshow(corr, text_auto=True)
        st.plotly_chart(fig, use_container_width=True)

        # Histogram
        st.subheader("📊 Distribution")
        col = st.selectbox("Select column", numeric_df.columns)
        fig2 = px.histogram(df, x=col)
        st.plotly_chart(fig2, use_container_width=True)

    # -------------------------------
    # AI Insights
    # -------------------------------
    st.subheader("🤖 AI Insights")

    if st.button("Generate Insights"):
        with st.spinner("Analyzing data..."):
            insights = generate_insights(df)
            st.write(insights)

    # -------------------------------
    # Ask Questions
    # -------------------------------
    st.subheader("💬 Ask Questions About Your Data")

    question = st.text_input("Type your question")

    if question:
        with st.spinner("Thinking..."):
            answer = ask_question(df, question)
            st.write(answer)

else:
    st.info("Please upload a CSV file to begin.")