import pandas as pd

"""
Groupby allows you to group together rows based off of a column and 
perform an aggregate function on them.
1. by: mapping, function, label, or list of labels
2. level: int, level name, or sequence of such, default None
3. as_index: bool, default True
4. sort: bool, default True
5. group_keys: bool, default True
6. dropna: bool, default True
"""

#Splitting data into groups 

import pandas as pd 
  
data1 = {'Name':['Jai', 'Anuj', 'Jai', 'Princi', 
                 'Gaurav', 'Anuj', 'Princi', 'Abhi'], 
        'Age':[27, 24, 22, 32, 
               33, 36, 27, 32], 
        'Address':['Nagpur', 'Kanpur', 'Allahabad', 'Kannuaj',
                   'Jaunpur', 'Kanpur', 'Allahabad', 'Aligarh'], 
        'Qualification':['Msc', 'MA', 'MCA', 'Phd',
                         'B.Tech', 'B.com', 'Msc', 'MA']} 
df = pd.DataFrame(data1)

# with one key
df.groupby('Name')
print(df.groupby('Name').groups)
df2 = df.groupby('Name')
print(df2.first())

# with multiple keys
df.groupby(['Name', 'Qualification'])
print(df.groupby(['Name', 'Qualification']).groups)
df2 = df.groupby(['Name', 'Qualification'])
print(df2.first())