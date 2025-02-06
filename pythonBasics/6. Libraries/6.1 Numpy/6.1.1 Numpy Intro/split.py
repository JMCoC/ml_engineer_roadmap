#Split is the reverse of join. 
# It splits a string into a list of strings based on a delimiter.

import numpy as np

arr = np.array([1, 2, 3, 4, 5, 6])
newarr = np.array_split(arr, 3) #it's a python list and inside it has 3 numpy arrays
print(newarr)

#If the array has less elements than required, it will adjust from the end accordingly.

arr = np.array([1, 2, 3, 4, 5, 6])
newarr = np.array_split(arr, 4)
#newarr2 = np.split(arr, 4) #ValueError: array split does not result in an equal division
print(newarr)
#We also have the method split() available but it will not adjust 
# the elements when elements are less in source array for splitting 
# like in example 2. That would throw an error.

#You can access them using the index.
print(newarr[0])
print(newarr[1])

#Splitting 2-D Arrays
#Use the same syntax when splitting 2-D arrays.

arr = np.array([[1, 2], [3, 4], [5, 6], [7, 8], [9, 10], [11, 12]])
newarr = np.array_split(arr, 3) #Returns 3 2-D arrays
print(newarr)

#Using axis

arr = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12], [13, 14, 15], [16, 17, 18]])
newarr = np.array_split(arr, 3, axis=1) #Splits the 2-D array into three 2-D arrays along rows
print(newarr)

#An alternate solution is using hsplit() opposite of hstack() and vsplit() opposite of vstack().

newarr = np.hsplit(arr, 3) #Splits the 2-D array into three 2-D arrays along rows
print(newarr)