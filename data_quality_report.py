#read csv file
import pandas as pd
import os
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


df= pd.read_csv('HR_Analytics.csv')

#double check the cleaned data csv file 
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

print("Summary statistics for Age:")
print(df['Age'].describe())
