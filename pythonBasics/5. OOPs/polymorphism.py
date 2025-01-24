#Allos entities like functions, methods or operators to act differently 
#based on the type of data they are handling

#Polymorphism with built-in functions
print(len("geeks")) #string length
print(len([10, 20, 30])) #list length
#Python determines behavior at runtime

#Polymorphism with functions
def add(x, y):
    return x + y 

print(add(5, 6))
print(add([1, 2, 3], [4, 5, 6]))
print(add("Hello ", "World"))
#Duck Typing: Anothe way of achieving polymorphism
# Object must have the minimum necessary methods/atrrubutes to be used
# "if it looks like a duck and quacks like a duck, it must be a duck"

#Polymorphism in operator overloading
#Means that an operator behaves differently based on the type of data it is handling
print(5 + 6)
print("Hello " + "World")

#Polymorphism in OOPs
# Allows methods in different classes to have the same name
# but different signatures

class Shape:
    def area(self):
        return "Undefined"

class Rectangle(Shape):
    def __init__(self, length, breadth):
        self.length = length
        self.breadth = breadth

    def area(self):
        return self.length * self.breadth

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius ** 2

shapes = [Rectangle(10, 20), Circle(5)]
for shape in shapes:
    print(shape.area())

#Abstract classes
#Classes that have methods that are not implemented
#Abstract classes cannot be instantiated
#They are meant to be inherited by other classes
#Abstract methods are meant to be overridden by the inheriting class

from abc import ABC, abstractmethod

class Animal(ABC):
    @abstractmethod #decorator
    def talk(self):
        pass

#animal = Animal() #TypeError: Can't instantiate abstract class Animal with abstract methods talk

class Dog(Animal):
    def talk(self):
        return "Woof Woof"

class Cat(Animal):
    def talk(self):
        return "Meow Meow"
    #if talk method is not implemented, TypeError will be raised

animals = [Dog(), Cat()]
for animal in animals:
    print(animal.talk())

#Polymorphism with inheritance
#Method overriding

class Animal:
    def talk(self):
        return "Animal talks"

class Dog(Animal):
    def talk(self): #overriding
        return "Dog barks"

class Cat(Animal):
    def talk(self):
        return "Cat meows"