import pandas as pd

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
