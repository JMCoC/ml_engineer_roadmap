#First-class functions is a concept in functional programming 
#where functions are treated as first-class citizens. 
#This means that functions can be passed as 
#1. arguments to other functions, 
#2. returned as values from other functions, 
#3. assigned to variables and 
#4. stored in data structures.

#Assigning a function to a variable

def square(x):
    return x*x

f = square
print(f(5))

#Passing a function as an argument to another function (Higher Order Function)

def msg(name):
    return f"Hello {name}"

def call_func(func, name):
    return func(name)

print(call_func(msg, "John"))

#Returning a function from another function

def logger(msg):
    def logMessage():
        return f"Log: {msg}"
    return logMessage

log_hi = logger("Hi!")
print(log_hi())

#Storing functions in data structures

def add(x, y):
    return x + y

def sub(x, y):
    return x - y

d = {
    "add": add, #with lambda function: "add": lambda x, y: x + y
    "sub": sub 
}

print(d["add"](5, 3))
print(d["sub"](5, 3))