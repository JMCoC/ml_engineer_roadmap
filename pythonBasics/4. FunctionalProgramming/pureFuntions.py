#The pure functions always return the same result for the same arguments.
#The pure functions do not produce side effects.
#Does not modify the arguments passed to it. (Immutable)
#Also make it easier to test the code and write concurrent code.

#Pure Function

def multiplyBy2(li):
    newList = []
    for item in li:
        newList.append(item*2)
    return newList
    #return [item*2 for item in li] #List comprehension

print(multiplyBy2([1,2,3])) # [2,4,6]

#Non-Pure Function

newList = []
def multiplyBy2(li):
    for item in li:
        newList.append(item*2)
    return newList

print(multiplyBy2([1,2,3])) # [2,4,6]

#The above function is not pure because it is modifying the global variable newList.