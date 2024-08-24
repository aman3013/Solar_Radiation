import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import pandas as pd

class PlottingUtils:
    def calculate_correlation_matrix(self, df):
        """
        Calculate the correlation matrix for the given DataFrame.

        Args:
        - df (pd.DataFrame): The DataFrame containing the data.

        Returns:
        - corr_matrix (pd.DataFrame): The correlation matrix.
        """
        corr_df = df[['GHI', 'DNI', 'DHI', 'TModA', 'TModB']]
        return corr_df.corr()

    def create_correlation_heatmap(self, corr_matrix):
        """
        Create a heatmap for correlation analysis.

        Args:
        - corr_matrix (pd.DataFrame): The correlation matrix.

        Returns:
        - fig (matplotlib.figure.Figure): The figure object.
        """
        fig, ax = plt.subplots(figsize=(8, 8))
        sns.heatmap(corr_matrix, annot=True, cmap='coolwarm', square=True, ax=ax)
        ax.set_title('Correlation Analysis')
        return fig

    def create_pair_plot(self, df):
        """
        Create a pair plot for correlation analysis.

        Args:
        - df (pd.DataFrame): The DataFrame containing the data.

        Returns:
        - fig (matplotlib.figure.Figure): The figure object.
        """
        corr_df = df[['GHI', 'DNI', 'DHI', 'TModA', 'TModB']]
        fig = sns.pairplot(corr_df)
        return fig
    def create_scatter_matrix(self, df):
        """
        Create a scatter matrix for wind conditions and solar irradiance.

        Args:
        - df (pd.DataFrame): The DataFrame containing the data.

        Returns:
        - fig (matplotlib.figure.Figure): The figure object.
        """
        scatter_df = df[['WS', 'WSgust', 'WD', 'GHI', 'DNI', 'DHI']]
        fig = sns.pairplot(scatter_df, x_vars=['WS', 'WSgust', 'WD'], y_vars=['GHI', 'DNI', 'DHI'], height=4, aspect=0.8)
        return fig

    def create_polar_plot(self, df, ws_col='WS', wd_col='WD'):
        """
        Create a polar plot of wind speed and direction distribution.

        Parameters:
        df (Pandas DataFrame): Dataset containing wind speed and direction data.
        ws_col (str): Column name for wind speed data. Defaults to 'WS'.
        wd_col (str): Column name for wind direction data. Defaults to 'WD'.

        Returns:
        - fig (matplotlib.figure.Figure): The figure object.
        """
        df[f'{wd_col}_rad'] = np.radians(df[wd_col])

        fig = plt.figure(figsize=(8, 8))
        ax = fig.add_subplot(111, polar=True)

        ax.scatter(df[f'{wd_col}_rad'], df[ws_col], c=df[ws_col], cmap='viridis', alpha=0.5)

        ax.set_rlim(0, df[ws_col].max() * 1.1)  
        ax.set_rticks([max(df[ws_col]) // 4, max(df[ws_col]) // 2, max(df[ws_col]) * 3 // 4])
        ax.set_rlabel_position(270)
        ax.set_title('Wind Speed and Direction Distribution')
        ax.set_xlabel('Wind Direction (°)', labelpad=20)

        direction_labels = ['N', 'NE', 'E', 'SE', 'S', 'SW', 'W', 'NW']
        ax.set_thetagrids(22.5 * np.arange(8), direction_labels)

        return fig

    def analyze_temperature_data(self, df):
            # Create scatter plots
            fig, axes = plt.subplots(nrows=1, ncols=3, figsize=(15, 5))
            sns.scatterplot(x='RH', y='Tamb', data=df, ax=axes[0])
            axes[0].set_title('Temperature vs Relative Humidity')
            axes[0].set_xlabel('Relative Humidity (%)')
            axes[0].set_ylabel('Temperature (°C)')

            sns.scatterplot(x='RH', y='GHI', data=df, ax=axes[1])
            axes[1].set_title('Global Horizontal Irradiance vs Relative Humidity')
            axes[1].set_xlabel('Relative Humidity (%)')
            axes[1].set
            axes[1].set_ylabel('Global Horizontal Irradiance (W/m²)')

            sns.scatterplot(x='RH', y='DNI', data=df, ax=axes[2])
            axes[2].set_title('Direct Normal Irradiance vs Relative Humidity')
            axes[2].set_xlabel('Relative Humidity (%)')
            axes[2].set_ylabel('Direct Normal Irradiance (W/m²)')

            plt.tight_layout()
            return fig

    def create_histograms(self, df):
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
        axes[1, 1].set_title('Wind Speed (m/s)')
        axes[1, 1].set_xlabel('Value')
        axes[1, 1].set_ylabel('Frequency')

        axes[2, 0].hist(df['RH'], bins=50, alpha=0.5, label='RH')
        axes[2, 0].set_title('Relative Humidity (%)')
        axes[2, 0].set_xlabel('Value')
        axes[2, 0].set_ylabel('Frequency')

        axes[2, 1].hist(df['Tamb'], bins=50, alpha=0.5, label='Tamb')
        axes[2, 1].set_title('Ambient Temperature (°C)')
        axes[2, 1].set_xlabel('Value')
        axes[2, 1].set_ylabel('Frequency')

        plt.tight_layout()
        return fig

    def calculate_zscores(self, df, cols, threshold=3):
        # Calculate Z-scores for each column
        for col in cols:
            df[f'{col}_zscore'] = np.abs((df[col] - df[col].mean()) / df[col].std())

        # Flag outliers
        df['outlier'] = np.where(df[[f'{col}_zscore' for col in cols]].max(axis=1) > threshold, 1, 0)

        return df

    def create_bubble_charts(self, df, cols, bubble_col):
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
            return fig

    def create_time_series_plots(self, df):
        # Plot line graphs for GHI, DNI, DHI, and Tamb over time
        fig1, ax = plt.subplots(figsize=(10, 6))
        ax.plot(df['GHI'], label='GHI')
        ax.plot(df['DNI'], label='DNI')
        ax.plot(df['DHI'], label='DHI')
        ax.plot(df['Tamb'], label='Tamb')
        ax.legend()
        ax.set_title('Time Series Plot of GHI, DNI, DHI, and Tamb')
        ax.set_xlabel('Time')
        ax.set_ylabel('Value')

        # Plot area plots for GHI, DNI, DHI, and Tamb over time
        fig2, ax = plt.subplots(figsize=(10, 6))
        ax.fill_between(df.index, df['GHI'], label='GHI')
        ax.fill_between(df.index, df['DNI'], label='DNI')
        ax.fill_between(df.index, df['DHI'], label='DHI')
        ax.fill_between(df.index, df['Tamb'], label='Tamb')
        ax.legend()
        ax.set_title('Area Plot of GHI, DNI, DHI, and Tamb')
        ax.set_xlabel('Time')
        ax.set_ylabel('Value')

        # Create a line graph with separate lines for clean and dirty sensors
        clean_df = df[df['Cleaning'] == 1]
        dirty_df = df[df['Cleaning'] == 0]

        fig3, ax = plt.subplots(figsize=(10, 6))
        ax.plot(clean_df.index, clean_df['ModA'], label='Clean ModA')
        ax.plot(clean_df.index, clean_df['ModB'], label='Clean ModB')
        ax.plot(dirty_df.index, dirty_df['ModA'], label='Dirty ModA')
        ax.plot(dirty_df.index, dirty_df['ModB'], label='Dirty ModB')
        ax.legend()
        ax.set_title('Impact of Cleaning on Sensor Readings')
        ax.set_xlabel('Time')
        ax.set_ylabel('Value')

        return [fig1, fig2, fig3]