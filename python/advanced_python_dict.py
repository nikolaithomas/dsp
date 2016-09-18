import numpy as np
import numpy as np
import pandas as pd
from pandas import Series,DataFrame


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
del df2['name']
df2
#df2.set_index('lastname').T.to_dict('list')
mydict = {}
for x in range(len(df2)):
    lastname = df2.iloc[x,3]
    title = df2.iloc[x,1]
    email = df2.iloc[x,2]
    degree = df2.iloc[x,0]
    mydict.setdefault(lastname, [])
    mydict[lastname].append(degree)
    mydict[lastname].append(title)
    mydict[lastname].append(email)  
mydict

dict(mydict.items()[0:3])
