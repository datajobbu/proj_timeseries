import pandas as pd

df = pd.read_csv("tsdata.csv")


#print(df.head())
print(df.isnull().sum().sum())

#print(df.iloc[:,[0,25730]])
#ck = df.columns.unique()
#print(len)