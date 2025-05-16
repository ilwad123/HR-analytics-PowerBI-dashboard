import pandas as pd 
import os 
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import re
import datetime

#read csv file
df= pd.read_csv('HR_Analytics.csv')
# replace the missing values in the YearsWithCurrManager column with unfilled values with -1 =unknown
df['YearsWithCurrManager'].fillna(-1, inplace=True)

#check for duplictes in the employee id column
duplicates = df.duplicated(subset=['EmpID'])
print("number of duplicates in df:", duplicates.sum())
#drop employee count column as it is not useful for analysis as it is constant value
if df['EmployeeCount'].nunique() == 1:
    df.drop(columns=['EmployeeCount'], inplace=True)

df.drop(columns=['Over18'], inplace=True)

# df.drop_duplicates(subset=['EmpID'], keep='first', inplace=True)

#get the number of duplicates in empID as they are not all unique 
dupes = df[df.duplicated(subset='EmpID', keep=False)]
dupes.to_csv("potential_conflicts.csv", index=False)

#drop duplicate rows as there are duplicates because of empID is not all unique 
#keep the first occurrence of each duplicate
df.drop_duplicates(subset='EmpID', keep='first', inplace=True)
df.to_csv("cleaned_data.csv", index=False)


