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

#Merging, joining and concatenating DataFrames

#Concatenating DataFrames (pd.concat())
"""
Concatenate pandas objects along a particular axis with optional set logic along the other axes.
1. objs: a sequence or mapping of Series or DataFrame objects.
2. axis: {0/'index', 1/'columns'}, default 0. The axis to concatenate along.
3. join: {'inner', 'outer'}, default 'outer'. How to handle indexes on other axis(es).
4. ignore_index: bool, default False. If True, do not use the index values along the concatenation axis.
5. keys: sequence, default None. Construct hierarchical index using the passed keys as the outermost level.
6. levels: list of sequences, default None. Specific levels (unique values) to use for constructing a MultiIndex.
7. names: list, default None. Names for the levels in the resulting hierarchical index.
8. verify_integrity: bool, default False. Check whether the new concatenated axis contains duplicates. This can be very expensive relative to the actual data concatenation.
9. sort: bool, default False. Sort non-concatenation axis if it is not already aligned when join is 'outer'.
10. copy: bool, default True. If False, do not copy data unnecessarily.
"""

s1 = pd.Series([1, 2])
s2 = pd.Series([3, 4])
df1 = pd.concat([s1, s2])
print(df1) #index 0,1,0,1

df1 = pd.concat([s1, s2], ignore_index=True)
print(df1) #index 0,1,2,3

df1 = pd.concat([s1, s2], keys=['s1', 's2'])
print(df1) #MultiIndex

df1 = pd.concat([s1, s2], keys=['s1', 's2'], names=['Series name', 'Row ID'])
print(df1) #MultiIndex with names

df1 = pd.concat([s1, s2], axis=1)
print(df1) #columns 0,1

#Combining DataFrames

df1 = pd.DataFrame({'A': ['A0', 'A1', 'A2', 'A3'],
                    'B': ['B0', 'B1', 'B2', 'B3'],
                    'C': ['C0', 'C1', 'C2', 'C3'],
                    'D': ['D0', 'D1', 'D2', 'D3']},
                    index=[0, 1, 2, 3])

df2 = pd.DataFrame({'A': ['A4', 'A5', 'A6', 'A7'],
                    'B': ['B4', 'B5', 'B6', 'B7'],
                    'C': ['C4', 'C5', 'C6', 'C7'],
                    'D': ['D4', 'D5', 'D6', 'D7']},
                    index=[5, 6, 7, 8])

print(pd.concat([df1, df2], ignore_index=True)) #Concatenating two DataFrames
print(pd.concat([df1, df2], axis=1)) #Concatenating two DataFrames along columns
#(Columns outside the intersection will be filled with NaN values)
print(pd.concat([df1, df2], verify_integrity=True)) #Verify integrity, raises ValueError if duplicates are found
#Eg if index is not unique (df1 = 0,1,2,3, df2 = 0,1,2,3)

df1 = pd.DataFrame({'A': ['A0', 'A1', 'A2', 'A3'],
                    'B': ['B0', 'B1', 'B2', 'B3'],
                    'C': ['C0', 'C1', 'C2', 'C3'],
                    'D': ['D0', 'D1', 'D2', 'D3']},
                    index=[0, 1, 2, 3])

df2 = pd.DataFrame({'A': ['A4', 'A5', 'A6', 'A7'],
                    'B': ['B4', 'B5', 'B6', 'B7'],
                    'C': ['C4', 'C5', 'C6', 'C7'],
                    'D': ['D4', 'D5', 'D6', 'D7']},
                    index=[2, 3, 4, 5])

print(pd.concat([df1, df2], axis=1, join='inner')) #Inner join, only common rows will be included