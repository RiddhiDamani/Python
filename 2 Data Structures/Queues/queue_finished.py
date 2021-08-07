# Queues - Collection that supports adding and removing
#        - First item added is the first item out. 
# Usage - Order/Message processing, Messaging
# We can use regular list as a queue in Python, but it is very inefficient method. B'coz removing an item from the front of the list requires a linear O(n) time complexity 'coz all the subsequent items have to be shifted down in their slots when we do that. There is a much efficient data structure in Python called as a deck object that we can use in a Python's collections module. 
# Methods for Queue usage in Python: 1) deque() 2) append() 3) popleft()

# try out the Python queue functions
# importing deque
from collections import deque

# create a new empty deque object that will function as a queue
queue = deque()

# add some items to the queue
queue.append(1)
queue.append(2)
queue.append(3)
queue.append(4)

# print the queue contents
print(queue)

# pop an item off the front of the queue
x = queue.popleft()
print(x)
print(queue)
