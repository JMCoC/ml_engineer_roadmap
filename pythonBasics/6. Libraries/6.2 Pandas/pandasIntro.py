"""
Pandas is a library that provides data structures and data analysis tools 
for Python programming language. It is built on top of the NumPy package. 
Pandas is used for data manipulation, data analysis, and data visualization. 
It is widely used in data science, machine learning, and data analytics.

Pandas it's built on top of NumPy which means that a lot of the structure 
of NumPy is used or replicated in Pandas. Data in pandas is often used to
feed statistical analysis in SciPy, plotting functions from Matplotlib,
and machine learning algorithms in Scikit-learn.
"""

# Importing the pandas library
import pandas as pd
import numpy as np

#Pandas Series
"""
A Series is a one-dimensional array-like object containing an array of data
and an associated array of data labels called its index. The simplest Series
is formed from only an array of data.
"""

data = np.array([1, 2, 3, 4, 5])
s = pd.Series(data) #A column in a excel sheet
print(s)

#Creating Pandas Series (Column in Excel Sheet)
"""
In the real world, a Pandas Series will be created by loading the datasets
from existing storage, storage can be SQL Database, CSV file, and Excel file.

Pandas Series can be created from the lists, dictionary, and from a scalar value etc.
"""
#From array

data = np.array([1, 2, 3, 4, 5])
s = pd.Series(data)
print(s)

#From List

data = [1, 2, 3, 4, 5]
s = pd.Series(data)
print(s)

#From Dictionary

data = {'a': 0, 'b': 1, 'c': 2, 'd': 3, 'e': 4} #Keys will be the index
s = pd.Series(data)
print(s)

#From Scalar value

data = 5
s = pd.Series(data, index=[0, 1, 2, 3, 4])
print(s)

#Accessing Data from Series 
"""
You can access the elements of the Series in two ways. They are:
    1. Accessing Element from Series with Position
    2. Accessing Element Using Label (index)
"""

#Accessing Element from Series with Position
"""
In order to access the data from the Series, you can use the indexing operator [].
And to access to multiple elements, use slicing operator [:].
"""

data = [1, 2, 3, 4, 5]
s = pd.Series(data)
print(s[0]) #1
print(s[1:4]) #2, 3, 4

#CSV File
df = pd.read_csv("pythonBasics/CSV/nba.csv")
ser = pd.Series(df['Name'])
print(ser.head(5))

#Accessing Element Using Label (index)

data = np.array([1, 2, 3, 4, 5])
s = pd.Series(data, index=[100, 101, 102, 103, 104])
print(s[100]) #1
print(s[104]) #5
print(s[[100, 102, 104]]) #1, 3, 5

#CSV File
df = pd.read_csv("pythonBasics/CSV/nba.csv")
ser = pd.Series(df['Name'])
print(ser[[0, 50, 100]])

#Indexing and Selecting Data in Series (iloc, loc)
#iloc: iloc is an integer-location based indexing for selection by position.
#loc: loc is label-based indexing function.

df = pd.read_csv("pythonBasics/CSV/nba.csv")
ser = pd.Series(df['Name'])
data = ser.head(10)
print(data.loc[3:6])
print(data.iloc[3:6])

#Binary Operation on Series (Addition, Subtraction, Multiplication, and Division, etc.)

data1 = pd.Series([1, 2, 3, 4, 5], index=['a', 'b', 'c', 'd', 'e'])
data2 = pd.Series([10, 20, 30, 40, 50], index=['a', 'b', 'c', 'd', 'e'])
print(data1.add(data2, fill_value=0))
print(data1.sub(data2, fill_value=0))

#Converison Operation on Series (to_numpy(), to_list(), to_dict(), astype(), etc.)

data = pd.read_csv("pythonBasics/CSV/nba.csv")
data.dropna(inplace=True) #Drop all the columns with NaN values
before = data.dtypes #Before conversion
data['Salary'] = data['Salary'].astype(int)
data['Number'] = data['Number'].astype(str)
after = data.dtypes #After conversion

print(before)
print(after)

#to_list()

data = pd.read_csv("pythonBasics/CSV/nba.csv")
data.dropna(inplace=True)
dtypeBefore = type(data['Salary'])
salaryList = data['Salary'].to_list()
dtypeAfter = type(salaryList)

print(dtypeBefore)
print(dtypeAfter)

print(data.info())