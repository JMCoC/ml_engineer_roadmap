#Ufuncs stands for "Universal Functions" and they are NumPy functions 
# that operates on the ndarray object.
# Why use ufuncs?
# They are used to implement vectorization in NumPy which is way faster 
# than iterating over elements.

#What is vectorization?
#Converting iterative statements into a vector based operation is 
# called vectorization.

#It is faster as modern CPUs are optimized for such operations.

#Example:
#Add the Elements of Two Lists

#Without ufunc, we can use Python's built-in zip() method:

x = [1, 2, 3, 4]
y = [4, 5, 6, 7]

z = []
for i, j in zip(x, y):
  z.append(i + j)
print(z)

#NumPy has a ufunc for this, called add(x, y) that will produce the same result.

import numpy as np

z = np.add(x, y)
print(z)

#Create Your Own ufunc
#To create you own ufunc, you have to define a function, like you do with
#normal functions in Python, then you add it to your NumPy ufunc library
#with the frompyfunc() method.

#The frompyfunc() method takes the following arguments:

#function - the name of the function.
#inputs - the number of input arguments (arrays).
#outputs - the number of output arrays.

def myadd(x, y):
  return x+y

myadd = np.frompyfunc(myadd, 2, 1)
print(myadd([1, 2, 3, 4], [5, 6, 7, 8]))

#Check if a Function is a ufunc
#Check if a function is a ufunc by using the numpy.ufunc attribute.

#A ufunc should return <class 'numpy.ufunc'>.

print(type(np.add))

#If it is not a ufunc, it will return <class 'function'>.

print(type(np.concatenate))