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

#Conditional filtering using loc
print(df.loc[df['Species'] == 'Iris-setosa']) #Select rows where the species is Iris-setosa

#How to select specific information
print(df.loc[0:100,'Species']) #Select the species of the first row


#How to select rows with iloc
print(df.iloc[0]) #Select the first row
print(df.iloc[0:4]) #Select the first 5 rows
print(df.iloc[0:100, 5]) #Select the species of the first row



#Filtering data based on conditions
print(df[df['SepalLengthCm'] > 3.0])



#How to sort values 
print(df.sort_values(by='SepalLengthCm')) #Sort by SepalLengthCm in ascending order



#Value counts of a specific column
print(df['Species'].value_counts())
print(df['PetalWidthCm'].value_counts())

#Group by a specific column
print(df.groupby('Species').mean()) #Group by species and calculate the mean of each group
print(df.groupby('Species').max())


cor_data = df[['SepalLengthCm', 'SepalWidthCm', 'PetalLengthCm', 'PetalWidthCm']]
print(cor_data.corr("spearman"))

data = pd.read_csv("Titanic-Dataset.csv")
print(data.head())


#Check for missing values for titanic dataset
print(data.isnull())

#Count missing values for each column
print(data.isnull().sum())


#Create a new dataframe with no missing values
data_no_missing = data.dropna()
print(data_no_missing.isnull().sum())

#Create a new dataframe with the missing values filled with 0
data_filled = data.fillna(0)
print(data_filled.isnull().sum())

import pandas as pd

df = pd.read_csv("Iris.csv")

df.rename(columns={
    'SepalLengthCm': 'Sepal Length',
    'SepalWidthCm': 'Sepal Width',
    'PetalLengthCm': 'Petal Length',
    'PetalWidthCm': 'Petal Width'
})

print(df.head())


df.rename(columns={"SepalLengthCm": "Sepal Length",
                   "SepalWidthCm": "Sepal Width",
                     "PetalLengthCm": "Petal Length",
                        "PetalWidthCm": "Petal Width"}, inplace=True)
print(df.head())

#Add a new column to the dataframe
df["Sepal_Area"] = df["Sepal Length"] * df["Sepal Width"]

print(df.head())

print(df["Sepal_Area"].mean())


print(df["Sepal_Area"].sample(5))