#sets {} are unordered, unchangeble, unindexed and do not allow duplicates

thisSet = {"apple", "banana", "cherry"}
print(thisSet)

#1 and true are considered the same value, same for 0 and false
thisSet = {1, True, 0, False}
print(thisSet)

#length of the set
print(len(thisSet))

#set items can be of different data types and can contain different data types
thisSet = {"apple", 1, True, 3.14}
print(thisSet)
print(type(thisSet))

#set() constructor can be used to create a set
thisSet = set(("apple", "banana", "cherry"))
print(thisSet)

#accessing elements by index is not possible in sets
# print(thisSet[1]) #error
#but we can loop through the set
for x in thisSet:
    print(x)

print("banana" in thisSet) #check if an element is in the set

#add() method is used to add an element to the set
thisSet.add("orange")
print(thisSet)

#update() method is used to add multiple elements to the set
tropical = {"pineapple", "mango", "papaya"}
thisSet.update(tropical)
print(thisSet)
#update() can take any iterable object as an argument
mylist = ["kiwi", "orange"]
thisSet.update(mylist)
print(thisSet)

#remove() method is used to remove an element from the set
thisSet.remove("kiwi")
print(thisSet)
#if the element is not in the set, remove() will raise an error
# thisSet.remove("kiwi") #error
#discard() method is used to remove an element from the set
thisSet.discard("kiwi") #no error
print(thisSet)

#pop() method is used to remove the last element from the set, but since sets are unordered, the last element is arbitrary
thisSet.pop()
print(thisSet)

#clear() method is used to empty the set
thisSet.clear()
print(thisSet)

#del keyword is used to delete the set
#del thisSet
# print(thisSet) #error

#Join Sets
#union() and update() methods are used to join two sets
#the difference between the two is that union() method returns a new set, update() method inserts the elements from the second set into the first set

set1 = {"a", "b", "c"}
set2 = {1, 2, 3}
set3 = set1.union(set2) #you can also use the | operator instead of union()
print(set3)

#update() method can join multiple sets
set4 = {"d", "e", "f"}
set3 = set1.union(set2, set4) #set3 = set1 | set2 | set4
print(set3)

#You can join a set with other data types using the union() method

y = (5, 6, 7)
set5 = set1.union(y) #the | only works with sets
#set5 = set1 | y #error
print(set5)

set1.update(set2) #set1 = set1 | set2
print(set1)

#intersection() method returns a set that contains the common elements of two or more sets
set1 = {"a", "b", "c"}
set2 = {"a", "b", "c", 1, 2, 3}
set3 = set1.intersection(set2) #you can also use the & operator instead of intersection()
print(set3)

#intersection_update() method removes the elements that are not present in both sets
set1 = {"a", "b", "c"}
set2 = {"a", "b", "c", 1, 2, 3}
set2.intersection_update(set1) #set1 = set1 & set2
print(set2)

#difference() method returns a set that contain the items that only exist in the first set, and not in the second set
set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}
set3 = set2.difference(set1) #you can also use the - operator instead of difference()
print(set3)
#the - operator only works with sets

#difference_update() method removes the items that exist in both sets, and updates the first set
set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}
set2.difference_update(set1) #set1 = set1 - set2
print(set2)

#symmetric_difference() method returns the elements that are not present in both sets
set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}
set3 = set1.symmetric_difference(set2) #you can also use the ^ operator instead of symmetric_difference()
print(set3)
#the ^ operator only works with sets

#symmetric_difference_update() method removes the items that are present in both sets, and inserts the other items
set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}
set2.symmetric_difference_update(set1) #set1 = set1 ^ set2
print(set2)

#rest of the methods 
#isdisjoint() method returns True if none of the items are present in both sets
#issubset() method returns True if all items in the set exists in the specified set
#issuperset() method returns True if all items in the specified set exists in the original set
#copy() method returns a copy of the set