# Python Object Oriented Programming by Joe Marini course example
# Using data classes to represent data objects
# In Python 3.7 - Python has provided Data classes that provides a decorator and functions for automatically adding generated special methods such as init() and repr()

from dataclasses import dataclass

# python will automatically create a init function out of the below definition and have the constructor and attributes defined for that class. 
@dataclass
class Book:
    # str = type hints. required for data classes to work. But, their type is actually not enforced as Python has to be flexible. 
    title : str
    author : str
    pages : int
    price : float

    def bookinfo(self):
        return f"{self.title}, by {self.author}"

# create some instances
b1 = Book("War and Peace", "Leo Tolstoy", 1225, 39.95)
b2 = Book("The Catcher in the Rye", "JD Salinger", 234, 29.95)
b3 = Book("War and Peace", "Leo Tolstoy", 1225, 39.95)

# access fields
print(b1.title)
print(b2.author)

# TODO: print the book itself - dataclasses implement __repr__
print(b1)

# TODO: comparing two dataclasses - they implement __eq__
print(b1 == b3)

# TODO: change some fields
b1.title = "Anna"
b1.pages = 864
print(b1.bookinfo())