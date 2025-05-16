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
duplicate_employee_count = df.duplicated(subset=["EmployeeCount"])
#drop employee count column as it is not useful for analysis as it is constant value
if df['EmployeeCount'].nunique() == 1:
    df.drop(columns=['EmployeeCount'], inplace=True)
#drop duplicate rows as there are duplicates because of empID is not all unique 
#keep the first occurrence of each duplicate
# df.drop_duplicates(subset=['EmpID'], keep='first', inplace=True)



dupes = df[df.duplicated(subset='EmpID', keep=False)]
#drop fully duplicated rows
# dupes.drop_duplicates(subset='EmpID', keep='first', inplace=True)

dupes.to_csv("potential_conflicts.csv", index=False)
