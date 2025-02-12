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

#Rounding Decimals

#Truncate, remove the decimal part and return the integer value

a = np.array([1.0, 2.1, 3.5, 4.2, 5.6, 6.0])
print(np.trunc(a))

#Fix, round towards zero
print(np.fix(a))

#Rounding (around() function)
print(np.around(a)) #If the decimal is less than 5, it rounds down, otherwise it rounds up.

#Floor, round down
print(np.floor(a)) #No matter what the decimal is, it always rounds down.

#Ceil, round up
print(np.ceil(a)) #No matter what the decimal is, it always rounds up.

#Logs (2, e, 10)
a = np.array([1, 2, 3, 4])
print(np.log2(a))
print(np.log(a))
print(np.log10(a))

#Summation 
#Addition vs Summation
a = np.array([1, 2, 3, 4])
b = np.array([5, 6, 7, 8])

newArray = np.add(a, b)
print(newArray)

newArray = np.sum([a, b])
print(newArray)

#Adittion is element-wise, while summation is the sum of all elements in the array.

#Over a specific axis
newArray = np.sum([a, b], axis=0)
print(newArray)

newArray = np.sum([a, b], axis=1)
print(newArray)

#Cumulative Sum
a = np.array([1, 2, 3, 4])
print(np.cumsum(a))

#Product
a = np.array([1, 2, 3, 4])
x = np.prod(a) #1*2*3*4
print(x)

b = np.array([5, 6, 7, 8])
newArray = np.prod([a, b])
print(newArray) #1*2*3*4*5*6*7*8

#Over a specific axis
newArray = np.prod([a, b], axis=0)
print(newArray)

newArray = np.prod([a, b], axis=1)
print(newArray)

#Cumulative Product
a = np.array([1, 2, 3, 4])
print(np.cumprod(a))

#Difference
a = np.array([1, 2, 3, 4])
print(np.diff(a)) #2-1, 3-2, 4-3

#We can perform this operation multiple times
print(np.diff(a, n=2)) #1. (2-1, 3-2, 4-3) result: 1, 1, 1. 2. (1-1, 1-1) result: 0, 0

#Lcm

num1 = 4
num2 = 6
print(np.lcm(num1, num2)) #12 cause 4*3=12 and 6*2=12

arr = np.array([3, 6, 9])
print(np.lcm.reduce(arr))

#Gcd

num1 = 4
num2 = 6
print(np.gcd(num1, num2)) #2 cause 4/2=2 and 6/2=3

arr = np.array([20, 8, 32, 36, 16])
print(np.gcd.reduce(arr)) #4 cause 20/4=5, 8/4=2, 32/4=8, 36/4=9, 16/4=4