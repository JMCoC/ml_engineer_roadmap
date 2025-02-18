import pandas as pd

"""
df.drop_duplicates()
Return a dataframe with duplicates removed
1. subset: column label or sequence of labels to consider for identifying duplicates
2. keep: {'first', 'last', False}, default 'first'
    - first: Drop duplicates except for the first occurrence.
    - last: Drop duplicates except for the last occurrence.
    - False: Drop all duplicates.
3. inplace: bool, default False (Modify the DataFrame in place instead of creating a new DataFrame)
4. ignore_index: bool, default False
"""

df = pd.DataFrame({
    'brand': ['Yum Yum', 'Yum Yum', 'Indomie', 'Indomie', 'Indomie'],
    'style': ['cup', 'cup', 'cup', 'pack', 'pack'],
    'rating': [4, 4, 3.5, 15, 5]
})

print(df)
print(df.drop_duplicates()) #Drop if all columns are same
print(df.drop_duplicates(subset=['brand'])) 
print(df.drop_duplicates(subset=['brand', 'style'], keep='last'))
result = df.drop_duplicates(subset=['brand', 'style'], keep=False)
print(result)
df.drop_duplicates(subset=['brand', 'style'], keep=False, inplace=True)
print(df)