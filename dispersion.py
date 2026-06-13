import pandas as pd
import numpy as np

def calculate_cross_sectional_dispersion(df_returns: pd.DataFrame, method: str='CSSD')->pd.Series:
    """
    Calculate the cross-sectional dispersion of returns for each date in the DataFrame.

    Parameters:
    df_returns (pd.DataFrame): A DataFrame where each column represents a different asset and each row represents a different date.
    method (str): The method to use for calculating dispersion. Options are 'CSSD' (Cross-Sectional Standard Deviation) or 'CSD' (Cross-Sectional Dispersion).

    Returns:
    pd.Series: A Series containing the cross-sectional dispersion for each date.
    """

    mean_returns_sectors=df_returns.mean(axis=1=True)
    differences=df_returns.sub(mean_returns_sectors, axis=0)

    N= df_returns.shape[1]

    if method == 'CSSD':
        dispersion = np.sqrt((differences**2).sum(axis=1)/(N-1))
    elif method == 'CSD':
        dispersion = differences.abs().sum(axis=1)/N
    else:
        raise ValueError("Method must be either 'CSSD' or 'CSD'.")
    
    dispersion.name = f'Dispersion{method}'
    return dispersion

def calculate_rolling_dispersion(df_returns: pd.DataFrame, window: int=21, method: str='CSSD')->pd.DataFrame:
    """
    Calculate the rolling cross-sectional dispersion of returns for each date in the DataFrame.

    Parameters:
    df_returns (pd.DataFrame): A DataFrame where each column represents a different asset and each row represents a different date.
    window (int): The size of the rolling window.
    method (str): The method to use for calculating dispersion. Options are 'CSSD' (Cross-Sectional Standard Deviation) or 'CSD' (Cross-Sectional Dispersion).

    Returns:
    pd.DataFrame: A DataFrame containing the rolling cross-sectional dispersion for each date.
    """
    
    rolling_dispersion = df_returns.rolling(window=window).apply(lambda x: calculate_cross_sectional_dispersion(x, method=method), raw=False)
    
    return rolling_dispersion


