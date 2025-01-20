#Functional programming there's no loops (for, while), only recursion
#Recursion is a function that calls itself directly or indirectly

#Example of recursion

def factorial(n):
    if n == 1:
        return 1 #base case
    else:
        return n * factorial(n - 1)

print(factorial(5)) #120

#Fibonacci sequence

def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)

print(fibonacci(6)) #8

#Recursion is not always the best solution, it can be slow and use a lot of memory
#It's better to use loops when possible
#Recursion is useful when the problem can be broken down into smaller problems of the same type