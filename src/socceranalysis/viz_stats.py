# Author: Gaoxiang Wang
import pandas as pd 
import altair as alt
from panel.interact import interact
import panel as pn
import numpy as np


def soc_viz_stats_scatter(x_col, y_col,df):
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
    assert (x_col in df.columns) == True, f'Column {x_col} does not exist in data frame'
    assert np.issubdtype(df[x_col].dtype, np.number) ==True, "Column used should be numeric"
    assert isinstance(y_col,str) == True, "Column named used should be passed as string"
    assert (y_col in df.columns) == True, f'Column {y_col} does not exist in data frame'
    assert np.issubdtype(df[y_col].dtype, np.number) ==True, "Column used should be numeric"
    assert set(['Name','age', 'Team','Continent','Position_Final']).issubset(set(df.columns)),  "'Name','age', 'Team','Continent','Position_Final' shoud be included "

    
    slider = alt.binding_range(
        name='age', step=1,
        min=df['age'].min(), max=df['age'].max())
    select_age = alt.selection_single(
        fields=['age'],
        bind=slider,
        init={'age': 18})
    chart = alt.Chart(df).mark_point().encode(
        x=x_col,
        y=y_col,
        tooltip=['Name','age', 'Team','Continent','Position_Final'],
        color = 'Continent',opacity=alt.condition(
        alt.datum.age < select_age.age,
        alt.value(0.7), alt.value(0.1))
).add_selection(select_age)
    return chart

def soc_viz_stats_hist(x_col, df):
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
    assert (x_col in df.columns) == True, f'Column {x_col} does not exist in data frame'
    assert np.issubdtype(df[x_col].dtype, np.number) ==True, "Column used should be numeric"
    
    chart = alt.Chart(df).mark_bar().encode(
        x=alt.X(x_col, bin=alt.Bin(maxbins=30)),
        y='count()')
    return chart



