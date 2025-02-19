import pandas as pd

"""
In pandas we use astype() method to change the data type of a column.
"""

data = {
    'Name': ['John', 'Anna', 'Peter', 'Linda'],
    'Age': [25, 30, 35, 40],
    'City': ['New York', 'Paris', 'Berlin', 'London'],
    'Salary': [50000, 60000, 70000, 80000]}

df = pd.DataFrame(data)

print(df.dtypes)
df['Salary'] = df['Salary'].astype(float)
print(df.dtypes)

#Datetime type

df['Date'] = ['2021-01-01', '2021-02-01', '2021-03-01', '2021-04-01']
print(df.dtypes)
df['Date'] = pd.to_datetime(df['Date'])
print(df.dtypes)

#Mixed data type
"""
Is when a column has different data types.
Caused by missing values or data entry errors or inconsistent formatting.
Use info() it's not enough to detect mixed data types.
You have to iterate over the column and check the data type of each element with pd.api.types.infer_dtype() method.
"""

df = pd.DataFrame({'Name': ['John', 'Anna', 'Peter', 'Linda', 'Sam'],
                   'Age': [25, 30, 35.3, 40, '45'],
                   'City': ['New York', 'Paris', 'Berlin', 'London', 'Madrid'],
                   'Salary': [50000, 60000, 70000, 80000, 90000]})

for column in df.columns:
    print(column, pd.api.types.infer_dtype(df[column]))

#We can use astype() method to convert the column to the correct data type.

df['Age'] = df['Age'].astype(int)
print(df.dtypes)
print(df)
for column in df.columns:
    print(column, pd.api.types.infer_dtype(df[column]))
