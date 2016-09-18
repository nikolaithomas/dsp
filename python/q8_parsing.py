# The football.csv file contains the results from the English Premier League. 
# The columns labeled ‘Goals’ and ‘Goals Allowed’ contain the total number of 
# goals scored for and against each team in that season (so Arsenal scored 79 goals 
# against opponents, and had 36 goals scored against them). Write a program to read the file, 
# then print the name of the team with the smallest difference in ‘for’ and ‘against’ goals.

import numpy as np
import pandas as pd
from pandas import Series,DataFrame

url = 'https://raw.githubusercontent.com/nikolaithomas/dsp/master/python/football.csv'
df = pd.read_csv(url, index_col=None)
df['Goal Difference'] = abs(df['Goals'] - df['Goals Allowed'])
dfanswer = df['Goal Difference'].min()
df_row = df.loc[df['Goal Difference'] == dfanswer]
df_row
