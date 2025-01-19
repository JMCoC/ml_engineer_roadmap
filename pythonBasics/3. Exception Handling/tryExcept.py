#Exception Handling
#When an error occurs, or exception as we call it, 
#Python will normally stop and generate an error message.
#These exceptions can be handled using the try, except, else, and finally blocks.

#try block: lets you test a block of code for errors. Python will "try" to execute the code
#if an error occurs, it will be handled by the except block.

#except block: lets you handle the error. You can define what the program should do if an error occurs.
#We can handle specific errors by specifying the error after the except keyword.
#or we can handle all errors by not specifying any error after the except keyword.

#else block: is optional and will execute if the try block does not raise an error.

#finally block: Always runs after the try block and the except block, regardless of whether the try block raises an error or not.

#The try block will generate an exception, because x is not defined:
try:
    print(x)  
except:
    print("An exception occurred")

#Since the try block raises an error, the except block will be executed.
#Without the try block, the program will crash and raise an error:

#print(x) #This will raise an error

try:
    n = int(input("Enter a number: "))
    res = 10 / n

except ZeroDivisionError:
    print("You cannot divide by zero.")

except ValueError:
    print("Please enter a valid number.")

else:
    print(f"The result is {res}")

finally:
    print("Exiting the program")

#There are many types of exceptions in Python.
#NameError, TypeError, ZeroDivisionError, ValueError, FileNotFoundError, etc.