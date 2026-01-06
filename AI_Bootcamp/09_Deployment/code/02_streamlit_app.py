import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Konfigurasi Halaman
st.set_page_config(page_title="AI Dashboard", layout="wide")

st.title("🤖 Simple AI Dashboard with Streamlit")
st.write("Aplikasi web interaktif untuk visualisasi data dan prediksi AI.")

# 1. Sidebar Input
st.sidebar.header("User Input Features")
val1 = st.sidebar.slider("Input Nilai A", 0, 100, 50)
val2 = st.sidebar.slider("Input Nilai B", 0, 100, 50)

# 2. Main Content
col1, col2 = st.columns(2)

with col1:
    st.subheader("Data Visualization")
    # Generate random data
    chart_data = pd.DataFrame(
        np.random.randn(20, 3),
        columns=['a', 'b', 'c']
    )
    st.line_chart(chart_data)

with col2:
    st.subheader("Prediction Result")
    # Dummy calculation
    result = val1 * val2
    st.info(f"Hasil Perkalian Input: {result}")
    
    if result > 2500:
        st.success("High Value! 🚀")
    else:
        st.warning("Low Value ⚠️")

# 3. Data Table
st.subheader("Raw Data")
st.dataframe(chart_data)
