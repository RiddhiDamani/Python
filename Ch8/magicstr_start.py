# Python Object Oriented Programming by Joe Marini course example
# Using the __str__ and __repr__ magic methods

# Good idea to define a repr function for classes that you create inorder to make debugging easier.  
class Book:
    def __init__(self, title, author, price):
        super().__init__()
        self.title = title
        self.author = author
        self.price = price

    # TODO: use the __str__ method to return a string. user friendly string representation of an object. Usually intended to be displayed for the user. 
    # __ denotes pythons magic methods here for the str
    def __str__(self):
        return f"{self.title} by {self.author}, costs {self.price}"


    # TODO: use the __repr__ method to return an obj representation. Develop more developer facing string that ideally can be used to recreate the object. Common usage: Debuggin purposes. Displays a lot of detailed information for the developer with regards to the object. 
    def __repr__(self):
        return f"title={self.title}, author={self.author}, price={self.price}"

b1 = Book("War and Peace", "Leo Tolstoy", 39.95)
b2 = Book("The Catcher in the Rye", "JD Salinger", 29.95)

print(b1)
print(b2)
print(str(b1))
print(repr(b2))
