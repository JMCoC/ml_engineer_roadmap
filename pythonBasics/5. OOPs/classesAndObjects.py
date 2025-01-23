#OOPs is a way of organizing code that uses the concept of classes and objects
#to represent real-world entities and their behavior.

#Python is an object oriented programming language. 
#Almost everything in Python is an object, with its properties and methods. 
#A Class is like an object constructor, or a "blueprint" for creating objects.

#A class id a collection of objects. 
#It is a logical entity that has some specific attributes and methods.

#An object is an instance of a class. 
#It represents a specific implementation of a class and holds its own data.

#defining a class
class Dog:
    sound = "bark" #class attribute

#creating an object of the class
dog1 = Dog()

#accessing the class attribute
print(dog1.sound) #output: bark

#Using the __init__() function
#All classes have a function called __init__() (constructor), 
#which is always executed when the class is being initiated.

class Person:
    def __init__(self, name):
        self.name = name
    
    def sayHi(self):
        print("Hello, my name is " + self.name)

person1 = Person("John")
person1.sayHi() #output: Hello, my name is John

#self parameter is a reference to the current instance of the class,
#and is used to access variables that belongs to the class.

class check:
    def __init__(self):
        print("Address of self: ", id(self))

obj = check()
print("Address of obj: ", id(obj))
obj2 = check()
print("Address of obj2: ", id(obj2))

#__str__() method
#The __str__() method is called when you use the print() function on an object.

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def __str__(self):
        return "Person: " + self.name + ", " + str(self.age)

person1 = Person("John", 36)
print(person1) #output: Person: John, 36

#Class and Instance variables
#Class variables are shared by all instances of a class. They are defined within a class but outside any of the class's methods.
#Instance variables are unique to each instance. They are defined inside the constructor (__init__) method.

class Dog:
    kind = "canine" #class variable

    def __init__(self, name):
        self.name = name #instance variable
    
dog1 = Dog("Buddy")
dog2 = Dog("Max")

print(dog1.kind) #output: canine
print(dog2.kind) #output: canine
print(dog1.name) #output: Buddy
print(dog2.name) #output: Max

#modifying class and instance variables
#To modify a class variable, you need to access it using the class name.
#To modify an instance variable, you need to access it using the object name.

dog1.name = "Rocky"
print(dog1.name) #output: Rocky

Dog.kind = "feline"
print(dog1.kind) #output: feline
print(dog2.kind) #output: feline