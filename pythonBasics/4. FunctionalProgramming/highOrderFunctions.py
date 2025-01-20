#A high order function is a function that takes another function 
#as an argument or returns a function as a result.

#passed as an argument

def square(x):
    return x*x

def cube(x):
    return x*x*x

def my_map(func, arg_list):
    result = []
    for i in arg_list:
        result.append(func(i))
    return result

squares = my_map(square, [1, 2, 3, 4, 5])
cubes = my_map(cube, [1, 2, 3, 4, 5])

print(squares)
print(cubes)

#returned as a result

def logger(msg):
    def logMessage():
        return f"Log: {msg}"
    return logMessage

log_hi = logger("Hi!")
print(log_hi())

#In python we have built-in higher order functions like map, filter and reduce

#map() function returns a map object(which is an iterator) 
#of the results after applying the given function to each item 
#of a given iterable (list, tuple etc.)

def square(x):
    return x*x

numbers = [1, 2, 3, 4, 5]
squared = map(square, numbers) #we can also use lambda function here or convert the map object to a list (list(map(square, numbers)))

print(squared)

for i in squared:
    print(i, end=" ")

#using lambda function and converting the map object to a list

numbers = [1, 2, 3, 4, 5]
squared = list(map(lambda x: x*x, numbers))

print(squared)

#map with multiple iterables

a = [1, 2, 3, 4, 5]
b = [6, 7, 8, 9, 10]
res = list(map(lambda x, y: x*y, a, b))
print(res)

#filter() function returns an iterator were the items are filtered 
#with help of a function that returns either True or False

def is_even(x):
    return x % 2 == 0

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
evens = filter(is_even, numbers) #we can also use lambda function here or convert the filter object to a list (list(filter(is_even, numbers)))

print(evens)

for i in evens:
    print(i, end=" ")

#using lambda function and converting the filter object to a list

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
evens = list(filter(lambda x: x % 2 == 0, numbers))

print(evens)

#combine map and filter

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

filtered = filter(lambda x: x % 2 == 0, numbers)
mapped = map(lambda x: x*x, filtered)

print(list(mapped))

#reduce() function is used to apply a particular function passed in its argument
#to all of the list elements mentioned in the sequence passed along.

from functools import reduce

def add(x, y):
    return x + y

numbers = [1, 2, 3, 4, 5]
result = reduce(add, numbers) #we can also use lambda function here

print(result)

#using lambda function

numbers = [1, 2, 3, 4, 5]
result = reduce(lambda x, y: x + y, numbers)

print(result)