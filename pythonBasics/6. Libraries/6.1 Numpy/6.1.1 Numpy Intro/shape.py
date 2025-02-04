#The shape of an array is the number of elements in each dimension.
#NumPy arrays have an attribute called shape that returns a tuple 
# with each index having the number of corresponding elements.

import numpy as np

arr = np.array([[1, 2, 3, 4], [5, 6, 7, 8]])
print(arr.shape)

#Reshaping means changing the shape of an array
#The shape of an array is the number of elements in each dimension.
#By reshaping, we can add or remove dimensions or change number of elements in each dimension.

arr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]) #1D array with 12 elements
newarr = arr.reshape(4, 3) #2D array with 4 rows and 3 columns
print(newarr)

newarr = arr.reshape(2, 3, 2) #3D array with 2 arrays, each with 3 rows and 2 columns
print(newarr)

#To reshape correctly, the new shape must be compatible with the original shape
#meaning that 4*3 = 12 and 2*3*2 = 12
#if the elements don't fit, you will get an error

#shape it's a copy or a view?

print(arr.reshape(2, 3, 2).base) #The example above returns the original array, so it is a view

newarr[0, 1, 1] = 42
print(newarr) #The new array is changed
print(arr) #The original array is also changed

#Unknown dimension
#You are allowed to have one "unknown" dimension.
#Meaning that you do not have to specify an exact number for one of the dimensions in the reshape method.
#Pass -1 as the value, and NumPy will calculate this number for you.

arr = np.array([1, 2, 3, 4, 5, 6, 7, 8])
newarr = arr.reshape(2, 2, -1) #The unknown dimension is 
print(newarr)

#Flattening the arrays
#Flattening an array means converting a multidimensional array into a 1D array.
#You can use the reshape(-1) method to do this.

arr = np.array([[1, 2, 3], [4, 5, 6]])
newarr = arr.reshape(-1)
print(newarr)

#Note: There are a lot of functions for changing the shapes of arrays in numpy flatten, ravel and also for rearranging the elements rot90, flip, fliplr, flipud etc.
#1. flatten: returns a copy of the array collapsed into one dimension
#2. ravel: returns a contiguous flattened array(only a view of the original array will be returned)
#3. rot90: rotates the array by 90 degrees
#4. flip: flips the array in a given direction
#5. fliplr: flips the array from left to right
#6. flipud: flips the array from up to down