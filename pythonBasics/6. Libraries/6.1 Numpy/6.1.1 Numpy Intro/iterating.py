#Iterating means going through elements one by one. 
# As we know, Numpy arrays are multidimensional, 
# so we can iterate using for loop in multiple ways.

import numpy as np

# 1-D array
arr = np.array([1, 2, 3, 4, 5])

#iterate over 1D array will print each element
for i in arr:
    print(i)

# 2-D array
arr = np.array([[1, 2, 3], [4, 5, 6]])

#iterate over 2D array will print each row
for i in arr:
    print(i)

#iterate over 2D array will print each element
for i in arr:
    for j in i:
        print(j)

# 3-D array
arr = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])

#iterate over 3D array will print each 2D array
for i in arr:
    print(i)

#iterate over 3D array will print each row
for i in arr:
    for j in i:
        print(j)

#iterate over 3D array will print each element
for i in arr:
    for j in i:
        for k in j:
            print(k)

# nditer() function
# The nditer() function is used to iterate through the array.
# It is a more efficient way to iterate through the array.

arr = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])

for i in np.nditer(arr):
    print(i)

#iterating with different data types
#We can use op_dtypes argument and pass it the expected datatype 
# to change the datatype of elements while iterating.

#Numpy does not change the data type of the element in-place (where the element is in array)
# so it needs some other space to perform this action, that extra space is called buffer,
# and in order to enable it in nditer() we pass flags=['buffered'].

arr = np.array([1, 2, 3, 4, 5])

for i in np.nditer(arr, flags=['buffered'], op_dtypes=['S']):
    print(i)

#Iterating with different step size
#We can use the slicing concept to iterate through the array.

arr = np.array([[1, 2, 3, 4], [5, 6, 7, 8]])

for i in np.nditer(arr[:, ::2]):
    print(i)

#Enumerated Iteration using ndenumerate()

#The ndenumerate() function is used to iterate through the array and
# it returns the index and value of the array.

arr = np.array([[1, 2, 3, 4], [5, 6, 7, 8]])

for index, value in np.ndenumerate(arr):
    print(index, value)