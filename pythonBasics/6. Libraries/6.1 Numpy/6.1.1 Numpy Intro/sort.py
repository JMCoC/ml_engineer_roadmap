#You can put the elements in an ordered sequence using the sort() method.

import numpy as np

arr = np.array([3, 2, 0, 1])
print(np.sort(arr))
#This method returns a copy of the array without modifying the original array.

#You can also sdort arrays of strings or any other data type.
arr = np.array(['banana', 'cherry', 'apple'])
print(np.sort(arr))

arr = np.array([True, False, True])
print(np.sort(arr))

#You can also sort a 2-D array.
arr = np.array([[3, 2, 4], [5, 0, 1]])
print(np.sort(arr))