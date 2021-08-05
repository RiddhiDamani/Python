from typing import Counter, ForwardRef


class SLLNode:

    # defined attributes for our node class
    def __init__(self, data):
        self.data = data
        # Since the new node does not point to anything. 
        self.next = None

    def __repr__(self):
        return "SLLNode object: data = {}".format(self.data)

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

class SLL:
    def __init__(self):
        self.head = None

    def __repr__(self):
        return "SLL Object: Head={}".format(self.head)

    def is_empty(self):
        #if self.head == None:
        #    return True
        #else:
        #    return False
        # Other way of doing it is as shown below. Other way of doing it: self.head == None
        # Returns true if the linked list is empty. Otherwise returns false.
        return self.head is None

    def add_front(self, new_data):
        """
        Add a node whose data is the new_data argument to the front of the Linked List!
        """
        temp = SLLNode(new_data)
        temp.set_next(self.head)
        self.head = temp

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

    """
    Edge Cases: 1) Empty linked list 2)Target data not found 3) if the node to remove is the 1st node
    4) Removing node elsewhere (Removing non-first nodes)

    Removes the first occurrence of a Node that contains the data argument as its self.data variable. Returns nothing. 

    Time Complexity: O(n) becuase in the worst case we have to visit every node before we find the one we need to remove.  
    """
    def remove(self, data):
        if self.head is None:
            return "Linked list is empty. No nodes to remove."

        current = self.head
        previous = None
        found = False

        while not found:
            if current.get_data() == data:
                found = True
            else:
                if current.get_next() == None:
                    return "A node with that data value is not present"
                else:
                    previous = current
                    current = current.get_next()
        
        if previous is None:
            self.head = current.get_next()
        else:
            previous.set_next(current.get_next())



sll = SLL()
print(sll.size())
print(sll.is_empty())
sll.add_front('apple')
sll.add_front('berry')
sll.add_front('cherry')
print("Search2:", sll.search('apple'))
sll.remove('cherry')
print("Head: ", sll.head)
print("Next: ", sll.head.next)
print(sll.size())

node = SLLNode(5)
sll.head = node
print(sll.is_empty())

sll.add_front('berry')
print(sll.head)

#node = SLLNode('apple')
#print(node.get_data())
#node.set_data('chikku')
#print(node.get_data())
#node2 = SLLNode('banana')
#node.set_next(node2)
#print(node.get_next())