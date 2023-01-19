
import numpy as np
import pandas as pd

def get_outliers(df,col, method = "SD",thresh=3):
    
    """Returns outliers in the dataset based on values of a variable

    This function identifies outliers in the dataset based on either of the following methods:
    
    1. Interquartile Range (IQR) Method: Identifies all values less than Q1 - 1.5*IQR and 
    greater than Q3 + 1.5*IQR where IQR = Q3-Q1, are identified as outliers.
    
    2. Mean and Standard Deviation Method: Identifies all values less than 
    mean - k*standard_deviation and greater than mean + k*standard_deviation as outliers.
    
    Parameters
    ----------
    df : dataframe
        Dataframe in  which outliers are to be identified.
    col : str
        Variable in the dataframe based on which outliers are to be identified.
    method : str
        Name of the outlier identification method to be used. 
        "IQR" for IQR method and "SD" for mean and standard deviation method.
    thresh : int
        The value of k in the Mean and Standard Deviation Method formula above.

    Returns
    -------
    dataframe
        Subset of original dataframe  containing only rows corresponding to outliers.

    Examples
    --------
    >>> get_outliers(df,"Wages_Euros","SD",3)
    """
    assert isinstance (df,pd.DataFrame) == True, "Input data must be a dataframe"
    assert isinstance(col,str) == True, "Column named used for outlier detection should be passed as string"
    assert (col in df.columns) == True, f"Column {col} does not exist in data frame"
    assert np.issubdtype(df[col].dtype, np.number) ==True, "Column used for outlier detection should be numeric"
    
    if method == "SD":
        mean = np.mean(df[col])
        std = np.std(df[col])
        outliers = df[(df[col] > mean + thresh*std) | (df[col] < mean - thresh*std)]
    
    elif method == "IQR":
        q1,q3 =  np.percentile(df[col], [25 ,75])
        iqr = q3 - q1
        outliers = df[(df[col] > q3 + 1.5*iqr) | (df[col] < q1 - 1.5*iqr)]
        
    return outliers
        
        
        
    
        