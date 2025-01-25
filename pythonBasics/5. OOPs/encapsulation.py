#Encapsulation is the process of restricting access to methods and variables
#in a class in order to prevent direct modification of data.
#Python achives through public, protected and private access specifiers.

#How encapsulation works
#Data Hiding: The object's data should not be directly accessible to the user.
#Access through methods: The object's data should only be accessed through its methods. (getters and setters)

#Public members: The members of a class that are accessible 
#from outside the class are called public members.

class Public:
    def __init__(self):
        self.name = "Public" #public variable
    
    def display(self):
        print(self.name) #public method

obj = Public()
obj.display() #Accessible
print(obj.name) #Accessible

#Protected members: Are defined by a single underscore prefix.
#They are meant to be accessed only within the class or by a subclass.

class Protected:
    def __init__(self):
        self._name = "Protected" #protected variable
    
class SubProtected(Protected):
    def display(self):
        print(self._name) #protected method

obj = SubProtected()
obj.display() #Accessible

#Private members: Are defined by a double underscore prefix.
#They are meant to be accessed only within the class.
#Python uses name mangling to make it difficult to access private members from outside the class.
#Name mangling is a process of adding some data to the member name to make it unique.

class Private:
    def __init__(self):
        self.__name = "Private" #private variable
    
    def display(self):
        print(self.__name) #private method

obj = Private()
print(obj.display()) #Accessible
# print(obj.__name) #Not Accessible

#Name mangling
#Python internally changes the name of the private variable to _classname__variable.

print(obj._Private__name) #Accessible

#getters and setters
#Getters are methods that get the value of a private variable.
#Setters are methods that set the value of a private variable.

class Dog:
    def __init__(self, name, breed, age):
        self.name = name
        self._breed = breed
        self.__age = age
    
    #Public method
    def get_info(self):
        return self.name, self._breed, self.__age
    
    #Getter
    def get_age(self):
        return self.__age
    
    #Setter
    def set_age(self, age):
        if age > 0:
            self.__age = age
        else:
            print("Age cannot be negative")

dog = Dog("Tommy", "Labrador", 5)
print(dog.name) #Accessible
print(dog._breed) #Accessible
# print(dog.__age) #Not Accessible
print(dog.get_age()) #Accessible
dog.set_age(7)
print(dog.get_age()) #Accessible
print(dog.get_info()) #Accessible