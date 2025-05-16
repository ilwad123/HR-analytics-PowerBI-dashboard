import pandas as pd
import os 


df= pd.read_csv('cleaned_data.csv')
#check for number of duplicates in the dataframe

print("missing values : ")
print(df.isnull().sum())

print("number of duplicates in df:", df.duplicated().sum())
print(f"Number of rows: {df.shape[0]}")

print("Number of completely duplicated rows:", df.duplicated().sum())

duplicates = df[df.duplicated(subset='EmpID', keep=False)]
print(duplicates.sort_values('EmpID'))
#double check the data types of each column
print(df.dtypes)

