#A permutation refers to an arrangement of elements. For example [1, 2, 3] has 6 permutations:
# [1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 1, 2], [3, 2, 1]

#Shuffle array
#Shuffle means changing the position of elements in an array.

import numpy as np
from numpy import random

arr = np.array([1, 2, 3, 4, 5])
random.shuffle(arr) #Makes changes in the original array
print(arr)

#Generate a random permutation of elements
arr = np.array([1, 2, 3, 4, 5])
print(random.permutation(arr)) #Does not make changes in the original array
print(arr)

arr = np.arange(9).reshape(3, 3)
print(random.permutation(arr)) #Does not make changes in the original array
print(arr)