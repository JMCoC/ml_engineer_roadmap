#Stacks follow the LIFO (Last In First Out) principle.
#means the last element added to the stack will be the first element to be removed.

#Basic operations of stack:
#1. Push: Add an element to the top of a stack
#2. Pop: Remove an element from the top of a stack
#3. IsEmpty: Check if the stack is empty
#4. IsFull: Check if the stack is full
#5. Peek: Get the value of the top element without removing it
#6. Size: Get the number of elements in the stack

#Stack implementation using list

stack = []

# Push operation
stack.append('a')
stack.append('b')
stack.append('c')
print(stack)

# Pop operation
stack.pop()
print(stack)

# Peek operation
print(stack[-1])

#implementation using collections.deque

from collections import deque

stack = deque()

# Push operation
stack.append('a')
stack.append('b')
stack.append('c')
print(stack)

# Pop operation
stack.pop()
print(stack)