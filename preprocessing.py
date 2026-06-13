import pandas as pd
import numpy as np

def clean_data(df):
    df_clean=df.copy()
    df_clean=df_clean.fillna(method='ffill')
    df_clean.dropna(inplace=True)
    return df_clean

def compute_daily_returns(df):
    df_returns=df.pct_change()
    return df_returns.dropna(how='all')

def process_risk_free_rate(rf_series:pd.Series):
    rf_annuel=rf_series/100
    rf_daily=(1+rf_annuel)**(1/252)-1
    return rf_daily



