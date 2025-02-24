import pandas as pd

"""
String manipulation is the process of changing, parsing, splicing, and converting strings.
It's useful when you have a column of strings that you want to clean up or modify for analysis.
"""

df = pd.read_csv('pythonBasics/CSV/nba.csv')

#We can use the methods that .str provides to perform string manipulation on a column.

print(df['Name'].str.lower().head(5))
print(df['Name'].str.upper().head(5))
print(df['Name'].str.title().head(5))
print(df['Name'].str.len().head(5))

"""
More methods:
Method	Description
1.	upper()	Converts a string into uppercase
2.	lower()	Converts a string into lowercase
3.	isupper()	Checks whether the character is uppercase or not
4.	islower()	Checks whether the character is lowercase or not
5.	len()	Identifies the length of the string.
6.	startswith() 	Returns true if the element starts with the pattern
7.	split()	Splits the string at a particular index or character
8.	find()	Returns the index at where the given string is found
9.	strip()	Strips whitespaces from each string from both sides.
10.	replace() 	Replaces a part of the string with another one.
"""