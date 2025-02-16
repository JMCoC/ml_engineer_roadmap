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

#Pandas Dataframe index

"""
Index is used to access the rows of the DataFrame.
It can be numeric or string.
"""

data = {'Name':['Tom', 'Jack', 'Steve', 'Ricky'],
        'Age':[28,34,29,42],
        'Gender':['M','M','M','M'],
        'City':['NY','LA','SF','DC'],
        'Salary':[100,200,300,400]}

df = pd.DataFrame(data)
print(df.index)

#Setting custom index (set_index())
"""
Allow to set a custom index for the DataFrame based on a column.
"""
df = df.set_index('Name')
print(df)

#Resetting index (reset_index())

df = df.reset_index()
print(df)

#Indexing with .loc[] (label based indexing) (Selecting, slicing, filtering and changing values)

row = df.loc[0] #Single row
print(row)

rows = df.loc[[0,1,2]] #Multiple rows
print(rows)

subset = df.loc[0:2, ['Name', 'Age']] #Multiple columns and rows
print(subset)

condition = df.loc[df['Age'] > 30] #Condition based indexing
print(condition)

conditions = df.loc[(df['Age'] > 30) & (df['Salary'] >= 300)] #Multiple conditions
print(conditions)

df.loc[[0], ['Age']] = 60 #Changing value
print(df)

df.loc[0] = 100 #Changing entire row
print(df)

df.loc[df['Age'] > 30, 'Age'] = 40 #Changing value based on condition
print(df)

df.loc[:, 'Age'] = 50 #Changing entire column
print(df)

#Accessing a specific cell (at[])
"""
Access a single value for a row/column label pair.
"""

cell = df.at[0, 'Age']
print(cell)