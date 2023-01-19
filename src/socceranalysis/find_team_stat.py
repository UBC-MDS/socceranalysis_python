# Author: Vincent Ho
import pandas as pd
import altair as alt
from IPython.display import display


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
    >>> find_team_stat(soccer_df, "Manchester United", "Market_Value_Euros")
    """
    
    if not isinstance(df, pd.DataFrame):
        raise TypeError("The data must be in type of Pandas DataFrame.")
        
    if not isinstance(team_name, str):
            raise TypeError("Incorrect type in argument: `team_name`. Please pass in a string for `team_name`, and follow the team name format under column 'Team' in the dataset.")
            
    if not isinstance(feature, str):
            raise TypeError("Incorrect type in argument: `feature`. Please pass in a string for `feature`, and follow the name format of any numerical column in the dataset.") 
    
    team_df = df.query(f"Team==@team_name")
    
    display(team_df.describe())
    
    box_plot = alt.Chart(team_df).mark_boxplot().encode( x = feature, y = "Team")
    
    return box_plot