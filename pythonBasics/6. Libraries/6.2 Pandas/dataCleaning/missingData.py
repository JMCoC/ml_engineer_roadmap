import pandas as pd
import numpy as np

"""
Missing values are represented in pandas as NaN (Not a Number).
"""

# Checking for missing values (isnull() and notnull() methods)

df = pd.read_csv('pythonBasics/CSV/nba.csv')

print(df.isnull()) # Returns a DataFrame of boolean values, True if the value is NaN, False otherwise
print(df.isnull().sum()) # Returns the number of missing values in each column

#Filtering data based on missing values

bool_series = pd.isnull(df['College']) 
print(df[bool_series]) # Returns the rows where College is NaN

"""
Same can be done using notnull() method but notnull() returns True if the value is not NaN, False otherwise.
"""

bool_series = pd.notnull(df['College'])
print(df[bool_series]) # Returns the rows where College is not NaN

#Filling missing values (fillna(), replace(), interpolate())
"""
1. fillna(): fillna() method is used to fill the missing values with a specified value.
2. replace(): replace() method is used to replace a value with another value.
3. interpolate(): interpolate() method is used to fill the missing values with a value in the same column.
"""

#fillna()
"""
1. value: scalar, dict, Series, or DataFrame
2. method: bfill, ffill
3. axis: 0 or 1
4. inplace: if True, fills the missing values in the original DataFrame (this modifies the original DataFrame)
5. limit: maximum number of consecutive NaN values to fill
"""

df = pd.read_csv('pythonBasics/CSV/nba.csv')

print(df.fillna(0)) # Fills all the missing values with 0
print(df.fillna(method='ffill')) # Fills the missing values with the previous value in the same column
print(df.fillna(method='bfill')) # Fills the missing values with the next value in the same column
print(df.fillna({'Name': 'Unknown', 'College': 'No College', 'Salary': 0})) # Fills the missing values with a dictionary

#replace()
"""
1. to_replace: str, regex, list, dict, Series, int, float, or None
How to find the value to replace.
if numeric, str, or regex: value equal to to_replace will be replaced with value.
if list of str, regex, or numeric: if to_replace and value are of different lengths, the length of to_replace must be the same as the length of value.
if dict: value will be replaced by key value.
2. value: scalar, dict, list, str, regex, default None
3. inplace: if True, replaces the value in the original DataFrame (this modifies the original DataFrame)
4. regex: if True, interpret to_replace and value as regular expressions
"""

df = pd.DataFrame({'A': [0, 1, 2, 3, 4], 'B': [5, 6, 7, 8, 9]})
print(df.replace(0, 100)) # Replaces 0 with 100
print(df.replace([0, 1, 2], 100)) # Replaces 0, 1, 2 with 100
print(df.replace({0: 100, 1: 101, 2: 102})) # Replaces 0 with 100, 1 with 101, 2 with 102
print(df.replace([0, 1, 2], [100, 101, 102])) # Replaces 0 with 100, 1 with 101, 2 with 102

#interpolate()
"""
Fill NaN values using an interpolation method.
1. method: linear, time, index, values, nearest, zero, slinear, quadratic, cubic, barycentric, krogh, piecewise_polynomial, polynomial, spline, or pchip
2. axis: 0 or 1
3. limit: maximum number of consecutive NaN values to fill
4. inplace: if True, fills the missing values in the original DataFrame (this modifies the original DataFrame)
5. limit_direction: forward, backward, both
6. limit_area: inside, outside (Inside: fill only NaN values surrounded by valid values, Outside: fill only NaN values outside valid values)
"""

df = pd.DataFrame({'A': [1, 2, np.nan, 4, 5], 'B': [10, 20, 30, np.nan, 50]})
print(df.interpolate(method='linear')) # Fills the missing values using linear interpolation