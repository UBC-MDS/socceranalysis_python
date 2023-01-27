[![docs](https://img.shields.io/docsrs/passing)](https://soccer-analysis-python.readthedocs.io/en/latest/)

# socceranalysis

socceranalysis is a powerful Python package designed to make it easy to analyze and understand soccer statistics. With its set of functions, you can quickly obtain summary statistics for a particular team, identify outliers based on market value, rank players by goals per game and display different plots. The package is built in a way that allows user to easily customize the functions to their own interests, giving them the flexibility to analyze the data in a way that is most meaningful to them. Whether you're a coach, a sports journalist or an analyst, socceranalysis will help you unlock the insights hidden in your soccer data and make more informed decisions.

## Functions


1. `find_team_stat`: provides a quick and easy way to understand the descriptive statistics of a team. (https://github.com/UBC-MDS/socceranalysis_python/blob/main/src/socceranalysis/find_team_stat.py) 

2. `rankingplayers`:  Ranks players based on specific attributes (https://github.com/UBC-MDS/socceranalysis_python/blob/main/src/socceranalysis/playerranking.py)

3. `get_outliers`: Identifes outliers using statistical methods (interquartile range or standard deviations) (https://github.com/UBC-MDS/socceranalysis_python/blob/main/src/socceranalysis/outlier_identification.py)

4. `soc_viz_stats` :  Generates meaningful visualizations to help users understand and interpret the data (https://github.com/UBC-MDS/socceranalysis_python/blob/main/src/socceranalysis/viz_stats.py)
* `soc_viz_stats_scatter` : Generate a scatter plot for two given numeric columns with a slider to control age 
* `soc_viz_stats_hist` :  Generate a histogram for one given numeric columns



## Python ecosystem
socceranalysis can be used in conjunction with other popular Python packages such as [pandas](https://github.com/pandas-dev/pandas) and [scikit-learn](https://github.com/scikit-learn/scikit-learn) to perform more advanced data analysis and machine learning tasks. For example, users can use pandas to manipulate and clean their soccer data, and then use this package to perform specific soccer-related analysis on the cleaned data. Additionally, socceranalysis can be used in conjunction with scikit-learn for machine learning tasks on soccer data. They are designed to be a higher-level, more user-friendly and declarative interface based on [Altair](https://github.com/altair-viz/altair) for performing specific soccer-related analysis and visualization tasks. Users can perform similar visualization using [matplotlib](https://github.com/matplotlib/matplotlib). Overall, socceranalysis is a valuable addition to the Python ecosystem as it provides a specialized tool for analyzing and understanding soccer data without the need for writing complex code, this can be especially useful for users who may not have extensive experience with data analysis or visualization.



## Installation

```bash
$ pip install socceranalysis

# directly from test pypi
$ pip install -i https://test.pypi.org/simple/ socceranalysis
```

## Usage


###  find_team_stat
```bash
from socceranalysis.find_team_stat import *
data = pd.read_excel('soccer_data.xlsx')
find_team_stat(data , "Manchester United", "Market_Value_Euros")
```
### get_outliers
```bash 
data = pd.read_excel('soccer_data.xlsx')
from  socceranalysis.outlier_identification import get_outliers
get_outliers(data,"Wages_Euros","SD",3)
```
###  soc_viz_stats

```bash
from socceranalysis.viz_stats import *

# scatter plots of two given columns
soc_viz_stats_scatter('age','Goals_total', data)
# histogram of one given column
soc_viz_stats_hist('age', data)
```
### playerranking
```bash
from socceranalysis.rankingplayers import *
data = pd.read_excel('soccer_data.xlsx')
rankingplayers(data, "Goals_total", "Assists_Total")
```

## Contributors

|  	 Core contributor| Github.com username| 
|---------|---|
|  Flora Ouedraogo |  @florawendy19 | 
|  Gaoxiang Wang |  @louiewang820 | 
|  Manvir Kohli | @manvirsingh96 |
| Vincent Ho | @vincentho32 |

## Contributing

Authors: Vincent Ho, Manvir Singh Kohli, Gaoxiang Wang, Flora Ouedraogo.

Interested in contributing? Check out the contributing guidelines. Please note that this project is released with a Code of Conduct. By contributing to this project, you agree to abide by its terms.

## License

`socceranalysis` was created by Gaoxiang Wang, Manvir Kohli, Vincent Ho and Flora Ouedraogo. It is licensed under the terms of the MIT license.

## Credits

`socceranalysis` was created with [`cookiecutter`](https://cookiecutter.readthedocs.io/en/latest/) and the `py-pkgs-cookiecutter` [template](https://github.com/py-pkgs/py-pkgs-cookiecutter).
