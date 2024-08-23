import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px

# Load the data
@st.cache_data
def load_data(file_path):
    data = pd.read_csv(file_path)
    return data

togo_data = load_data("../data/togo-dapaong_qc.csv")
benin_data = load_data("../data/benin-malanville.csv")
sierraleone_data = load_data("../data/sierraleone-bumbuna.csv")

# Create a Streamlit app
st.title("Solar Radiation Data Dashboard")

# Add a selectbox to select the country
st.sidebar.title("Select Country")
country = st.sidebar.selectbox("Select Country", ["Togo", "Benin", "Sierra Leone"])

# Add a selectbox to select the type of analysis
st.sidebar.title("Select Analysis Type")
analysis_type = st.sidebar.selectbox("Select Analysis Type", ["Summary Statistics", "Time Series Analysis", "Correlation Analysis", "Wind Analysis", "Temperature Analysis"])

# Add a selectbox to select the columns for analysis
st.sidebar.title("Select Columns")
if country == "Togo":
    columns = st.sidebar.multiselect("Select Columns", togo_data.columns)
elif country == "Benin":
    columns = st.sidebar.multiselect("Select Columns", benin_data.columns)
elif country == "Sierra Leone":
    columns = st.sidebar.multiselect("Select Columns", sierraleone_data.columns)

# Create a container for the analysis
with st.container():
    if country == "Togo":
        data = togo_data
    elif country == "Benin":
        data = benin_data
    elif country == "Sierra Leone":
        data = sierraleone_data

    if analysis_type == "Summary Statistics":
        # Display summary statistics
        st.subheader("Summary Statistics")
        st.write(data.describe())

    elif analysis_type == "Time Series Analysis":
        # Display time series analysis
        st.subheader("Time Series Analysis")
        fig = px.line(data, x="Timestamp", y=columns)
        st.plotly_chart(fig, use_container_width=True)

    elif analysis_type == "Correlation Analysis":
        # Display correlation analysis
        st.subheader("Correlation Analysis")
        corr_matrix = data[columns].corr()
        fig = plt.figure(figsize=(10, 8))
        sns.heatmap(corr_matrix, annot=True, cmap="coolwarm", square=True)
        st.pyplot(fig)

    elif analysis_type == "Wind Analysis":
        # Display wind analysis
        st.subheader("Wind Analysis")
        fig = px.scatter(data, x="WS", y="WD")
        st.plotly_chart(fig, use_container_width=True)

    elif analysis_type == "Temperature Analysis":
        # Display temperature analysis
        st.subheader("Temperature Analysis")
        fig = px.scatter(data, x="TModA", y="TModB")
        st.plotly_chart(fig, use_container_width=True)

# Add interactive features
st.sidebar.title("Interactive Features")
slider_value = st.sidebar.slider("Select a range of values for WS", min_value=data["WS"].min(), max_value=data["WS"].max())

# Filter the data based on the slider value
filtered_data = data[data["WS"] <= slider_value]

# Display the filtered data
st.subheader("Filtered Data")
st.write(filtered_data)