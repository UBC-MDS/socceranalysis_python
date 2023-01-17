from socceranalysis.outlier_identification import *

def test_get_outliers():
    """Test word counting from a file."""
    data = pd.read_excel("soccer_data.xlsx")
    assert len(get_outliers(data,"Market_Value_Euros","SD",3)) == 108, "There should 108 outliers when using mean +- 3*sd on Market Value"
    assert len(get_outliers(data,"Market_Value_Euros","IQR")) == 328, "There should 328 outliers when using IQR on Market Value"
    assert len(get_outliers(data,"Wages_Euros","SD",3)) == 104, "There should 104 outliers when using SD method on Wages"
    assert len(get_outliers(data,"Wages_Euros","IQR")) == 324 , "There should 324 outliers when using IQR method on Wages"
    assert len(get_outliers(data,"Wages_Euros","IQR").columns) == 32, "The outlier dataframe is incorrect (total columns should be 32)"
    assert isinstance(data,pd.DataFrame) == True, "Input data should be a pandas dataframe"
    assert isinstance(get_outliers(data,"Wages_Euros","IQR"),pd.DataFrame) == True ,"Ouptut data should be a pandas dataframe"
    
    
