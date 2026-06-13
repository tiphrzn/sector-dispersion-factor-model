#Model to answer the question: "Does the market react differently tomorrow if the dispersion is exceptionnaly high or low today? "

import pandas as pd
import numpy as np

def identify_dispersion_regimes(dispersion_series:pd.Series, window:int=252, threshold: float=1.0)->pd.Series:
    """
    Identify dispersion regimes using the sliding Z-score

    Args:
        dispersion_series (pd.Series): La série de dispersion 
        window: fenetre pour la moyenne et l'écart type
        threshold: seuil du Z-score (1.0= top 16% d'une loi normale)
    returns:
        Série catégorielle('High','Normal','Low')
    """

    roll_mean=dispersion_series.rolling(window=window).mean()
    roll_std=dispersion_series.rolling(window=window).std()

    z_score=(dispersion_series-roll_mean)/roll_std

    regimes=pd.Series('Normal', index=dispersion_series.index)
    regimes.loc[z_score>threshold] = 'High'
    regimes.loc[z_score<threshold]='Low'

    regimes.loc[z_score.isna()]=np.nan

    return regimes




