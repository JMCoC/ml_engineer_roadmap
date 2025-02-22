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

#Iterating through groups

for name, group in df.groupby('Name'): 
    print(name) 
    print(group) 
    print()

#Select a group (get_group)

grp = df.groupby('Name')
print(grp.get_group('Jai'))

grp2 = df.groupby(['Name', 'Qualification'])
print(grp2.get_group(('Jai', 'MCA')))

print(df.groupby('Name').get_group('Jai'))

#Applying function to group

#Aggregation
"""
Aggregation is a process in which we compute a summary statistic
about each group. For example, we might want to compute the average
age for each name. (.agg() or .aggregate() they are same)
1. func: function, str, list or dict
2. axis: int, default 0 (0 or 'index' for row-wise, 1 or 'columns' for column-wise)
3. *args: positional arguments passed to func
4. **kwargs: keyword arguments passed to func
Returns: scalar, Series or DataFrame
"""

group1 = df.groupby('Name')
print(group1['Age'].agg('sum'))

group2 = df.groupby(['Name', 'Qualification'])
print(group2['Age'].agg('mean'))

#multiple functions

print(group1['Age'].agg(['sum', 'mean', 'std']))

#Transformation
"""
Transformation is a process in which we perform some group-specific
computation and return a like-indexed object.
1. func: function, str, list or dict
2. axis: int, default 0 (0 or 'index' for row-wise, 1 or 'columns' for column-wise)
3. *args: positional arguments passed to func
4. **kwargs: keyword arguments passed to func
Returns: DataFrame that must have the same length as input
"""

group1 = df.groupby('Name')
print(group1['Age'].transform(lambda x: x - x.mean()))

sc = lambda x: (x - x.mean()) / x.std()
print(group1['Age'].transform(sc))

print(group1['Name'].transform(lambda x: x.str.upper()))

#Filteration
"""
Filtration allows you to drop entire groups based on a condition.
1. func: function, str, list or dict
2. dropna: bool, default True
"""

df = pd.read_csv('pythonBasics/CSV/nba.csv')

filter1 = df.groupby('Team').filter(lambda x: x['Salary'].mean() >= 7000000)
print(filter1)