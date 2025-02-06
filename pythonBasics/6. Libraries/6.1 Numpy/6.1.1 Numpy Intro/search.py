#You can search an array for a certain value, and return the indexes 
# that get a match.
# To search an array, use the where() method.

import numpy as np

arr = np.array([1, 2, 3, 4, 5, 4, 4])

x = np.where(arr == 4)

print(x) #it's returns a tuple with array indexes

#2D array

arr = np.array([[1, 2, 4], [4, 5, 6]])

x = np.where(arr == 4)

print(x) #The first array represents in which row the value is present, and the second array represents in which column the value is present.

#You can use any condition to search in the array, and return the indexes that get a match.

arr = np.array([1, 2, 3, 4, 5, 6, 7, 8])

x = np.where(arr%2 == 0)
y = np.where(arr%2 == 1)

print(x)
print(y)

#Search Sorted
#Perform a binary search in the sorted array to find the index where the value is inserted.

arr = np.array([6, 7, 8, 9])

x = np.searchsorted(arr, 10)

print(x) #returns the index where the value 7 should be inserted, starting from the left.
#You can also search from the right, by specifying side='right'.

x = np.searchsorted(arr, 7, side='right')

print(x) #returns the index where the value 7 should be inserted, starting from the right.

#Multiple Values

arr = np.array([1, 3, 5, 7])

x = np.searchsorted(arr, [2, 4, 6])

print(x) #return an array with indexes where the values 2, 4, and 6 should be inserted.