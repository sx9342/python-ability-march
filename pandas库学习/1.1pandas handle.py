# What kind of data does pandas handle?
import pandas as pd
df = pd.DataFrame({ # Create an example DataFrame in Titanic
    "Name":[
    "Braund, Mr. Owen Harris",
    "Allen, Mr. William Henry",
    "Bonnell, Miss. Elizabeth", 
    ],
    "Age":[22,35,58],
    "Sex":["male","male","female"],
})
# print(df)
# print("\n")
print(df["Age"]) # get the column Age

# I want to know the maximun Age
max_age = df["Age"].max()
print("The maximum age is {}".format(df["Age"].max()))

# some basic statistics
print(df.describe())