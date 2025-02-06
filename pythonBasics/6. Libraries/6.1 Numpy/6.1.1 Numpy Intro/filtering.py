#You can filter the elements of an array using a boolean index.
import numpy as np

arr = np.array([41, 42, 43, 44])
x = [True, False, True, False]
newarr = arr[x]
print(newarr)

#But the common use is to create a filter array based on a condition.

filter_arr = []

for element in arr:
  if element > 42:
    filter_arr.append(True)
  else:
    filter_arr.append(False)

newarr = arr[filter_arr]

print(filter_arr)
print(newarr)

#You can also use the filter array directly.

filter_arr = arr > 42
newarr = arr[filter_arr]
print(filter_arr)
print(newarr)