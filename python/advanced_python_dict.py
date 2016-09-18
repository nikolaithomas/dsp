import numpy as np
import pandas as pd
from pandas import Series,DataFrame
import itertools

url = 'https://raw.githubusercontent.com/nikolaithomas/dsp/master/python/faculty.csv'
df = pd.read_csv(url, index_col=None)
df.columns = [x.strip().replace(' ', '_') for x in df.columns]

def Cleandata_degree(df):
    df['name']= df['name'].str.replace('.','') 
    df['name']= df['name'].str.split(' ')
Cleandata_degree(df)
def new_list(list1, list2):
    for x in list1:
        list2.append(x[len(x)-1])
    
my_list = df['name'].tolist()
lastname = []
new_list(my_list, lastname)

df1 = DataFrame({'lastname': lastname})

df2 = df.join(df1)

df2
