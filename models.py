#Model to answer the question: "Does the market react differently tomorrow if the dispersion is exceptionnaly high or low today? "

import pandas as pd
import numpy as np

def identify_dispersion_regimes(dispersion_series:pd.Series, window:int=252, threshold: float=1.0)->pd.Series:

    
