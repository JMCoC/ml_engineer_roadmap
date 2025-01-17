#Comprehension and Generators

#Comprehension is a concise way to generate a list, set, or dictionary.

#Generators are used to create iterators, but with a different approach. 
#Generators are simple functions which return an iterable set of items, one at a time, in a special way.

#List comprehension
#List comprehension is an elegant way to define and create lists based on existing lists.

#Syntax:
#new_list = [expression for_loop_one_or_more conditions]


#Create a list of squares of numbers from 0 to 9
squares = [x**2 for x in range(10)]
print(squares)

#for loop equivalent
squares = []
for x in range(10):
    squares.append(x**2)
print(squares)

#List comprehension can be used to iterate through a list and apply a specific condition.

#Create a list of even numbers from 0 to 9
even_squares = [x**2 for x in range(10) if x%2 == 0]
print(even_squares)

#Nested list comprehension
#List comprehension can be nested where they can be used to iterate over multiple sequences.

#Create a list of tuples where each tuple contains the number and its square
number_square_pairs = [(x, x**2) for x in range(10)]
print(number_square_pairs)

#Matrix representation using nested list comprehension
matrix = [[j for j in range(5)] for i in range(5)]
print(matrix)


#Set comprehension
#Set comprehension is similar to list comprehension, the only difference is the use of curly braces {}.

#Create a set of squares of numbers from 0 to 9
squares_set = {x**2 for x in range(10)}
print(squares_set)

#Dictionary comprehension
#Dictionary comprehension is similar to list comprehension, the only difference is the way elements are assigned to the keys.

#Create a dictionary of squares of numbers from 0 to 9
squares_dict = {x: x**2 for x in range(10)}
print(squares_dict)

#Generator
#Generators are iterators, a kind of iterable you can only iterate over once.
#Generators do not store all the values in memory, they generate the values on the fly.
#Syntax:
#def generator_function(parameters):
#    ...
#    yield value
#    ...


#Create a generator to generate the squares of numbers from 0 to 9
def generate_squares(n):
    for i in range(n):
        yield i**2

squares = generate_squares(10)
for i in squares:
    print(i)

#Generator expression
#Generator expressions are similar to list comprehensions, but with parentheses () instead of square brackets [].

#Create a generator to generate the squares of numbers from 0 to 9
squares = (x**2 for x in range(10))
for i in squares:
    print(i)

#Generator expressions can be used as function arguments.

#Sum of squares of numbers from 0 to 9
sum_of_squares = sum(x**2 for x in range(10))
print(sum_of_squares)

#Generator expressions can be used as arguments to functions.

#Create a list of squares of numbers from 0 to 9
squares = list(x**2 for x in range(10))
print(squares)

#difference between list comprehension and generator expression
#List comprehension returns a list, generator expression returns a generator.

#Comparison of memory usage
#List comprehension stores the entire list in memory before returning the result.
#Generator expression generates one item at a time, thus saving memory.

#Comparison of time usage
#List comprehension is faster than generator expression when the number of elements is small.
#Generator expression is faster than list comprehension when the number of elements is large.

#Use list comprehension when you want to iterate over the entire list.
#Use generator expression when you want to iterate over the list partially.

#use timeit module to compare the time taken by list comprehension and generator expression and for loop
import time
#List comprehension
start_time = time.time()
squares = [x**2 for x in range(100000000)]
end_time = time.time()
print("Time taken by list comprehension: ", end_time - start_time) #12.6Seconds

#Generator expression
start_time = time.time()
squares = (x**2 for x in range(100000000))
end_time = time.time()
print("Time taken by generator expression: ", end_time - start_time) #1.38Seconds

#For loop
start_time = time.time()
squares = []
for x in range(100000000):
    squares.append(x**2)
end_time = time.time()
print("Time taken by for loop: ", end_time - start_time) #15.9Seconds
