# Author: Gaoxiang Wang
import pandas as pd 
import altair as alt
from panel.interact import interact
import panel as pn
import numpy as np
# using Altair with panel in the next cell
pn.extension('vega')   
# load data
data = pd.read_excel("soccer_data.xlsx")

def soc_viz_stats_scatter(x_col, y_col,df=data):
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
    >>> data = pd.read_excel("soccer_data.xlsx")
    >>> soc_viz_stats_scatter('age', 'Wages_Euros', data)
    """
    assert isinstance(x_col,str) == True, "Column named used should be passed as string"
    assert (x_col in df.columns) == True, f'Column {col} does not exist in data frame'
    assert np.issubdtype(df[x_col].dtype, np.number) ==True, "Column used should be numeric"
    assert isinstance(y_col,str) == True, "Column named used should be passed as string"
    assert (y_col in df.columns) == True, f'Column {col} does not exist in data frame'
    assert np.issubdtype(df[y_col].dtype, np.number) ==True, "Column used should be numeric"
    assert set(['Name','age', 'Team','Continent','Position_Final']).issubset(set(df.columns)),  "'Name','age', 'Team','Continent','Position_Final' shoud be included "
    
    chart = alt.Chart(df).mark_point().encode(
        x=x_col,
        y=y_col,
        tooltip=['Name','age', 'Team','Continent','Position_Final'],
        color = 'Continent')
    return chart

def soc_viz_stats_hist(x_col, df=data):
    """Create a histogram of one chosen numerical feature.
    
    Parameters
    ----------
    x_col : str
        name of the feature in horizontal axis. 

        name of the feature in vertical axis.
    df : pandas dataframe
        The dataframe of the feature

    Returns
    -------
    Chart: altair.vegalite.v4.api.Chart
        an altair chart
    Examples
    --------
    >>> data = pd.read_excel("soccer_data.xlsx")
    >>> soc_viz_stats_hist('age', data)
    """
    assert isinstance(x_col,str) == True, "Column named used should be passed as string"
    assert (x_col in df.columns) == True, f'Column {col} does not exist in data frame'
    assert np.issubdtype(df[x_col].dtype, np.number) ==True, "Column used should be numeric"
    
    chart = alt.Chart(df).mark_bar().encode(
        x=alt.X(x_col, bin=alt.Bin(maxbins=30)),
        y='count()')
    return chart



def soc_viz_stats_get_dashboard(single_col_vis = True , col = ['age', 'Appearances total', 'Wages_Euros', 'Goals_total', 'Yellow_Cards_Total']):
    """Display a simple dashboard of a scatter plot with dropdown menus for selecting features.
    This function can provide a quick and easy way to explore the relationship between different features in the data.
    
    Parameters
    ----------
    df : pandas dataframe
        The dataframe of the feature
    single_col_vis: Bool
        Indicator to Use historgram or scatterplot
    col : list
        a list of column names used in the dropdown menus.

    Returns
    -------
    None
    
    Examples
    --------
    >>> soc_viz_stats_get_dashboard(single_col_vis = True , col = ['age', 'Appearances total', 'Wages_Euros', 'Goals_total',  'Yellow_Cards_Total'])
    """
    assert isinstance(single_col_vis,bool) == True, "single_col_vis should be a binary input"
    assert isinstance(col,list) == True, "Column named used should be passed as a list"
    
    if single_col_vis:
        interact(soc_viz_stats_hist, x_col=col ).embed(max_opts=100)
    else:
        interact(soc_viz_stats_scatter,x_col= col, y_col=col).embed(max_opts=100)