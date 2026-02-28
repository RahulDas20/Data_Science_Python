import pandas as pd

df = pd.read_csv("Iris.csv")

#Show the first 5 rows of the dataframe
print(df.head())

#Show the last 5 rows of the dataframe
print(df.tail())

#Show the dataset information
print(df.info())


#Show the statistical summary of the dataset
print(df.describe())


#Show column names
print(df.columns)

#Dataset shape
print(df.shape)


#How to select an entire column
print(df['SepalLengthCm'])

#how to select multiple columns
print(df[['SepalLengthCm', 'SepalWidthCm']])


#How to select rows with loc
print(df.loc[0]) #Select the first row
print(df.loc[0:4]) #Select the first 5 rows
print(df.loc[df['Species'] == 'Iris-setosa']) #Select rows where the species is Iris-setosa
print(df.loc[0:100,'Species']) #Select the species of the first row