#Lists [] are mutable, ordered, and allow duplicate elements.
#basic list operations are append, insert, remove, pop, clear, index, count, sort, reverse, copy

list = ["apple", "banana", "cherry"]
print(list)

list.append("orange") #adds an element to the end of the list
print(list)
print(list[1]) #accessing elements by index
print(list[-1]) #accessing elements by negative index
print(list[1:3]) #slicing the list

list.append("apple") #allows duplicate elements
print(list)
print(len(list)) #length of the 

list2 = ["mango", 3, True, 3.14] #lists can have different data types

if "apple" in list:
    print("Yes, 'apple' is in the list")

list[1] = "blackcurrant" #changing an element
print(list)

list.insert(1, "blueberry") #inserting an element at a specific index
print(list)

list.extend(list2) #adding elements of list2 to list
print(list) #extend can add any iterable object (list, tuple, set, dictionary)
#using the extend method is more efficient than using the append method in a loop or using the + operator, in terms of time complexity and memory usage

list.remove("apple") #removing an element, if there are multiple elements, only the first occurrence is removed
print(list)

list.pop() #removes the last element, if an index is provided, that element is removed ( pop(1) removes the second element)
print(list)

del list[0] #removes the first element
print(list)
# del list #deletes the list

#list.clear() #removes all elements from the list

for x in list:
    print(x) #iterating through a list

for i in range(len(list)):
    print(list[i]) #iterating through a list using index

i = 0
while i < len(list):
    print(list[i]) #iterating through a list using while loop
    i += 1

list3 = ["apple", "banana", "cherry"]
list4 = [x for x in list3 if "a" in x] #list comprehension offers a shorter syntax to create a new list based on an existing list
print(list4) #Syntax: newlist = [expression for item in iterable if condition == True]
list5 = [x for x in range(10)] #the iterable can be any iterable object
print(list5)

list6 = [x.upper() for x in list3] #the expression can be anything
print(list6)

list7 = ["orange", "mango", "kiwi", "pineapple", "banana"]
list7.sort() #sorts the list in ascending order
print(list7)
list7.sort(reverse=True) #sorts the list in descending order
print(list7) #sort() works for numbers as well

list8 = [100, 50, 65, 82, 23]
list8.sort()
print(list8)

def myFunc(e):
    return abs (e - 50) #sorts the list based on how close the number is to 50

list8.sort(key=myFunc)
print(list8)

list7.append("Melon") #sort() is case sensitive, capital letters come before lowercase letters
list7.sort()
print(list7)
list7.sort(key=str.lower) #ignores the case
print(list7)

list7.reverse() #reverses the order of the list
print(list7)
#sort(reverse=True) and reverse() are not the same, sort(reverse=True) sorts the list in descending order, reverse() reverses the order of the original list

list9 = ["apple", "banana", "cherry"]
list10 = list9 #list10 is a reference to list9, changing list10 will change list9
#Show the memory address of the list

list10.append("orange")
print(list9)

list11 = list9.copy() #list11 is a copy of list9, changing list11 will not change list9
list11.append("mango")
print(list9)
print(list11)
print(id(list9))
print(id(list10)) #list10 and list9 have the same memory address
print(id(list11)) #list11 has a different memory address