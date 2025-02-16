import pandas as pd

"""
Pivot Table is a data summarization tool frequently used in spreadsheets 
and other data analysis programs.
1. Values: List-like or scalar values to aggregate according to the factors.
2. Index: A column, Grouper, array which the data is aggregated.
3. Columns: A column, Grouper, array, or list of the previous which the data is aggregated.
4. Aggfunc: function to use for aggregating the data. (default is numpy.mean)
5. Fill_value: A scalar value that is used to fill missing values in the result.
6. Margins: Add all row / columns (e.g. subtotals) in the result.
7. Dropna: Do not include columns whose entries are all NaN
8. margins_name: Name of the row / column that will contain the totals when margins is True.
9. sort: Sort row / column labels.
""" 

df = pd.read_csv('pythonBasics/CSV/nba.csv')
pivot = pd.pivot_table(df, index=['Team'], values=['Salary'], aggfunc='sum')
print(pivot)

pivot_count = pd.pivot_table(df, index=['Team'], values=['Name'], aggfunc='count')
print(pivot_count)

pivot = pd.pivot_table(df, index=['Team'], values=['Salary'], aggfunc={'mean', 'median'})
print(pivot)