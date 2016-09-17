

#Q1. Find how many different degrees there are, and their frequencies: Ex: PhD, ScD, MD, MPH, BSEd, MS, JD, etc.


#Q2. Find how many different titles there are, and their frequencies: Ex: Assistant Professor, Professor
import numpy as np
import pandas as pd
from pandas import Series,DataFrame

data_prof = pd.read_clipboard()
data_prof
my_list = data_prof["email"].tolist()
my_list

#Q3. Search for email addresses and put them in a list. Print the list of email addresses.



#Q4. Find how many different email domains there are (Ex: mail.med.upenn.edu, upenn.edu, email.chop.edu, etc.). Print the list of unique email domains.

