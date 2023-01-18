# socceranalysis_python

socceranalysis_python is a powerful Python package designed to make it easy to analyze and understand soccer statistics. With its set of functions, you can quickly obtain summary statistics for a particular team, identify outliers based on market value, rank players by goals per game and display different plots. The package is built in a way that allows user to easily customize the functions to their own interests, giving them the flexibility to analyze the data in a way that is most meaningful to them. Whether you're a coach, a sports journalist or an analyst, socceranalysis_python will help you unlock the insights hidden in your soccer data and make more informed decisions.




## Function 1: find_team_stat [Summary statistics of a particular team](https://github.com/UBC-MDS/socceranalysis_python/blob/main/src/socceranalysis/find_team_stat.py) 
* This function can provide a quick and easy way to understand the descriptive statistics of a team.


## Function 2: rankingplayers [Ranking the players by goal per game](https://github.com/UBC-MDS/socceranalysis_python/blob/main/src/socceranalysis/playerranking.py)
* This function provides an easy way to compare the performance of players based on specific attributes.

## Function 3: get_outliers [Getting outliers based on the market value of a player](https://github.com/UBC-MDS/socceranalysis_python/blob/main/src/socceranalysis/outlier_identification.py)
*  This function allows users to identify players who are outliers i.e. players who stand out from the majority and cause the data to be skewed. It uses statistical methods (interquartile range or standard deviations) to determine which players are considered outliers. Any numeric feature can be used to identify outliers.

## Function 4: viz_stats [Visual descriptive statistics based on user selection](https://github.com/UBC-MDS/socceranalysis_python/blob/main/src/socceranalysis/viz_stats.py)
* This function is a useful tool for quickly generating meaningful visualizations that can help users understand and interpret the data.


Socceranalysis_python can be used in conjunction with other popular Python packages such as [pandas](https://github.com/pandas-dev/pandas) and [scikit-learn](https://github.com/scikit-learn/scikit-learn) to perform more advanced data analysis and machine learning tasks. For example, users can use pandas to manipulate and clean their soccer data, and then use this package to perform specific soccer-related analysis on the cleaned data. Additionally, socceranalysis_python can be used in conjunction with scikit-learn for machine learning tasks on soccer data. They are designed to be a higher-level, more user-friendly and declarative interface based on [Altair](https://github.com/altair-viz/altair) for performing specific soccer-related analysis and visualization tasks. Users can perform similar visualization using [matplotlib](https://github.com/matplotlib/matplotlib). Overall, socceranalysis is a valuable addition to the Python ecosystem as it provides a specialized tool for analyzing and understanding soccer data without the need for writing complex code, this can be especially useful for users who may not have extensive experience with data analysis or visualization.



## Installation

```bash
$ pip install socceranalysis_python
```

## Usage

```bash 
data = pd.read_excel('soccer_data.xlsx')
from  socceranalysis.outlier_identification import get_outliers
get_outlier(data,"Wages_Euros","SD",3)
```

## Contributing

Authors: Vincent Ho, Manvir Singh Kohli, Gaoxiang Wang, Flora Ouedraogo

Interested in contributing? Check out the contributing guidelines. Please note that this project is released with a Code of Conduct. By contributing to this project, you agree to abide by its terms.

## License

`socceranalysis_python` was created by Gaoxiang Wang, Manvir Kohli, Vincent Ho and Flora Wendy. It is licensed under the terms of the MIT license.

## Credits

`socceranalysis_python` was created with [`cookiecutter`](https://cookiecutter.readthedocs.io/en/latest/) and the `py-pkgs-cookiecutter` [template](https://github.com/py-pkgs/py-pkgs-cookiecutter).
