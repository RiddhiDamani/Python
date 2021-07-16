# Python Object Oriented Programming by Joe Marini course example
# Using instance methods and attributes


class Book:
    # the "init" function is called when the instance is
    # created and ready to be initialized
    def __init__(self, title, author, pages, price):
        self.title = title
        # TODO: add properties
        # Each of these attributes are called as Instance attributes 'coz the value that it holds is unique to each instance of the object that it's declared on. Same applies to instance methods
        self.author = author
        self.pages = pages
        self.price = price
        # this property cannot be seen outside of the class. 
        self.__secret = " This is a secret attibute"

    # TODO: create instance methods
    # Every instance method takes in the object(self) as the first parameter. 
    def getprice(self, ):
        if hasattr(self, "_discount"):
            return self.price - (self.price * self._discount)
        else:
            return self.price

    def setdiscount(self, amount):
        # _ before a variable name gives other developers a hint that this attribute is considered internal to the class and should not be accessed from outside the class logic. 
        # _ is intended to be used only by the class (attibute/method)
        # __ double underscore : at the start of the attribute of the method name - the python interpreter will change the name of that attr or method so that the other class will get an error if they try to access it. self.__secret property cannot be seen outside of the class.  However this is not a perfect mechanism - so the way Python does this is by prefixing the name of the attribute with the class names. This is called Name Mangling. Reason for doing this: avoid subclasses from inadvertently overriding the attribute, but other classes can simply subvert this simply by using the class name. 
        self._discount = amount

# TODO: create some book instances
b1 = Book("War and Peace", "Leo Tolstoy", 1225, 39.95)
b2 = Book("The Catcher in the Rye", "JD Salinger", 234, 29.95)

# TODO: print the price of book1
print(b1.getprice())

# TODO: try setting the discount
print(b2.getprice())
b2.setdiscount(0.25)
print(b2.getprice())

# TODO: properties with double underscores are hidden by the interpreter
#print(b2.__secret)
print(b2._Book__secret)

# __ can be used to make sure that the sub classes dont use the same name for an attribute that you have already used. 