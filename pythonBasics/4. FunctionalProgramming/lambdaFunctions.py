#Lambda functions are small anonymous functions (no name)
#that can take any number of arguments, but can only have one expression. 
#They are useful when you need a short function for a short period of time.

#Syntax: lambda arguments : expression

#Example:
x = lambda a : a + 10
print(x(5))

#Lambda with conditional statement
x = lambda a : True if a > 10 else False
print(x(5))
print(x(15))

#Lambda with multiple arguments and statements

x = lambda a, b : a * b
print(x(5, 6))

x = lambda a, b : (a * b, a + b)
print(x(5, 6))

#Lambda with list comprehension
x = lambda a : [i for i in range(a)]
print(x(5))

li = [lambda arg = x: arg*10 for x in range(1,5)]

for f in li:
    print(f())