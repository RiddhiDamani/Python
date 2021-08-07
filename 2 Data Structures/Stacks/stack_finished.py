# Stacks - Collection of elements that supports push and pop operations. 
#        - Last item pushed (Constant time O(1)) is the first one popped (Linear time O(n))
# Usage -  Expression processing, Backtracking : Browser back stack example
# Methods for Stack usage in Python: 1) append() 2) pop()


# try out the Python stack functions

# create a new empty stack list
stack = []

# push items onto the stack using append() method
stack.append(1)
stack.append(2)
stack.append(3)
stack.append(4)

# print the stack contents
print(stack)

# pop an item off the stack
x = stack.pop()
print(x)
print(stack)
