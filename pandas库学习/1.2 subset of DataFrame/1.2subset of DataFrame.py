# How do I read and write tabular data?
import pandas as pd
import requests

url = 'https://raw.githubusercontent.com/pandas-dev/pandas/main/doc/data/titanic.csv'
data = requests.get(url).text
with open("pandas库学习/1.2 subset of DataFrame/titanic.csv", "w") as f:
    f.write(data)

titanic = pd.read_csv("pandas库学习/subset of DataFrame/titanic.csv")
# print(titanic.head(8)) # the first N rows of the DataFrame
# print(titanic.tail(8)) # the last N rows of the DataFrame
# print(titanic.dtypes)  # data types for each column
# print(titanic.info()) # summary of the DataFrame
titanic.to_excel("pandas库学习/subset of DataFrame/titanic.xlsx", sheet_name="passengers",index=False) # save DataFrame to an Excel file. Remember to install the openpyxl package
