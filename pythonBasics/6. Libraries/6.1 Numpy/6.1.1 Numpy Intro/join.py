#Joining means putting contents of two or more arrays in a single array.
# In SQL we join tables based on a key, whereas in NumPy we join arrays by axes.
# We pass a sequence of arrays that we want to join to the concatenate() function, along with the axis.
# If axis is not explicitly passed, it is taken as 0.
# axis means the dimension along which the arrays will be joined.

import numpy as np

arr1 = np.array([[1, 2], [3, 4]])
arr2 = np.array([[5, 6], [7, 8]])

# Joining two arrays along axis 0
print(np.concatenate((arr1, arr2)))

# Joining two arrays along axis 1
print(np.concatenate((arr1, arr2), axis=1))

#Using stack() function

arr1 = np.array([1, 2, 3])
arr2 = np.array([4, 5, 6])

print(np.stack((arr1, arr2), axis=0))
print(np.stack((arr1, arr2), axis=1))

#Using hstack() function
#hstack() function is used to stack arrays in sequence horizontally (column wise).

arr1 = np.array([1, 2, 3])
arr2 = np.array([4, 5, 6])

print(np.hstack((arr1, arr2)))

#Using vstack() function
#vstack() function is used to stack arrays in sequence vertically (row wise).

arr1 = np.array([1, 2, 3])
arr2 = np.array([4, 5, 6])

print(np.vstack((arr1, arr2)))

#Using dstack() function
#dstack() function is used to stack arrays in sequence depth wise (along third axis).

arr1 = np.array([1, 2, 3])
arr2 = np.array([4, 5, 6])

print(np.dstack((arr1, arr2)))