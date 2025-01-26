#Abstraction is used to hide the internal functionality of the function 
#from the users. The users only interact with the basic implementation 
#of the function, but inner working is hidden. User is familiar with 
# that a particular action will be performed, but don’t need to know 
#how the action will be performed.

#Abstraction can be achieved by using abstract classes and interfaces.
#Python does not have abstract classes and interfaces like other
#object-oriented languages, but we can achieve abstraction using
#the abc module.

#Abstraction classes
#Abstract classes are classes that contain one or more abstract methods
#with no implementation.

#Abstract method: A method that is declared, but contains no implementation.
# Concrete method: A method that is declared with implementation. 

from abc import ABC, abstractmethod

class Car(ABC):
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year
    
    @abstractmethod
    def printDetails(self):
        pass

    def accelerate(self):
        print("Accelerating...")
    
    def stop(self):
        print("Stopping...")

class BMW(Car):
    def __init__(self, brand, model, year, color):
        super().__init__(brand, model, year)
        self.color = color
    
    def printDetails(self):
        print(f"Brand: {self.brand}, Model: {self.model}, Year: {self.year}, Color: {self.color}")

class Audi(Car):
    def __init__(self, brand, model, year, color):
        super().__init__(brand, model, year)
        self.color = color
    
    def printDetails(self):
        print(f"Brand: {self.brand}, Model: {self.model}, Year: {self.year}, Color: {self.color}")

#car = Car("BMW", "X5", 2021) #TypeError: Can't instantiate abstract class Car with abstract methods printDetails
bmw = BMW("BMW", "X5", 2021, "Black")
bmw.printDetails()
bmw.accelerate()
bmw.stop()

