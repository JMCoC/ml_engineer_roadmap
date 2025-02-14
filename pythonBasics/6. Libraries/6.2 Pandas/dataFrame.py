"""
Pandas Data Frame is a 2D data structure with columns of potentially different types.
It is similar to a spreadsheet or SQL table, or a dictionary of Series objects.
It is generally the most commonly used pandas object.
"""

import pandas as pd

# Creating a DataFrame
"""
A pandas DataFrame can be created in multiple ways.
"""

#Empty DataFrame

df = pd.DataFrame()
print(df)

#Creating a DataFrame from lists

data = [1,2,3,4,5]
df = pd.DataFrame(data)
print(df)

data = [['Alex',10],['Bob',12],['Clarke',13]]
df = pd.DataFrame(data,columns=['Name','Age'])
print(df)

#Creating a DataFrame from Dict of ndarrays / Lists

data = {'Name':['Tom', 'Jack', 'Steve', 'Ricky'],'Age':[28,34,29,42]} #Must have same length
df = pd.DataFrame(data)
print(df)

#Creating a DataFrame from List of Dicts

data = [{'a': 1, 'b': 2, 'c': 3},{'a': 5, 'b': 10, 'c': 20}]
df = pd.DataFrame(data)
print(df)

#Creating a DataFrame from Dict of Series

d = {'one' : pd.Series([1, 2, 3], index=['a', 'b', 'c']),
    'two' : pd.Series([1, 2, 3], index=['a', 'b', 'c'])}
df = pd.DataFrame(d)
print(df)

#Zipping two lists and creating a DataFrame

name = ['Tom', 'Jack', 'Steve', 'Ricky']
age = [28,34,29,42]
list_of_tuples = list(zip(name, age))
df = pd.DataFrame(list_of_tuples, columns = ['Name', 'Age'])
print(df)

#Dealing with Rows and Columns
"""
We can perform various operations on rows and columns of a DataFrame.
Like selecting, adding, deleting, renaming etc.
"""

#Selecting a Column

data = pd.read_csv('pythonBasics/CSV/nba.csv')
print(data['Name'])

#Selecting multiple columns

print(data[['Name', 'Team']])

#Selecting a Row
#loc[] is used to select rows by their labels

print(data.loc[0])

#Selecting multiple rows

print(data.loc[0:4])

#Adding a new column

data['Sport'] = 'Basketball'
print(data)

#Deleting a column

data = data.drop('Sport', axis = 1)
print(data)

#Renaming a column

data = data.rename(columns = {'Name': 'Player Name'})
print(data)