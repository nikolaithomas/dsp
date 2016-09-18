import numpy as np
import pandas as pd
from pandas import Series,DataFrame
import csv
url = 'https://raw.githubusercontent.com/nikolaithomas/dsp/master/python/faculty.csv'
df = pd.read_csv(url, index_col=None)
df.columns = [x.strip().replace(' ', '_') for x in df.columns]


t = df['email'].tolist()
t
thecsv = csv.writer(open("emails.csv", 'wb'))
for row in t:
    thecsv.writerow([element])
