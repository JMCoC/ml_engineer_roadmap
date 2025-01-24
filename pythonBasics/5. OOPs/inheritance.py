#Inheritance allows us to define a class (child) 
#that inherits all the methods and properties from another class (parent).

#Parent class
class Person:
    def __init__(self, fname, lname):
        self.firstname = fname
        self.lastname = lname

    def printname(self):
        print(self.firstname, self.lastname)

    #You can difine a method to be overridden in the child class

    def welcome(self):
        pass #placeholder for the method

x = Person("John", "Doe")
x.printname()

#Child class
#To create a class that inherits the functionality from another class,
#send the parent class as a parameter when creating the child class:

class Student(Person):
    def welcome(self):
        return f"Welcome {self.firstname} {self.lastname} to the class"
#child class can also have its own properties and methods or override the parent class properties and methods.

#Now the Student class has the same properties and methods as the Person class.

x = Student("Mike", "Olsen")
x.printname()
print(x.welcome())

#__init__() method for the child class
#When you add the __init__() function, the child class will no longer inherit the parent's __init__() function.
#The child's __init__() function overrides the inheritance of the parent's __init__() function.

class Employee(Person):
    def __init__(self, fname, lname, year):
        super().__init__(fname, lname) #To keep the inheritance of the parent's __init__() function
        self.graduationyear = year

    def welcome(self):
        return f"Welcome {self.firstname} {self.lastname} to the class of {self.graduationyear}"
    
#super() function is used to refer to the parent class
#it allos you to call the parent class methods defined in the parent class from the child class
#The super() function returns an object that represents the parent class.

class Teacher(Person):
    def __init__(self, fname, lname, subject): #Parent and child can have theirown properties (Subject is a property of the teacher) 
        super().__init__(fname, lname)
        self.subject = subject

teacher = Teacher("John", "Doe", "Maths")
print(teacher.subject)
print(teacher.firstname)

#Types of inheritance
#Single inheritance: When a class inherits from only one class
#Multiple inheritance: When a class inherits from multiple classes
#Multilevel inheritance: When a class inherits from a class, that inherits from another class
#Hierarchical inheritance: When one class is inherited by multiple classes
#Hybrid inheritance: When a class is a combination of multiple types of inheritance

#1. Single inheritance
class Person:
    def __init__(self, fname):
        self.firstname = fname

class Employee(Person): #Employee class inherits from Person class
    def __init__(self, fname, salary):
        super().__init__(fname)
        self.salary = salary

# 2. Multiple inheritance
class Job:
    def __init__(self, salary):
        self.salary = salary

class EmployeePersonJob(Employee, Job): #Employee class inherits from Employee and Job class
    def __init__(self, fname, salary):
        Employee.__init__(self, fname, salary)
        Job.__init__(self, salary)

# 3. Multilevel inheritance
class Manager(EmployeePersonJob):
    def __init__(self, fname, salary, department):
        EmployeePersonJob.__init__(self, fname, salary)
        self.department = department

# 4. Hierarchical inheritance
class AssistantManager(EmployeePersonJob):
    def __init__(self, fname, salary, teamSize):
        EmployeePersonJob.__init__(self, fname, salary)
        self.teamSize = teamSize

# 5. Hybrid inheritance
class SeniorManager(Manager, AssistantManager):
    def __init__(self, fname, salary, department, teamSize):
        Manager.__init__(self, fname, salary, department)
        AssistantManager.__init__(self, fname, salary, teamSize)

#Single inheritance
emp = Employee("John", 50000)
print(emp.firstname, emp.salary)

#Multiple inheritance
emp2 = EmployeePersonJob("Alice", 50000)
print(emp2.firstname, emp2.salary)

#Multilevel inheritance
manager = Manager("Bob", 60000, "HR")
print(manager.firstname, manager.salary, manager.department)

#Hierarchical inheritance
assistantManager = AssistantManager("Charlie", 60000, 10)
print(assistantManager.firstname, assistantManager.salary, assistantManager.teamSize)

#Hybrid inheritance
seniorManager = SeniorManager("David", 70000, "Finance", 20)
print(seniorManager.firstname, seniorManager.salary, seniorManager.department, seniorManager.teamSize)