#Python does not have built-in support for arrays
#We have to import numpy library to work with arrays
import numpy as np

#Creating an array
arr = np.array([1, 2, 3, 4, 5])
print(arr)

#Accessing elements of an array
print(arr[0])

#Changing elements of an array
arr[0] = 6
print(arr)

#Length of an array
print(len(arr))

#Iterating through an array
for i in arr:
    print(i)

#Adding elements to an array
arr = np.append(arr, 7)
print(arr)

#Removing elements from an array
arr = np.delete(arr, 0)
print(arr)

#0-D array or scalars
arr0 = np.array(42)
print(arr)

#1-D array has 0-D arrays as its elements and is called uni-dimensional
arr1 = np.array([1, 2, 3, 4, 5])
print(arr)

#2-D array has 1-D arrays as its elements and is called bi-dimensional
#used to represent matrices or 2nd order tensors
arr2 = np.array([[1, 2, 3], [4, 5, 6]])
print(arr)

#3-D array has 2-D arrays as its elements and is called tri-dimensional
#used to represent a 3rd order tensor
arr3 = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])
print(arr)

#Checking the number of dimensions of an array
print(arr0.ndim)
print(arr1.ndim)
print(arr2.ndim)
print(arr3.ndim)

#Higher dimensional arrays
arr4 = np.array([1, 2, 3, 4], ndmin=5)
print(arr4)
print('number of dimensions :', arr4.ndim)

#Indexing in 2-D array
print(arr2[0, 1])

#Slicing in 2-D array
print(arr2[0, :])

#Indexing in 3-D array
print(arr3[0, 1, 2]) 

#Slicing in 3-D array
print(arr3[0, 1, :])