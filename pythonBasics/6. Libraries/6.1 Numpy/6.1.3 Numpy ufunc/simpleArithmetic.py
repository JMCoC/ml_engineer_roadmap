#You could use arithmetic operations directly on numpy arrays, but 
#numpy provides a set of functions that operate on arrays.

import numpy as np

a = np.array([1, 2, 3, 4])
b = np.array([5, 6, 7, 8])

#Addition
print(np.add(a, b))

#Subtraction
print(np.subtract(a, b))

#Multiplication
print(np.multiply(a, b))

#Division
print(np.divide(a, b))

#Exponentiation
print(np.power(a, b))

#Modulus
print(np.mod(a, b))

#Remainder
print(np.remainder(a, b))

#The mod function returns the remainder of division,
#while the remainder function returns the remainder of the floor division.

#Quotient and modulus
print(np.divmod(a, b))

#Absolute value
print(np.abs(a))