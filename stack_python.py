class Stack:

    # here we are using the built-in methods of List data type i.e. append(), pop(), etc. 
    def __init__(self):
        self.items = []
    
    # add item to stack
    def push(self,item):
        """Doc strings: Accepts an item as a parameter and appendes it to the end of the list. 
        Returns nothing.
        Runtime : O(1), or constant time, because appendingn to the end of the list happens in the constant time. Python automatically goes to the last index of the list and appends the item there. 
        """
        self.items.append(item)
    
    # List built in method of python always returns the last item from it. So, no need to write item as parameter
    # remove item from top of list
    # if you dont give the pop() method any parameters it will always return last item added i.e. top item from the list.
    def pop(self):

        """
        Removes and returns the last item from the list which is also the top item of the stack. 
        Runtime: O(1), constant because all it does is index to the last item of the list.
        """
        if(self.items):
            return self.items.pop()
        else:
            return None

    def peek(self):
        """
        Returns the last item in the list which is also the top item of the stack. 
        Runtime: O(1), constant time because indexing into a list is done in constant time
        """
        # -1 is the index for top of the stack.
        if(self.items):
            return self.items[-1]
        else:
            return None

    def size(self):
        """
        Returns the length of list that is representing the stack
        Runtime: O(1), constant time 'coz finding the length of a list happens in constant time
        """
        return len(self.items)

    # if our list == to empty list than it will return true, else false. 
    def isempty(self):
        """
        Returns a boolean value describing whether or not the stack is empty. 

        Testing for equality happens in constant time. 
        """
        return self.items == []

my_stack = Stack()
my_stack.pop()
print(my_stack.items)
my_stack.push('apple')
print(my_stack.items)
# appears to be on the right side of the apple item
# Right side of the list is considered to be the top of the list. Left side = bottom/down of the list.
# And we can add or remove from the top only!
my_stack.push('banana')
print(my_stack.items)
my_stack.push('carrot')
print(my_stack.items)
my_stack.pop()
print(my_stack.items)
print(my_stack.peek())
print(my_stack.size())
print(my_stack.isempty())