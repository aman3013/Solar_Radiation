import pandas as pd
from tabulate import tabulate as tb
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
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


