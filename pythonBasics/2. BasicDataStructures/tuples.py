#Tuples () are immutable, ordered and allow duplicate elements. 
#They are used to store multiple items in a single variable.
#Basic tuple operations are count, index

myTuple = ("apple", "banana", "cherry", "apple")
print(myTuple)

print(len(myTuple)) #length of the tuple

#to create a tuple with only one item, you need to add a comma after the item, otherwise python will not recognize it as a tuple
tuple2 = ("apple",)
print(type(tuple2))
notTuple = ("apple")
print(type(notTuple))

#tuples can be of different data types and can contain different data types
tuple3 = ("apple", 3, True, 3.14)

#accessing elements by index
print(myTuple[1])
print(myTuple[-1])
print(myTuple[1:3])

#checking if an element is in the tuple
if "apple" in myTuple:
    print("Yes, 'apple' is in the tuple")

#once a tuple is created, you cannot change its values, but you can convert it to a list and change the values
listFromTuple = list(myTuple)
listFromTuple[1] = "blackcurrant"
myTuple = tuple(listFromTuple) #the tuple() constructor is used to create a tuple
print(myTuple)
#you can use de add or remove methods but first you need to convert the tuple to a list

#You can add a tuple to another tuple
tuple4 = ("kiwi", "orange")
newTuple = myTuple + tuple4
print(newTuple)

#del myTuple #deletes the tuple
#print(myTuple) #this will raise an error because the tuple no longer exists

#Unpacking a tuple
fruits = ("apple", "banana", "cherry")
(green, yellow, red) = fruits
print(green)
print(yellow)
print(red)
#We asign the values of the tuple to the variables in the same order as the tuple

#If the number of variables is less than the number of values, you can add an * to the variable name and the values will be assigned to the variable as a list
fruits = ("apple", "banana", "cherry", "strawberry", "raspberry")
(green, yellow, *red) = fruits
print(green)
print(yellow)
print(red)
(green, *yellow, red) = fruits
print(green)
print(yellow)
print(red)
#python will assign values to the variable until the number of variables is equal to the number of values left

#Looping through a tuple
for x in fruits:
    print(x)

#Looping through a tuple with index
for i in range(len(fruits)):
    print(fruits[i])

#looping through a tuple with while
i = 0
while i < len(fruits):
    print(fruits[i])
    i += 1

#count() method returns the number of times a specified value occurs in a tuple
print(myTuple.count("apple"))

#index() method returns the index of the first occurrence of the specified value
print(myTuple.index("cherry"))