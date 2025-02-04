import numpy as np

#The main difference between a copy and a view of an array is that 
# the copy is a new array, and the view is just a view of the original array.

#The copy owns the data and any changes made to the copy 
# will not affect original array, and any changes made to the original array 
# will not affect the copy.

#The view does not own the data and any changes made to the view 
# will affect the original array, and any changes made to the original array 
# will affect the view.

arr = np.array([1, 2, 3, 4, 5])
x = arr.copy()
y = arr.view()
arr[0] = 42

print(arr) # [42  2  3  4  5]
print(x) # [1 2 3 4 5]
print(y) # [42  2  3  4  5]

#Make changes to the copy
x[0] = 99
print(arr) # [42  2  3  4  5]
print(x) # [99  2  3  4  5]
print(y) # [42  2  3  4  5]

#Make changes to the view
y[0] = 11
print(arr) # [11  2  3  4  5]
print(x) # [99  2  3  4  5]
print(y) # [11  2  3  4  5]

#Check if array owns the data
#if base is None, the array owns the data

print(x.base) # None
print(y.base) # [11  2  3  4  5]