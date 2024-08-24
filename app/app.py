import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Header
st.title("Solar Energy Analysis")
st.header("Comparative Analysis of Solar Irradiance in Three Locations")

# Introduction
st.write("This analysis compares the solar irradiance in three locations. The goal is to determine which location has the highest solar irradiance and is therefore most suitable for solar energy generation.")

# File upload in sidebar
st.sidebar.title("Upload Data")
uploaded_files = {}
locations = ["Location 1", "Location 2", "Location 3"]
for i, location in enumerate(locations):
    uploaded_files[location] = st.sidebar.file_uploader(f"Upload {location} data", type='csv', key=f"{location}_file")

# Check if all files have been uploaded
if all(file is not None for file in uploaded_files.values()):
    # Load the data
    dataframes = {}
    for location, file in uploaded_files.items():
        dataframes[location] = pd.read_csv(file)

    # Calculate mean and standard deviation for GHI, DNI, and DHI for each location
    stats = {}
    for location, df in dataframes.items():
        ghi_mean = df['GHI'].mean()
        dni_mean = df['DNI'].mean()
        dhi_mean = df['DHI'].mean()
        ghi_std = df['GHI'].std()
        dni_std = df['DNI'].std()
        dhi_std = df['DHI'].std()
        
        stats[location] = {
            'GHI Mean': ghi_mean,
            'GHI StdDev': ghi_std,
            'DNI Mean': dni_mean,
            'DNI StdDev': dni_std,
            'DHI Mean': dhi_mean,
            'DHI StdDev': dhi_std
        }

    # Convert the stats dictionary to a DataFrame for easier analysis and visualization
    stats_df = pd.DataFrame(stats).T

    # Set the style for the plots
    sns.set(style="whitegrid")

    # Plotting the GHI, DNI, and DHI Mean values
    fig, axes = plt.subplots(3, 1, figsize=(10, 15))

    # Plot GHI
    sns.barplot(x=stats_df.index, y="GHI Mean", data=stats_df, ax=axes[0], palette="Blues_d")
    axes[0].set_title('Mean Global Horizontal Irradiance (GHI)')
    axes[0].set_ylabel('Mean GHI (W/m²)')

    # Plot DNI
    sns.barplot(x=stats_df.index, y="DNI Mean", data=stats_df, ax=axes[1], palette="Greens_d")
    axes[1].set_title('Mean Direct Normal Irradiance (DNI)')
    axes[1].set_ylabel('Mean DNI (W/m²)')

    # Plot DHI
    sns.barplot(x=stats_df.index, y="DHI Mean", data=stats_df, ax=axes[2], palette="Oranges_d")
    axes[2].set_title('Mean Diffuse Horizontal Irradiance (DHI)')
    axes[2].set_ylabel('Mean DHI (W/m²)')

    # Adjust layout
    plt.tight_layout()

    st.write("Mean Irradiance Values")
    st.pyplot(fig)

    # Convert 'Timestamp' column to datetime
    for location, df in dataframes.items():
        df['Timestamp'] = pd.to_datetime(df['Timestamp'])
        # Set the Timestamp as the index
        df.set_index('Timestamp', inplace=True)

    # Resample data to daily means
    daily_data = {location: df.resample('D').mean() for location, df in dataframes.items()}

    # Plotting GHI over time for each location
    fig, ax = plt.subplots(figsize=(12, 8))

    for location, df in daily_data.items():
        ax.plot(df.index, df['GHI'], label=location)

    ax.set_title('Daily Mean Global Horizontal Irradiance (GHI)')
    ax.set_xlabel('Date')
    ax.set_ylabel('Mean GHI (W/m²)')
    ax.legend(loc='upper right')
    ax.grid(True)
    ax.set_ylim(0, 600)
    ax.set_yticks([0, 100, 200, 300, 400, 500, 600])
    plt.tight_layout()

    st.write("Daily Mean GHI Values")
    st.pyplot(fig)

    # Plotting DHI over time for each location
    fig, ax = plt.subplots(figsize=(12, 8))

    for location, df in daily_data.items():
        ax.plot(df.index, df['DHI'], label=location)
    ax.set_title('Daily Mean Diffuse Horizontal Irradiance (DHI)')
    ax.set_xlabel('Date')
    ax.set_ylabel('Mean DHI (W/m²)')
    ax.legend(loc='upper right')
    ax.grid(True)
    ax.set_ylim(0, 600)
    ax.set_yticks([0, 100, 200, 300, 400, 500, 600])
    plt.tight_layout()

    st.write("Daily Mean DHI Values")
    st.pyplot(fig)

    st.write("Recommendations:")
    st.write("Based on the analysis, the location with the highest mean GHI values is:")
    st.write(stats_df['GHI Mean'].idxmax())
    st.write("The locations can be ranked as follows:")
    st.write(stats_df['GHI Mean'].sort_values(ascending=False))
    st.write("These results suggest that the location with the highest GHI values may be the best location for solar energy generation.")
    st.write("However, further analysis is needed to confirm these findings and to consider other factors such as wind speed, temperature, and humidity.")
else:
    st.write("Please upload all the required files to proceed with the analysis.")
