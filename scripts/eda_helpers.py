import pandas as pd
from tabulate import tabulate as tb
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import statsmodels.api as sm
def read_csv_to_df(file_path):
    """
    Reads a CSV file into a pandas DataFrame.

    Args:
    file_path (str): The path to the CSV file.

    Returns:
    pd.DataFrame: A pandas DataFrame containing the data from the CSV file.
    """
    try:
        df = pd.read_csv(file_path)
        return df
    except FileNotFoundError:
        print(f"File not found at {file_path}. Please check the file path.")
        return None
    except pd.errors.EmptyDataError:
        print(f"No data in file {file_path}.")
        return None
    except pd.errors.ParserError as e:
        print(f"Error parsing file {file_path}: {e}")
        return None

def describe_df(df):
    """
    Describes a pandas DataFrame.

    Args:
    df (pd.DataFrame): The DataFrame to describe.

    Returns:
    None
    """
    if not isinstance(df, pd.DataFrame):
        print("Error: Input is not a pandas DataFrame.")
        return

    # Get the DataFrame shape
    rows, cols = df.shape
    print(f"Shape: {rows} rows, {cols} columns")

    # Get the data types of each column
    print("\nData Types:")
    print(df.dtypes)

    # Get the summary statistics for numeric columns
    numeric_df = df.select_dtypes(include=['int64', 'float64'])
    if not numeric_df.empty:
        print("\nSummary Statistics:")
        print(numeric_df.describe())

    # Get the unique values for categorical columns
    categorical_df = df.select_dtypes(include=['object'])
    if not categorical_df.empty:
        print("\nUnique Values for Categorical Columns:")
        for col in categorical_df.columns:
            print(f"{col}: {df[col].nunique()} unique values")

    # Check for missing values
    missing_values = df.isnull().sum()
    if missing_values.any():
        print("\nMissing Values:")
        print(missing_values)
    else:
        print("\nNo missing values found.")
import pandas as pd

def summary_statistics(df):
    """
    Generates summary statistics for a pandas DataFrame.

    Args:
    df (pd.DataFrame): The DataFrame to generate summary statistics for.

    Returns:
    None
    """
    # Check if input is a pandas DataFrame
    if not isinstance(df, pd.DataFrame):
        raise ValueError("Input is not a pandas DataFrame.")

    # Check for empty DataFrame
    if df.empty:
        print("Error: DataFrame is empty.")
        return

    # Get the summary statistics for numeric columns
    numeric_df = df.select_dtypes(include=['int64', 'float64'])
    if not numeric_df.empty:
        print("Summary Statistics:")
        print(numeric_df.describe())
    else:
        print("No numeric columns found.")

    # Get the summary statistics for non-numeric columns
    non_numeric_df = df.select_dtypes(exclude=['int64', 'float64'])
    if not non_numeric_df.empty:
        print("\nNon-Numeric Columns:")
        for col in non_numeric_df.columns:
            print(f"Column: {col}")
            print(non_numeric_df[col].value_counts())
            print()
    else:
        print("No non-numeric columns found.")




def check_missing_values(df):
    """
    Checks for missing values in a pandas DataFrame.

    Args:
    df (pd.DataFrame): The DataFrame to check for missing values.

    Returns:
    None
    """
    missing_values = df.isnull().sum()
    if missing_values.any():
        print("Missing Values:")
        print(missing_values[missing_values > 0])
    else:
        print("No missing values found.")

def check_outliers(df):
    """
    Checks for outliers in numeric columns of a pandas DataFrame.

    Args:
    df (pd.DataFrame): The DataFrame to check for outliers.

    Returns:
    None
    """
    numeric_df = df.select_dtypes(include=['int64', 'float64'])
    if not numeric_df.empty:
        print("\nOutliers:")
        for col in numeric_df.columns:
            q1 = numeric_df[col].quantile(0.25)
            q3 = numeric_df[col].quantile(0.75)
            iqr = q3 - q1
            lower_bound = q1 - 1.5 * iqr
            upper_bound = q3 + 1.5 * iqr
            outliers = numeric_df[(numeric_df[col] < lower_bound) | (numeric_df[col] > upper_bound)]
            if not outliers.empty:
                print(f"Column: {col}")
                print(outliers)
            else:
                print(f"No outliers found in column: {col}")
    else:
        print("No numeric columns found.")

def check_incorrect_entries(df):
    """
    Checks for incorrect entries (e.g., negative values where only positive should exist) in a pandas DataFrame.

    Args:
    df (pd.DataFrame): The DataFrame to check for incorrect entries.

    Returns:
    None
    """
    print("\nIncorrect Entries:")
    for col in df.columns:
        if df[col].dtype.kind in 'bifc':
            # Check for negative values in columns that should not have them
            if (df[col] < 0).any():
                print(f"Column: {col} has negative values.")
            else:
                print(f"No negative values found in column: {col}")
        elif df[col].dtype.kind == 'O':
            # Check for invalid categories in categorical columns
            if df[col].isnull().any():
                print(f"Column: {col} has missing values.")
            else:
                print(f"No missing values found in column: {col}")
        else:
            print(f"Column: {col} has no incorrect entries.")

# def data_quality_check(df):
#     """
#     Performs a data quality check on a pandas DataFrame.

#     Args:
#     df (pd.DataFrame): The DataFrame to perform data quality check on.

#     Returns:
#     None
#     """
#     check_outliers(df)
#     check_incorrect_entries(df)



def calculate_correlation_matrix(df):
    """
    Calculate the correlation matrix for the given DataFrame.

    Args:
    - df (pd.DataFrame): The DataFrame containing the data.

    Returns:
    - corr_matrix (pd.DataFrame): The correlation matrix.
    """
    corr_df = df[['GHI', 'DNI', 'DHI', 'TModA', 'TModB']]
    return corr_df.corr()

def create_correlation_heatmap(corr_matrix):
    """
    Create a heatmap for correlation analysis.

    Args:
    - corr_matrix (pd.DataFrame): The correlation matrix.

    Returns:
    - None
    """
    plt.figure(figsize=(8, 8))
    sns.heatmap(corr_matrix, annot=True, cmap='coolwarm', square=True)
    plt.title('Correlation Analysis')
    plt.show()

def create_pair_plot(df):
    """
    Create a pair plot for correlation analysis.

    Args:
    - df (pd.DataFrame): The DataFrame containing the data.

    Returns:
    - None
    """
    corr_df = df[['GHI', 'DNI', 'DHI', 'TModA', 'TModB']]
    plt.figure(figsize=(10, 8))
    sns.pairplot(corr_df)
    plt.title('Pair Plot for Correlation Analysis')
    plt.show()

def create_scatter_matrix(df):
    """
    Create a scatter matrix for wind conditions and solar irradiance.

    Args:
    - df (pd.DataFrame): The DataFrame containing the data.

    Returns:
    - None
    """
    scatter_df = df[['WS', 'WSgust', 'WD', 'GHI', 'DNI', 'DHI']]
    plt.figure(figsize=(10, 8))
    sns.pairplot(scatter_df, x_vars=['WS', 'WSgust', 'WD'], y_vars=['GHI', 'DNI', 'DHI'], height=4, aspect=0.8)
    plt.title('Scatter Matrix for Wind Conditions and Solar Irradiance')
    plt.show()


def create_polar_plot(df, ws_col='WS', wd_col='WD'):
    """
    Create a polar plot of wind speed and direction distribution.

    Parameters:
    df (Pandas DataFrame): Dataset containing wind speed and direction data.
    ws_col (str): Column name for wind speed data. Defaults to 'WS'.
    wd_col (str): Column name for wind direction data. Defaults to 'WD'.

    Returns:
    None
    """
    # Ensure wd is in radians for plotting
    df[f'{wd_col}_rad'] = np.radians(df[wd_col])

    # Create a polar plot
    fig = plt.figure(figsize=(8, 8))
    ax = fig.add_subplot(111, polar=True)

    # Plot wind speed and direction
    ax.scatter(df[f'{wd_col}_rad'], df[ws_col], c=df[ws_col], cmap='viridis', alpha=0.5)

    # Set plot limits and labels
    ax.set_rlim(0, df[ws_col].max() * 1.1)  # Set y-axis limit to max wind speed
    ax.set_rticks([max(df[ws_col]) // 4, max(df[ws_col]) // 2, max(df[ws_col]) * 3 // 4])
    ax.set_rlabel_position(270)
    ax.set_title('Wind Speed and Direction Distribution')
    ax.set_xlabel('Wind Direction (°)', labelpad=20)

    # Add direction labels
    direction_labels = ['N', 'NE', 'E', 'SE', 'S', 'SW', 'W', 'NW']
    ax.set_thetagrids(22.5 * np.arange(8), direction_labels)

    plt.show()

def analyze_temperature_data(df):
    # Create scatter plots
    fig, axes = plt.subplots(nrows=1, ncols=3, figsize=(15, 5))
    sns.scatterplot(x='RH', y='Tamb', data=df, ax=axes[0])
    axes[0].set_title('Temperature vs Relative Humidity')
    axes[0].set_xlabel('Relative Humidity (%)')
    axes[0].set_ylabel('Temperature (°C)')

    sns.scatterplot(x='RH', y='GHI', data=df, ax=axes[1])
    axes[1].set_title('Global Horizontal Irradiance vs Relative Humidity')
    axes[1].set_xlabel('Relative Humidity (%)')
    axes[1].set_ylabel('Global Horizontal Irradiance (W/m²)')

    sns.scatterplot(x='RH', y='DNI', data=df, ax=axes[2])
    axes[2].set_title('Direct Normal Irradiance vs Relative Humidity')
    axes[2].set_xlabel('Relative Humidity (%)')
    axes[2].set_ylabel('Direct Normal Irradiance (W/m²)')

    plt.tight_layout()
    plt.show()

    # Calculate correlations
    correlation_matrix = df[['Tamb', 'RH', 'GHI', 'DNI']].corr()
    print(correlation_matrix)


def create_histograms(df):
    # Create a figure with multiple subplots
    fig, axes = plt.subplots(nrows=3, ncols=2, figsize=(15, 10))

    # Plot histograms
    axes[0, 0].hist(df['GHI'], bins=50, alpha=0.5, label='GHI')
    axes[0, 0].set_title('Global Horizontal Irradiance (W/m²)')
    axes[0, 0].set_xlabel('Value')
    axes[0, 0].set_ylabel('Frequency')

    axes[0, 1].hist(df['DNI'], bins=50, alpha=0.5, label='DNI')
    axes[0, 1].set_title('Direct Normal Irradiance (W/m²)')
    axes[0, 1].set_xlabel('Value')
    axes[0, 1].set_ylabel('Frequency')

    axes[1, 0].hist(df['DHI'], bins=50, alpha=0.5, label='DHI')
    axes[1, 0].set_title('Diffuse Horizontal Irradiance (W/m²)')
    axes[1, 0].set_xlabel('Value')
    axes[1, 0].set_ylabel('Frequency')

    axes[1, 1].hist(df['WS'], bins=50, alpha=0.5, label='WS')

def calculate_zscores(df, cols, threshold=3):
    # Calculate Z-scores for each column
    for col in cols:
        df[f'{col}_zscore'] = np.abs((df[col] - df[col].mean()) / df[col].std())

    # Flag outliers
    df['outlier'] = np.where(df[[f'{col}_zscore' for col in cols]].max(axis=1) > threshold, 1, 0)

    return df


def create_bubble_charts(df, cols, bubble_col):
    # Create a figure with multiple subplots
    fig, axes = plt.subplots(nrows=2, ncols=2, figsize=(10, 10))

    # Plot bubble chart for GHI vs. Tamb vs. WS with bubble size representing RH or BP
    axes[0, 0].scatter(df['GHI'], df['Tamb'], s=df[bubble_col] * 10, alpha=0.5, label='GHI vs. Tamb vs. WS')
    axes[0, 0].set_title(f'GHI vs. Tamb vs. WS with {bubble_col}')
    axes[0, 0].set_xlabel('GHI (W/m²)')
    axes[0, 0].set_ylabel('Tamb (°C)')

    # Plot bubble chart for GHI vs. Tamb vs. WS with bubble size representing RH or BP
    axes[0, 1].scatter(df['GHI'], df['Tamb'], s=df[bubble_col] * 0.1, alpha=0.5, label='GHI vs. Tamb vs. WS')
    axes[0, 1].set_title(f'GHI vs. Tamb vs. WS with {bubble_col}')
    axes[0, 1].set_xlabel('GHI (W/m²)')
    axes[0, 1].set_ylabel('Tamb (°C)')

    # Plot bubble chart for DNI vs. Tamb vs. WS with bubble size representing RH or BP
    axes[1, 0].scatter(df['DNI'], df['Tamb'], s=df[bubble_col] * 10, alpha=0.5, label='DNI vs. Tamb vs. WS')
    axes[1, 0].set_title(f'DNI vs. Tamb vs. WS with {bubble_col}')
    axes[1, 0].set_xlabel('DNI (W/m²)')
    axes[1, 0].set_ylabel('Tamb (°C)')

    # Plot bubble chart for DNI vs. Tamb vs. WS with bubble size representing RH or BP
    axes[1, 1].scatter(df['DNI'], df['Tamb'], s=df[bubble_col] * 0.1, alpha=0.5, label='DNI vs. Tamb vs. WS')
    axes[1, 1].set_title(f'DNI vs. Tamb vs. WS with {bubble_col}')
    axes[1, 1].set_xlabel('DNI (W/m²)')
    axes[1, 1].set_ylabel('Tamb (°C)')

    plt.tight_layout()
    plt.show()

def create_time_series_plots(df):
    # Plot line graphs for GHI, DNI, DHI, and Tamb over time
    plt.figure(figsize=(10, 6))
    plt.plot(df['GHI'], label='GHI')
    plt.plot(df['DNI'], label='DNI')
    plt.plot(df['DHI'], label='DHI')
    plt.plot(df['Tamb'], label='Tamb')
    plt.legend()
    plt.title('Time Series Plot of GHI, DNI, DHI, and Tamb')
    plt.xlabel('Time')
    plt.ylabel('Value')
    plt.show()

    # Plot area plots for GHI, DNI, DHI, and Tamb over time
    plt.figure(figsize=(10, 6))
    plt.fill_between(df.index, df['GHI'], label='GHI')
    plt.fill_between(df.index, df['DNI'], label='DNI')
    plt.fill_between(df.index, df['DHI'], label='DHI')
    plt.fill_between(df.index, df['Tamb'], label='Tamb')
    plt.legend()
    plt.title('Area Plot of GHI, DNI, DHI, and Tamb')
    plt.xlabel('Time')
    plt.ylabel('Value')
    plt.show()

    # Create a line graph with separate lines for clean and dirty sensors
    clean_df = df[df['Cleaning'] == 1]
    dirty_df = df[df['Cleaning'] == 0]

    plt.figure(figsize=(10, 6))
    plt.plot(clean_df.index, clean_df['ModA'], label='Clean ModA')
    plt.plot(clean_df.index, clean_df['ModB'], label='Clean ModB')
    plt.plot(dirty_df.index, dirty_df['ModA'], label='Dirty ModA')
    plt.plot(dirty_df.index, dirty_df['ModB'], label='Dirty ModB')
    plt.legend()
    plt.title('Impact of Cleaning on Sensor Readings')
    plt.xlabel('Time')
    plt.ylabel('Value')
    plt.show()




def clean_data(df):
    """
    Clean the input DataFrame by handling missing values and anomalies.

    Args:
    - df (pd.DataFrame): Input DataFrame to be cleaned.

    Returns:
    - cleaned_df (pd.DataFrame): Cleaned DataFrame.
    """

    # Check if the input is a pandas DataFrame
    if not isinstance(df, pd.DataFrame):
        raise ValueError("Input must be a pandas DataFrame")

    # Handle missing values in the Comments column
    if 'Comments' in df.columns:
        if df['Comments'].isnull().all():
            df = df.drop('Comments', axis=1)

    # Identify numerical and categorical columns
    num_cols = df.select_dtypes(include=['int64', 'float64']).columns
    cat_cols = df.select_dtypes(include=['object']).columns

    # Mean imputation for numerical columns
    df[num_cols] = df[num_cols].fillna(df[num_cols].mean())

    # Forward fill for categorical columns
    df[cat_cols] = df[cat_cols].fillna(method='ffill')

    # Handle anomalies in numerical columns
    mask = np.ones(len(df), dtype=bool)
    for col in num_cols:
        Q1 = df[col].quantile(0.25)
        Q3 = df[col].quantile(0.75)
        IQR = Q3 - Q1
        mask = mask & ((df[col] >= (Q1 - 1.5 * IQR)) & (df[col] <= (Q3 + 1.5 * IQR)))

    df = df[mask]

    return df





