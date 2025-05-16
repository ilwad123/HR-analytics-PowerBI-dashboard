#read csv file
import pandas as pd
import os
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


df= pd.read_csv('HR_Analytics.csv')

# # Display the shape of the DataFrame
# print(df.shape)
# # Display the column names
# print("column names : ", df.columns)
# # Display the data types of each column
# print(df.dtypes)
# Display the summary statistics of the DataFrame
print("summary statistics : ")
print(df.describe())
# Display the number of missing values in each column
print("missing values : ")
print(df.isnull().sum())
# # Display the number of duplicates in the DataFrame
print("number of duplicates in df:", df.duplicated().sum())

print(f"Number of rows: {df.shape[0]}")

print("\nUnique values per column:")
print(df.nunique())

duplicates = df[df.duplicated(subset='EmpID', keep=False)]
print(duplicates.sort_values('EmpID'))

print("Number of completely duplicated rows:", df.duplicated().sum())
