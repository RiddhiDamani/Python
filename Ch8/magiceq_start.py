# Python Object Oriented Programming by Joe Marini course example
# Using the __str__ and __repr__ magic methods


class Book:
    def __init__(self, title, author, price):
        super().__init__()
        self.title = title
        self.author = author
        self.price = price

    # TODO: the __eq__ method checks for equality between two objects. Magic method __eq__ is called on your object when it is being compared with another object. 
    # adding equality check behavior to our book object
    def __eq__(self, value):
        if not isinstance(value, Book):
            raise ValueError("Can't compare a Book to a non-Book")
        return (self.title == value.title and self.author == value.author and self.price == value.price)

    # TODO: the __ge__ establishes >= relationship with another obj
    def __ge__(self, value):
         if not isinstance(value, Book):
            raise ValueError("Can't compare a Book to a non-Book")
         return self.price >= value.price

    # TODO: the __lt__ establishes < relationship with another obj
    def __lt__(self, value):
         if not isinstance(value, Book):
            raise ValueError("Can't compare a Book to a non-Book")
         return self.price < value.price

b1 = Book("War and Peace", "Leo Tolstoy", 39.95)
b2 = Book("The Catcher in the Rye", "JD Salinger", 29.95)
b3 = Book("War and Peace", "Leo Tolstoy", 39.95)
b4 = Book("To Kill a Mockingbird", "Harper Lee", 24.95)

# TODO: Check for equality
# Reason it is false is 'coz it does not compare object's attributes, it compares the instance of Book object. Both these objects are different in the memory storage hence returning false, they aint equal.
print(b1 == b3)
print(b1 == b2)
#print(b1 == 42)

# TODO: Check for greater and lesser value
print(b2 >= b1)
print(b2 < b1)

# TODO: Now we can sort them too
books = [b1, b3, b2, b4]
# built-in sort method
books.sort()
# sorting based on the price of each books. default sorted in less than order. 
print([book.title for book in books])