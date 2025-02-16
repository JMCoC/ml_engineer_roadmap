import pandas as pd

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

#Merging DataFrames (pd.merge())
"""
Merge DataFrame objects by performing a database-style join operation by columns or indexes.
1. left: DataFrame or named Series. Object to merge with.
2. right: DataFrame or named Series. Object to merge with.
3. how: {'left', 'right', 'outer', 'inner'}, default 'inner'. Type of merge to be performed.
4. on: label or list. Column or index level names to join on. These must be found in both DataFrames.
5. left_on: label or list, or array-like. Column or index level names to join on in the left DataFrame.
6. right_on: label or list, or array-like. Column or index level names to join on in the right DataFrame.
7. left_index: bool, default False. Use the index from the left DataFrame as the join key(s).
8. right_index: bool, default False. Use the index from the right DataFrame as the join key.
9. sort: bool, default False. Sort the join keys lexicographically in the result DataFrame.
10. suffixes: tuple of (str, str), default ('_x', '_y'). Suffix to apply to overlapping column names in the left and right side, respectively.
11. copy: bool, default True. If False, avoid copying data into resulting data structure in some exceptional cases.
12. indicator: bool or str, default False. If True, adds a column to output DataFrame called '_merge' with information on the source of each row.
13. validate: str, default None. If specified, checks if merge is of specified type. (One of 'one_to_one', 'one_to_many', 'many_to_one', 'many_to_many')
"""

df1 = pd.DataFrame({'lkey': ['foo', 'bar', 'baz', 'foo'],
                    'value': [1, 2, 3, 5]})

df2 = pd.DataFrame({'rkey': ['foo', 'bar', 'baz', 'foo'],
                    'value': [5, 6, 7, 8]})

print(df1.merge(df2, left_on='lkey', right_on='rkey', suffixes=('_left', '_right'))) #Merging two DataFrames

df1 = pd.DataFrame({'key': ['foo', 'bar', 'baz', 'foo'],
                    'value': [1, 2, 3, 5]})

df2 = pd.DataFrame({'key': ['foo', 'bar', 'baz', 'foo'],
                    'value': [5, 6, 7, 8]})
print(df1.merge(df2, on='key')) #Merging two DataFrames on a common column

df1 = pd.DataFrame({'key': ['foo', 'bar', 'baz', 'foo'],
                    'key2': ['bar', 'foo', 'baz', 'foo'],
                    'value': [1, 2, 3, 5]})

df2 = pd.DataFrame({'key': ['foo', 'bar', 'baz', 'foo'],
                    'key2': ['foo', 'bar', 'baz', 'foo'],
                    'value': [5, 6, 7, 8]})
print(df1.merge(df2, on=['key', 'key2'])) #Merging two DataFrames on multiple columns

print(df1.merge(df2, on=['key', 'key2'], how='left')) 
print(df1.merge(df2, on=['key', 'key2'], how='right'))
print(df1.merge(df2, on=['key', 'key2'], how='outer')) 
print(df1.merge(df2, on=['key', 'key2'], how='inner'))

#Joining DataFrames (pd.DataFrame.join())
"""
Join columns with other DataFrame either on index or on a key column.
1. other: DataFrame, Series, or list of DataFrame. Index should be similar to one of the columns in this one.
2. on: str, list of str, or array-like, default None. Column or index level name(s) in the caller to join on the index in other, otherwise joins index-on-index.
3. how: {'left', 'right', 'outer', 'inner'}, default 'left'. How to handle the operation of the two objects.
4. lsuffix: str, default ''. Suffix to use from left DataFrame's overlapping columns.
5. rsuffix: str, default ''. Suffix to use from right DataFrame's overlapping columns.
6. sort: bool, default False. Order result DataFrame lexicographically by the join key.
7. validate: str, default None. If specified, checks if merge is of specified type. (One of 'one_to_one', 'one_to_many', 'many_to_one', 'many_to_many')
"""

df = pd.DataFrame({'key': ['k0', 'k1', 'k2', 'k3'],
                   'A': ['A0', 'A1', 'A2', 'A3'],
                   'B': ['B0', 'B1', 'B2', 'B3']})

df2 = pd.DataFrame({'key': ['k0', 'k1', 'k2'],
                    'C': ['C0', 'C1', 'C2'],
                    'D': ['D0', 'D1', 'D2']})

print(df.join(df2, lsuffix='_caller', rsuffix='_other')) #Joining two DataFrames using index
print(df.set_index('key').join(df2.set_index('key'), lsuffix='_caller', rsuffix='_other')) #Joining two DataFrames using a common column
print(df.join(df2.set_index('key'), on='key', lsuffix='_caller', rsuffix='_other')) #Joining two DataFrames using a common column
print(df.join(df2.set_index('key'), how='inner', on='key')) 

"""
Difference between merge() and join() and concat():
1. merge() combine data on common columns or indices.
2. join() combines data on a key column or an index.
3. concat() combines data along a particular axis.
"""