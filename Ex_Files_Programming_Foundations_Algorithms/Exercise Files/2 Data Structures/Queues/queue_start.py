# try out the Python queue functions
from collections import deque

# TODO: create a new empty deque object that will function as a queue
list= deque()


# TODO: add some items to the queue
list.append(10)
list.append(20)
list.append(30)
list.append(40)

# TODO: print the queue contents
print(list)

# TODO: pop an item off the front of the queue
list.popleft()
print(list)