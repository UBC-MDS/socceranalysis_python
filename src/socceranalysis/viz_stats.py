# Author: Gaoxiang Wang

import pandas as pd 
import altair as alt
from panel.interact import interact

def viz_stats(x_col, y_col,df = dat):
    """Create a scatter plot of two chosen numerical features.
    
    Parameters
    ----------
    x_col : str
        name of the feature in horizontal axis. 
    y_col : str
        name of the feature in vertical axis.
    df : pandas dataframe
        The dataframe of the feature

    Returns
    -------
    Chart: altair.vegalite.v4.api.Chart
        an altair chart
    Examples
    --------
    >>> viz_stats('age', 'Wages_EUR')
    """




def get_dashboard(cols = ['age', 'Appearances total', 'Wages_EUR', 'Goals_total', 'Yellow_Cards_Total']):
    """Display a simple dashboard of a scatter plot with dropdown menus for selecting features.
    This function can provide a quick and easy way to explore the relationship between different features in the data.
    
    Parameters
    ----------
    cols : list
        a list of column names used in both dropdown menus.

    Returns
    -------
    None
    
    Examples
    --------
    >>> interact(viz_stats,x_col= col,y_col=col).embed(max_opts=100)
    """
