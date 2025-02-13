import numpy as np

arr1 = np.array([1, 1, 1, 2, 3, 3, 4, 5]) #Arrays should be 1D

x = np.unique(arr1)
print(x) #Set of unique elements in arr1

arr2 = np.array([5, 6, 7, 8, 9, 10, 11, 12])

y = np.union1d(arr1, arr2)
print(y) #Union of arr1 and arr2

z = np.intersect1d(arr1, arr2)
print(z) #Intersection of arr1 and arr2

a = np.setdiff1d(arr1, arr2)
print(a) #Elements in arr1 that are not in arr2

b = np.setxor1d(arr1, arr2)
print(b) #Symmetric difference of arr1 and arr2