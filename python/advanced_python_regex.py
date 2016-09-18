

#Q1. Find how many different degrees there are, and their frequencies: Ex: PhD, ScD, MD, MPH, BSEd, MS, JD, etc.
import numpy as np
import pandas as pd
from pandas import Series,DataFrame

url = 'https://raw.githubusercontent.com/nikolaithomas/dsp/master/python/faculty.csv'
df = pd.read_csv(url, index_col=None)
df.columns = [x.strip().replace(' ', '_') for x in df.columns]

def Cleandata_degree(df):
    na_vals = "0"
    na_vals2 = ''
    df.degree.replace(na_vals, np.nan, inplace=True)
    df.degree.replace(na_vals2, np.nan, inplace=True)
    df['degree']= df['degree'].str.replace('.','') 
    df.drop_duplicates(['degree'], keep='last')
  
    
Cleandata_degree(df)

s = df['degree'].str.split(' ').apply(Series, 1).stack()  
s.index = s.index.droplevel(-1)
s.name = 'degree'
del df['degree']
df2 = df.join(s)

Cleandata_degree(df2)
df3 = df2.dropna()
array1 = df3.degree.unique()
len(array1)

PART II
import numpy as np
import pandas as pd
from pandas import Series,DataFrame

url = 'https://raw.githubusercontent.com/nikolaithomas/dsp/master/python/faculty.csv'
df = pd.read_csv(url, index_col=None)
df.columns = [x.strip().replace(' ', '_') for x in df.columns]

def Cleandata_degree(df):
    na_vals = "0"
    na_vals2 = ''
    df.degree.replace(na_vals, np.nan, inplace=True)
    df.degree.replace(na_vals2, np.nan, inplace=True)
    df['degree']= df['degree'].str.replace('.','') 
    df.drop_duplicates(['degree'], keep='last')
  
    
Cleandata_degree(df)

s = df['degree'].str.split(' ').apply(Series, 1).stack()  
s.index = s.index.droplevel(-1)
s.name = 'degree'
del df['degree']
df2 = df.join(s)

Cleandata_degree(df2)
df3 = df2.dropna()
df3['degree'].value_counts()

#Q2. Find how many different titles there are, and their frequencies: Ex: Assistant Professor, Professor

import numpy as np
import pandas as pd
from pandas import Series,DataFrame

url = 'https://raw.githubusercontent.com/nikolaithomas/dsp/master/python/faculty.csv'
df = pd.read_csv(url, index_col=None)
df.columns = [x.strip().replace(' ', '_') for x in df.columns]

def Cleandata_degree(df):
    na_vals = "0"
    na_vals2 = ''
    df.degree.replace(na_vals, np.nan, inplace=True)
    df.degree.replace(na_vals2, np.nan, inplace=True)
    df.set_value(24, 'title', 'Assistant Professor of Biostatistics')
    df['degree']= df['degree'].str.replace('.','') 
    df.drop_duplicates(['degree'], keep='last')
  
    
Cleandata_degree(df)
array1 = df.title.unique()
len(array1)

Part II
import numpy as np
import pandas as pd
from pandas import Series,DataFrame

url = 'https://raw.githubusercontent.com/nikolaithomas/dsp/master/python/faculty.csv'
df = pd.read_csv(url, index_col=None)
df.columns = [x.strip().replace(' ', '_') for x in df.columns]

def Cleandata_degree(df):
    na_vals = "0"
    na_vals2 = ''
    df.degree.replace(na_vals, np.nan, inplace=True)
    df.degree.replace(na_vals2, np.nan, inplace=True)
    df.set_value(24, 'title', 'Assistant Professor of Biostatistics')
    df['degree']= df['degree'].str.replace('.','') 
    df.drop_duplicates(['degree'], keep='last')
  
    
Cleandata_degree(df)
array1 = df.title.unique()
df['title'].value_counts()


#Q3. Search for email addresses and put them in a list. Print the list of email addresses.

import numpy as np
import pandas as pd
from pandas import Series,DataFrame

url = 'https://raw.githubusercontent.com/nikolaithomas/dsp/master/python/faculty.csv'
df = pd.read_csv(url, index_col=None)
df.columns = [x.strip().replace(' ', '_') for x in df.columns]

my_list = df['email'].tolist()
my_list



#Q4. Find how many different email domains there are (Ex: mail.med.upenn.edu, upenn.edu, email.chop.edu, etc.). Print the list of unique email domains.

