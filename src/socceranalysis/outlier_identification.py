import pandas as pd
import numpy as np

def get_outliers(df,var, method = "IQR",thresh=3):
    """Returns outliers in the dataset based on values of a variable

    This function identifies outliers in the dataset based on either of the following methods:
    
    1. Interquartile Range (IQR) Method: Identifies all values less than Q1 - 1.5*IQR and 
    greater than Q3 + 1.5*IQR where IQR = Q3-Q1, are identified as outliers.
    
    2. Mean and Standard Deviation Method: Identifies all values less than 
    mean - k*standard_deviation and greater than mean + k*standard_deviation as outliers.
    
    Parameters
    ----------
    df : pandas dataframe
        Dataframe in  which outliers are to be identified.
    var : str
        Variable in the dataframe based on which outliers are to be identified.
    method : str
        Name of the outlier identification method to be used. 
        "IQR" for IQR method and "SD" for meand and standard deviation method.
    thresh : int
        The value of k in the Mean and Standard Deviation Method formula above.

    Returns
    -------
    dataframe
        Subset of original dataframe  containing only rows corresponding to outliers.

    Examples
    --------
    >>> get_outliers("Wages","IQR",3)
    """