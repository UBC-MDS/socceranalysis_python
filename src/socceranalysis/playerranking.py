# Author: Flora Ouedraogo
import pandas as pd 

def rankingplayers(df, *col_name):

    """Returns a sorted table of players based on which variables the user decide to use to rank players.
    This function can help users find the most and less important variables which can be used to compare 
    one player and the other in terms of performances. 
    
    Parameters
    ----------
    df  : pandas dataframe
        The dataframe of the soccer dataset    
    col_name : str
        The name of the columns which the user decide to use to rank the players one 
        
    Returns
    -------
    ranked_df: pandas dataframe
        This is the sorted data frame by column name
  
    Examples
    --------
    >>> rankingplayers(soccer_df, "Goals_total", "Assists_Total")
    """

    df = df.sort_values(by=[*col_name], ascending = False)
    df = pd.DataFrame(df["Name"])
    
    return df.reset_index(drop = True)