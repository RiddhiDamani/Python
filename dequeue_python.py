
class Dequeue: 

    def __init__(self):
        self.items = []

    def add_front(self,item):
        """
        Takes an item as a parameter and inserts it into the 0th index of the list that is representing the Dequeue. 
        Runtime: O(N) 'coz everytime we insert infront of the list, every item needs to shift one position right
        """
        self.items.insert(0, item)

    def add_rear(self, item):
        """
        Takes in an item as a paramater and appends that item to the end of the list that is representing the dequeue.
        Runtime: O(1), appending at the end of list is at constant time
        """
        self.items.append(item)

    def remove_front(self):
        """
        Return and removes the item in the 0th index of the list, which represents the front of the Dequeue. 
        Runtime: O(N), 'coz when we remove item from 0th index, all other items shift one index to left. 
        """
        if self.items:
            return self.items.pop(0)
        else:
            return None

    def remove_rear(self):
        """
        Return and remove the last item from the list, which represent the rear of the list.
        Runtime: O(1)

        """
        if self.items:
           return self.items.pop()
        else: 
            return None

    def peek_front(self):
        """
        Returns the value found at the 0th index of the list, which represents the front of the dequeue. 
        Runtime: O(1), all we are doing is indexing into the list
        """
        if self.items:
            return self.items[0]
        else:
            return None

    def peek_rear(self):
        """
        Returns the value found at the -1st or last index
        Runtime: O(1) - just indexing into a list
        """
        if self.items:
            return self.items[-1]
        else:
            return None

    def size(self):
        """
        Returns the length of the list
        Runtime: O(1)
        """
        return len(self.items)

    def isempty(self):
        """
        Checks to see if the list is empty or not. Returns true or false
        Runtime: O(1)
        """
        return self.items == []


my_dqueue = Dequeue()
my_dqueue.add_front('apple')
print(my_dqueue.items)
my_dqueue.add_rear('banana')
my_dqueue.add_rear('carrot')
print(my_dqueue.items)
print(my_dqueue.remove_front())
print(my_dqueue.remove_rear())
print(my_dqueue.items)
my_dqueue.add_front('apple')
print(my_dqueue.peek_front())
print(my_dqueue.peek_rear())
