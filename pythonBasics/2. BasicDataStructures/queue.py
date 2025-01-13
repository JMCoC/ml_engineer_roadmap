#Queues follow the First In First Out (FIFO) principle.
#means the first element added to the queue will be the first element to be removed.

#Basic operations of queue:
#1. Enqueue: Add an element to the end of the queue
#2. Dequeue: Remove an element from the front of the queue
#3. IsEmpty: Check if the queue is empty
#4. IsFull: Check if the queue is full
#5. Peek: Get the value of the front element without removing it
#6. Size: Get the number of elements in the queue

#Queue implementation using list

queue = []

# Enqueue operation
queue.append('a')
queue.append('b')
queue.append('c')
print(queue)

# Dequeue operation
queue.pop(0)
print(queue)

# Peek operation
print(queue[0])

#implementation using collections.deque

from collections import deque

queue = deque()

# Enqueue operation
queue.append('a')
queue.append('b')
queue.append('c')
print(queue)

# Dequeue operation
queue.popleft()
print(queue)