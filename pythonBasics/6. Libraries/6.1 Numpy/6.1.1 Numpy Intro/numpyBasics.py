#Numpy it's a library that allows us to work with arrays and matrices in Python.
#  It also provides a lot of mathematical functions that we can use to operate with these arrays.

#Why use Numpy?
# 1. Numpy arrays are faster and more efficient than Python lists because they are stored in contiguous memory blocks instead of being scattered across memory.
# 2. Numpy arrays are more convenient to work with because they allow us to perform operations on the entire array at once.
# 3. Numpy arrays are more powerful because they allow us to perform complex mathematical operations on arrays and matrices.

#Once we have installed Numpy, we can import it into our Python code using the following import statement:

import numpy as np #importing numpy library and renaming it as np

arr = np.array([1, 2, 3, 4, 5]) 
print(arr) 
print(type(arr)) #<class 'numpy.ndarray'>

#You can pass a list, tuple, or any array-like object to the np.array() function to create a Numpy array.
#The np.array() function will convert the input data into a Numpy array.

#Numpy arrays can have any number of dimensions. For example, you can create a 1D array, a 2D array, or even a 3D array.

arr0D = np.array(42) #0D array
arr1D = np.array([1, 2, 3, 4, 5]) #1D array
arr2D = np.array([[1, 2, 3], [4, 5, 6]]) #2D array
arr3D = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]]) #3D array

#You can check the number of dimensions of a Numpy array using the ndim attribute.

print(arr0D.ndim) #0
print(arr1D.ndim) #1
print(arr2D.ndim) #2
print(arr3D.ndim) #3

#Also you can use ndim as an argument to the np.array() function to create arrays with a specific number of dimensions.

arr0D = np.array(42, ndmin=5) #0D array with 5 dimensions
print(arr0D)

#Indexing works the same way as with Python lists. You can access elements of a Numpy array using square brackets and indices.

print(arr1D[0]) #1
print(arr2D[1, 0]) #4
print(arr3D[1, 0, 1]) #8

#Slicing also works the same way as with Python lists. You can use the colon operator to specify a range of indices to extract from the array.

print(arr1D[1:4]) #[2 3 4]
print(arr2D[0, 1:]) #[2 3]
print(arr3D[1, 0, :2]) #[7 8]

#Data types in Numpy
#Numpy arrays can have different data types. You can specify the data type of a Numpy array using the dtype argument of the np.array() function.

#i - integer
#b - boolean
#u - unsigned integer
#f - float
#c - complex float
#m - timedelta
#M - datetime
#O - object
#S - string
#U - unicode string
#V - fixed chunk of memory for other type ( void )

arr = np.array([1, 2, 3, 4], dtype='i') #integer
print(arr.dtype)

#if a type can't be converted, Numpy will raise an error.

#arr = np.array(['a', '1', '2'], dtype='i') #ValueError: invalid literal for int() with base 10: 'a'
#print(arr)

#You can convert the data type of a Numpy array using the astype() method.

arr = np.array([1.1, 2.2, 3.3, 4.4])
print(arr.dtype)
newarr = arr.astype('i') #or astype(int)
print(newarr)
print(newarr.dtype)