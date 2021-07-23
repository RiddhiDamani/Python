
class Queue: 

    def __init__(self):
        self.items = []

    def enqueue(self,item):
        """
        Takes in an item and inserts that item into the 0th index of the list that is representing the queue. 
        Runtime:  O(N), linear time 'coz inserting into the 0th index of a list forces all the other items in the list to move one index to the right. 
        """
        self.items.insert(0, item)

    def dequeue(self):
        """
        Returns and removes the front most item of the queue which is represented by the last item in the list. 
        Runtime: O(1), constant time: 'coz indexing to the end of the list happens in constant time. 
        """
        if self.items: 
            return self.items.pop()
        else: 
            return None

    def peek(self):
        """
        Returns last item of the list that repersents the front most item in the queue. 
        Runtime: O(1), constant time 'coz we are just indexing to the last time of the list and returning the value found there. 
        """
        if self.items:
            return self.items[-1]
        else:
            return None

    def size(self):
        """
        Returns the size of the quueue, which represents by length of list:
        Runtime: O(1)
        """
        return len(self.items)

    def isEmpty(self):
        """
        Returns a boolean value expressing where or not the list representing the queue is empty
        Runtime: O(1)
        """
        return self.items == []


queue = Queue()
print(queue.isEmpty())
queue.enqueue('apple')
# gets added to the left of the apple
queue.enqueue('grapes')
print(queue.items)
print(queue.dequeue())
print(queue.peek())