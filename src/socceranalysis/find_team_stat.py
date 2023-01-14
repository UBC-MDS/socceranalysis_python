# Author: Vincent Ho

import altair as alt
import warnings
import pandas as pd

def find_team_stat(df, team_name, feature="age"):
    """Returns the descriptive statistic table and box plot of a particular team.

    This function can help users to find the statistical data of a particular team.
    A box plot is provided for visualization of the statistical data.
    Users can visualize a certain feature of the team by inputting it in the optional argument "feature".
    If no input is found, the default feature of the box plot will be the "age" of the user's inputted team.
    
    Parameters
    ----------
    df : pandas dataframe
        The dataframe of the soccer dataset. 
    team_name : str
        String in the dataframe. Users can input any string from the "Team" column.
    feature : str
        Optional argument. The default feature is "age". Users can input other numerical features.
    

    Returns
    -------
    dataframe
        Descriptive statistics include those that summarize the central tendency, 
        dispersion and shape of a dataset's distribution, excluding NaN values.
    
    Boxplot
        A visualization plot to show a certain descriptive statistic feature of a particular team.

    

    Examples
    --------
    >>> find_team_stat(soccer_df, "Manchester United", "Market Value")
    """