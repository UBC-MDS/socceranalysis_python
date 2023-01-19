from socceranalysis.outlier_identification import *
from socceranalysis.viz_stats import *
from socceranalysis.find_team_stat import *

small_data = pd.DataFrame({
        'age': np.array([19, 19, 20, 34, 21]),
        'Goals_total' : np.array([24, 1111, 4, 50, 4]),
        'Continent' : ["A","AA","AAA","B","A"],
        'Name' : ['Vincet' , 'Lous' , 'Leo', 'Flora', 'manvir'],
        'Team' : ['C' , 'D', 'E', 'F', 'G'],
        'Position_Final' :['R', 'R', 'R', 'R', 'R']
    })
small_scatter = soc_viz_stats_scatter('age','Goals_total',df = small_data)
small_hist = soc_viz_stats_hist('age',df = small_data)

data = pd.read_excel("soccer_data.xlsx")

findstat_example = find_team_stat(data, "Manchester United", "Market_Value_Euros")

def test_get_outliers():
    """Test outlier identification in a data set"""
    assert len(get_outliers(data,"Market_Value_Euros","SD",3)) == 108, "There should 108 outliers when using mean +- 3*sd on Market Value"
    assert len(get_outliers(data,"Market_Value_Euros","IQR")) == 328, "There should 328 outliers when using IQR on Market Value"
    assert len(get_outliers(data,"Wages_Euros","SD",3)) == 104, "There should 104 outliers when using SD method on Wages"
    assert len(get_outliers(data,"Wages_Euros","IQR")) == 324 , "There should 324 outliers when using IQR method on Wages"
    assert len(get_outliers(data,"Wages_Euros","IQR").columns) == 20, "The outlier dataframe is incorrect (total columns should be 20)"
    assert isinstance(data,pd.DataFrame) == True, "Input data should be a pandas dataframe"
    assert isinstance(get_outliers(data,"Wages_Euros","IQR"),pd.DataFrame) == True ,"Ouptut data should be a pandas dataframe"
    
    
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
    
    