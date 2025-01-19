#We raise an exception using the raise keyword. 
#We can optionally pass in an error message to the exception.
#Sintax: raise Exception('Error Message')

def set(age):
    if age < 0:
        raise ValueError("Age cannot be negative.")
    print(f"Age set to {age}")

try:
    set(-5)
except ValueError as e:
    print(e)