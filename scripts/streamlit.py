# Import required libraries
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

# Create a title for the dashboard
st.title(" Dashboard Development Using Streamlit")

# Create a slider to select the number of data points
num_points = st.slider("Select the number of data points", 10, 100)

# Create a dropdown menu to select the type of data
data_type = st.selectbox("Select the type of data", ["Random", "Linear", "Quadratic"])

# Create a button to generate the data
if st.button("Generate Data"):
    # Generate data based on the selected type
    if data_type == "Random":
        data = pd.DataFrame({
            "x": range(num_points),
            "y": np.random.randint(1, 100, num_points)
        })
    elif data_type == "Linear":
        data = pd.DataFrame({
            "x": range(num_points),
            "y": [i * 2 for i in range(num_points)]
        })
    elif data_type == "Quadratic":
        data = pd.DataFrame({
            "x": range(num_points),
            "y": [i ** 2 for i in range(num_points)]
        })

    # Create a line chart
    fig, ax = plt.subplots()
    sns.lineplot(x="x", y="y", data=data, ax=ax)
    ax.set_title("Line Chart")
    ax.set_xlabel("X")
    ax.set_ylabel("Y")

    # Display the line chart
    st.pyplot(fig)

    # Create a bar chart
    fig, ax = plt.subplots()
    sns.barplot(x="x", y="y", data=data, ax=ax)
    ax.set_title("Bar Chart")
    ax.set_xlabel("X")
    ax.set_ylabel("Y")

    # Display the bar chart
    st.pyplot(fig)

    # Create a scatter plot
    fig, ax = plt.subplots()
    sns.scatterplot(x="x", y="y", data=data, ax=ax)
    ax.set_title("Scatter Plot")
    ax.set_xlabel("X")
    ax.set_ylabel("Y")

    # Display the scatter plot
    st.pyplot(fig)
