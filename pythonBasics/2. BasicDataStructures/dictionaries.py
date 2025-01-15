#Dictionaries {} are used to store data in key-value pairs. They are mutable, ordered and do not allow duplicate keys.

#Creating a dictionary
my_dict = {
    "name": "John",
    "age": 25,
    "city": "New York"
}
print(my_dict)

#Accessing values
print(my_dict["name"])

#duplicate keys are not allowed
my_dict = {
    "name": "John",
    "age": 25,
    "city": "New York",
    "name": "Doe"
} #This will overwrite the value of the key "name"
print(my_dict)

#length of dictionary
print(len(my_dict))

#Data types iteams in dictionary
my_dict = {
    "name": "John",
    "age": 25,
    "city": "New York",
    "is_student": False,
    "marks": [70, 80, 90]
}

#dict() constructor
my_dict = dict(name="John", age=25, city="New York")
print(my_dict)

#get() method
print(my_dict.get("name")) #John

#keys() method
print(my_dict.keys()) 

#values() method
print(my_dict.values()) 

#add a new key-value pair
print(my_dict)
my_dict["is_student"] = False
print(my_dict)

#items() method
print(my_dict.items()) #return each item as a list of tuples

#check if key exists
if "name" in my_dict:
    print("Yes") #print("name" in my_dict)

#if you asign the methos keys, values or items to a variable, it will return a view object
#if you change the dictionary, the view object will also change
keys = my_dict.values()
print(keys)
my_dict["city"] = "Boston"
print(keys)

#change the value of a key
my_dict["name"] = "Doe"
print(my_dict)

#update() method
my_dict.update({"name": "John", "age": 25})
#if the key does not exist, it will be added
my_dict.update({"is_student": True})

#remove a key-value pair
my_dict.pop("city")
print(my_dict)

#popitem() method
my_dict.popitem() #remove the last key-value pair
print(my_dict)

#del removes the key-value pair or the entire dictionary
del my_dict["age"]
print(my_dict)
#del my_dict
#print(my_dict) #NameError: name 'my_dict' is not defined

#clear() method
my_dict = {
    "name": "John",
    "age": 25,
    "city": "New York"
}
print(my_dict)
my_dict.clear()
print(my_dict)

#loop through a dictionary
#looping through dictionary will return the keys, but there are ways to get the values

my_dict = {
    "name": "John",
    "age": 25,
    "city": "New York"
}

for i in my_dict:
    print(i) #print the keys

for i in my_dict.values():
    print(i) #print the values

for i in my_dict.keys():
    print(i) #print the keys

for key, value in my_dict.items():
    print(key, value) #print the key-value pairs

#copy a dictionary
#You can not copy a dictionary by simply assigning it to a new variable (dict2 = dict1)
#dict2 will be a reference to dict1, so any changes made in dict1 will be reflected in dict2
#use the copy() method to create a copy of the dictionary

my_dict = {
    "name": "John",
    "age": 25,
    "city": "New York"
}

dict2 = my_dict.copy() #dict2 = dict(my_dict)
print(dict2)
print(id(my_dict))
print(id(dict2))

#nested dictionaries

myFamily = {
    "child1": {
        "name": "Tom",
        "age": 5
    },
    "child2": {
        "name": "Jane",
        "age": 7
    },
    "child3": {
        "name": "John",
        "age": 10
    }
}

#or add a dictionary to another dictionary
child1 = {
    "name": "Tom",
    "age": 5
}

child2 = {
    "name": "Jane",
    "age": 7
}

child3 = {
    "name": "John",
    "age": 10
}

myFamily = {
    "child1": child1,
    "child2": child2,
    "child3": child3
}

#accessing values in nested dictionaries
print(myFamily["child1"]["name"])

#loop through a nested dictionary
for child in myFamily:
    print(myFamily[child]["name"])