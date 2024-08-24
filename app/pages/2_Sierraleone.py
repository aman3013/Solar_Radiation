import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from utils.plotting import PlottingUtils

# Create an instance of the PlottingUtils class
plotting_utils = PlottingUtils()

# Create a Streamlit app
st.title('Exploratory Data Analysis')

# Load the data
df = pd.read_csv('C:/Users/amanu/OneDrive/Desktop/week_0/data/sierraleone-bumbuna.csv')

# Create a multi-select box for plotting options
plotting_options = [
    'Correlation Heatmap',
    'Pair Plot',
    'Scatter Matrix',
    'Polar Plot',
    'Temperature Data Analysis',
    'Histograms',
    'Z-scores',
    'Bubble Charts',
    'Time Series Plots'
]

selected_options = st.multiselect('Select Plotting Options', plotting_options)

# Create a button to generate the plots
if st.button('Generate plots'):
    for option in selected_options:
        if option == 'Correlation Heatmap':
            st.write('Correlation Heatmap')
            corr_matrix = plotting_utils.calculate_correlation_matrix(df)
            fig = plotting_utils.create_correlation_heatmap(corr_matrix)
            st.pyplot(fig)
        elif option == 'Pair Plot':
            st.write('Pair Plot')
            fig = plotting_utils.create_pair_plot(df)
            st.pyplot(fig)
        elif option == 'Scatter Matrix':
            st.write('Scatter Matrix')
            fig = plotting_utils.create_scatter_matrix(df)
            st.pyplot(fig)
        elif option == 'Polar Plot':
            st.write('Polar Plot')
            fig = plotting_utils.create_polar_plot(df)
            st.pyplot(fig)
        elif option == 'Temperature Data Analysis':
            st.write('Temperature Data Analysis')
            fig = plotting_utils.analyze_temperature_data(df)
            st.pyplot(fig)
        elif option == 'Histograms':
            st.write('Histograms')
            fig = plotting_utils.create_histograms(df)
            st.pyplot(fig)
        elif option == 'Z-scores':
            st.write('Z-scores')
            zscore_df = plotting_utils.calculate_zscores(df, ['GHI', 'DNI', 'DHI', 'Tamb'])
            st.write(zscore_df)
        elif option == 'Bubble Charts':
            st.write('Bubble Charts')
            fig = plotting_utils.create_bubble_charts(df, ['GHI', 'DNI', 'DHI', 'Tamb'], 'RH')
            st.pyplot(fig)
        elif option == 'Time Series Plots':
            st.write('Time Series Plots')
            fig1, fig2, fig3 = plotting_utils.create_time_series_plots(df)
            st.pyplot(fig1)
            st.pyplot(fig2)
            st.pyplot(fig3)

else:
    st.write("Please select plotting options and click 'Generate plots' button.")