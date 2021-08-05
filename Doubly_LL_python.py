from typing import Counter


class DLLNode:

    # defined attributes for our node class
    def __init__(self, data):
        self.data = data
        # Since the new node does not point to anything. 
        self.next = None
        self.previous = None

    def __repr__(self):
        return "DLLNode object: data = {}".format(self.data)

    def get_data(self):
        """
        Returns the self.data attribute
        """
        return self.data

    def set_data(self, new_data):
        """
        Replace the existing value of the self.data attribute with new_data parameter
        """
        self.data = new_data

    def get_next(self):
        """
        Return the self.next attribute
        """
        return self.next

    def set_next(self, new_next):
        """
        Replace the existing value of the self.next attribute with new_next parameter
        """
        self.next = new_next

    def get_previous(self):
        """
        Return the self.previous attribute
        """
        return self.previous

    def set_previous(self, new_previous):
        """
        Replace the existing value of the self.previous attribute with new_previous parameter
        """
        self.previous = new_previous


class DLL:
    def __init__(self):
        self.head = None

    def __repr__(self):
        return "<DLL Object: Head=>".format(self.head)

    def is_empty(self):
        return self.head is None

    def size(self):
        """
        Traverses the Linked list and returns an integer value representing the number of nodes in the linked list.

        Runtime: O(N): 'coz we have to visit every node in the linked list inorder to calculate the size of the linked list
        """
        size = 0
        if self.head is None:
            return 0
        
        current = self.head
        while current is not None: # while there are still nodes left to count
            size += 1
            current = current.get_next()

        return size

    def search(self, data):
        """
        Traverses the Linked list and returns True if the data searched for is present in one of the nodes. Otherwise, it returns False.
       
       Time complexity: O(n) because in the worst case we have to traverse all the nodes. 
        """
        if self.head is None:
            return "Linked list is empty. No nodes to search"

        # if there are any nodes in the LL then, self.head will not be none, it will be a node object.
        current = self.head    
        while current is not None:
            # The Node's data matches what we are looking for
            if current.get_data() == data:
                return True
            # The Node's daya doesn't match what we are looking for
            else:
                current = current.get_next()
            
        return False

    def add_front(self, new_data):
        """
        Add a node whose data is the new_data argument to the front of the Linked List!
        """
        temp = DLLNode(new_data)
        temp.set_next(self.head)
        # temp refers to the new node that we are inserting here! 
        if self.head is not None:
            self.head.set_previous(temp)

        self.head = temp

    """
    Edge Cases: 1) Empty Linked List 2) Target data not found 3) If the node is the first node 4) Removing non-first nodes. 

    Removes the first occurence of a node that contains the data argument as its self.data attribute. Returns Nothing. 

    Time Complexity: O(n)
    """
    def remove(self, data):
        if self.head is None:
            return "Linked list is empty. No nodes to remove"
        
        current = self.head
        found = False
        while not found:
            if current.get_data() == data:
                found = True
            else:
                if current.get_next() is None:
                    return "A node with that data value is not present."
                else:
                    current = current.get_next()

        if current.previous is None:
            self.head = current.get_next()
        else:
            current.previous.set_next(current.get_next())
            current.next.set_previous(current.get_previous())


node = DLLNode('apple')
#print(node.get_data())
node.set_data('chikku')
#print(node.get_data())
node2 = DLLNode('banana')
node.set_next(node2)
print(node.get_next())
node2.set_previous(node)
print(node2.get_previous())


one = DLLNode(1)
two = DLLNode(2)
one.set_next(two)
one.set_previous(one)
print(one.get_next())
print(one.get_previous())

dll = DLL()
print(dll.size())
dll.add_front(1)
print(dll.head)
print(dll.head.previous)
print(dll.head.next)
dll.add_front(2)
print(dll.head)
print(dll.head.previous)
print(dll.head.next)
print(dll.head.next.next)
dll.remove(2)
print(dll.head)