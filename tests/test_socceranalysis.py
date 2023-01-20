from socceranalysis.outlier_identification import *
from socceranalysis.viz_stats import *
from socceranalysis.find_team_stat import *
import pandas as pd
import numpy as np

sample_soccer_dict = {'Wages_Euros': [300000,	
                      575000,	150000,	475000,375000,	225000,	225000,	
                      200000,	225000,	250000,	250000,	375000,	200000,
                      150000,	225000,	225000,	200000,	225000,	190000,	
                      300000,	180000,	400000,	325000,	200000,	190000,	170000,	
                      300000,	140000,	225000,	350000,	190000]
                      ,
                      'Market_Value_Euros' : [105500000,	95500000,	
                      93500000,	90000000,	90000000,	83000000,	
                      80500000,	78000000,	76500000,	73000000,	
                      72500000,	69000000,	68000000,	67500000,	66000000,
                      64500000,	64000000,	62000000,	61000000,	60000000,	
                      60000000,	58500000,	57000000,	57000000,	56500000,	
                      56000000,	55000000,	54500000,	53500000,	53000000,	
                      52000000]}

sample_soccer_data = pd.DataFrame(sample_soccer_dict)  


small_data = pd.DataFrame({
        'age': np.array([19, 19, 20, 34, 21]),
        'Goals_total' : np.array([24, 1111, 4, 50, 4]),
        'Continent' : ["A","AA","AAA","B","A"],
        'Name' : ['Vincet' , 'Lous' , 'Leo', 'Flora', 'manvir'],
        'Team' : ['C' , 'D', 'E', 'F', 'G'],
        'Position_Final' :['R', 'R', 'R', 'R', 'R']
    })

test_df_1 = pd.DataFrame({
        'Name' : ['Lous' , 'Flora' , 'Vincet', 'Leo', 'manvir']
    })

test_df_2 = pd.DataFrame({
        'Name' : ['Flora' , 'manvir' , 'Leo', 'Vincet', 'Lous']
    })

test_df_3 = pd.DataFrame({
        'Name' : [ 'manvir', 'Flora' , 'Leo' , 'Lous', 'Vincet']
    })


small_scatter = soc_viz_stats_scatter('age','Goals_total',df = small_data)
small_hist = soc_viz_stats_hist('age',df = small_data)


data = pd.read_excel("soccer_data.xlsx")

findstat_example = find_team_stat(data, "Manchester United", "Market_Value_Euros")

def test_get_outliers():
    """Test outlier identification in a data set"""
    assert len(get_outliers(sample_soccer_data,"Market_Value_Euros","SD",2)) == 1, "There should 1 outlier when using mean +- 2*sd on Market Value"
    assert len(get_outliers(sample_soccer_data,"Market_Value_Euros","IQR")) == 0, "There should be no outliers when using IQR method on Market Value"
    assert len(get_outliers(sample_soccer_data,'Wages_Euros',"SD",1)) == 8, "There should 8 outliers when using SD method with threshold 1 on Wages"
    assert len(get_outliers(sample_soccer_data,'Wages_Euros',"IQR")) == 2 , "There should 2 outliers when using IQR method on Wages"
    assert len(get_outliers(sample_soccer_data,"Wages_Euros","IQR").columns) == 2, "The outlier dataframe is incorrect (total columns should be 2)"
    assert isinstance(sample_soccer_data,pd.DataFrame) == True, "Input data should be a pandas dataframe"
    
    
def test_scatter():
    assert small_scatter.encoding.x.shorthand == 'age', 'age should be in x axis'
    assert small_scatter.encoding.y.shorthand == 'Goals_total', 'Goals_total should be in y axis'
    assert small_scatter.mark == 'point', 'mark should be a point'
    assert [s['shorthand'] for s in small_scatter.encoding.tooltip] == ['Name','age', 'Team','Continent','Position_Final'], "tooltip   should contain required columns"
    assert small_scatter.encoding.color.shorthand == 'Continent', "color should be using 'Continent' column"
    
def test_hist():
    assert small_hist.encoding.x.shorthand == 'age', 'age should be in x axis'
    assert small_hist.encoding.y.shorthand =='count()', 'count() should be in y axis'
    assert small_hist.mark == 'bar', 'mark should be a bar'
    assert small_hist.encoding.x.bin.maxbins >= 20 , "maxbin should exist and set to be greater than 20"
    
def test_dashboard():
    assert soc_viz_stats_get_dashboard() == None, 'this function should return None'
    
    
def test_find_team_stat():
    "Test output is a boxplot with correct axis"
    assert isinstance(findstat_example , alt.vegalite.v4.api.Chart) == True, "Output should be an altair chart"
    assert findstat_example.mark == 'boxplot', 'mark should be a boxplot'
    assert findstat_example.encoding.x.shorthand == 'Market_Value_Euros', 'Your feature selection should be mapped to the x axis'
    assert findstat_example.encoding.y.shorthand == 'Team', 'Team should be mapped to the y axis'
    

def test_rankingplayers():
    assert rankingplayers(small_data, "Goals_total").equals(test_df_1), "The test dataframe and the function return dataframe are different"  
    assert rankingplayers(small_data, "age").equals(test_df_2), "he test dataframe and the function return dataframe are different"
    assert rankingplayers(small_data, "Team").equals(test_df_3), "he test dataframe and the function return dataframe are different"