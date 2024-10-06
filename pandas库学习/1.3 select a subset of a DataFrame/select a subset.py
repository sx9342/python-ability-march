# How do I select a subset of a DataFrame?
import pandas as pd
import requests

url = 'https://raw.githubusercontent.com/pandas-dev/pandas/main/doc/data/titanic.csv'
data = requests.get(url).text
with open("pandas库学习/1.3 select a subset of a DataFrame/titanic.csv", "w") as f:
    f.write(data)

titanic = pd.read_csv("pandas库学习/1.3 select a subset of a DataFrame/titanic.csv")
ages = titanic["Age"]
# print(ages.head()) # print the first 5 rows
# print(ages.shape) # print the shape of the DataFrame
# age_sex = titanic[["Age","Sex"]] # Select multiple columns by passing a list of column names. 
# The age_sex is a new DataFrame.
# print(age_sex.head()) # print the first 5 rows

# How do I specific rows from a DataFrame?

# above_35 = titanic[titanic["Age"] > 35] # select rows with age greater than 35

# class_23 = titanic[titanic["Pclass"].isin([2, 3])] # select rows with class 2 and 3
# print(class_23.head())
print(titanic.iloc[9:25,2:5])