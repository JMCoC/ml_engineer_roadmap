import pandas as pd

"""
Pandas DataFrame can be sorted by the value of one or more columns.
Using the sort_values() method, we can sort a DataFrame by one or more columns.
1. by: A string or list of strings that represent the column(s) we want to sort by.
2. axis: 0 or 'index' for rows and 1 or 'columns' for columns. (Default is 0)
3. ascending: A boolean or list of boolean values that specifies whether to sort in ascending order.
4. inplace: A boolean value that specifies whether to perform the operation in place.
5. kind: A string that specifies the type of sorting algorithm. (QuickSort, MergeSort, HeapSort, TimSort)
6. na_position: A string that specifies where to put NaN values. (first, last)
7. ignore_index: A boolean value that specifies whether to ignore the index.
8. key: A function that transforms the values before sorting.
"""

# Sort the DataFrame by column value

df = pd.read_csv('pythonBasics/CSV/nba.csv')
print(df.sort_values(by='Salary', ascending=False))

# Sort the DataFrame by multiple columns

print(df.sort_values(by=['Team', 'Name']))

# Sort the DataFrame by multiple columns in different orders

print(df.sort_values(by=['Team', 'Salary'], ascending=[True, False]))

# Sort dataframe with missing values

print(df.sort_values(by='Salary', na_position='first'))

# Sort dataframe with custom function
x = df['Name']
print(df.sort_values(by='Name', key=lambda x: x.str.len()))