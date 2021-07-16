# Python Object Oriented Programming by Joe Marini course example
# Basic class definitions


# TODO: create a basic class
class Book:
    #  pass statement is used as a placeholder for future code.
    #  When the pass statement is executed, nothing happens, but you avoid getting an error when empty code is not allowed.
    # Empty code is not allowed in loops, function definitions, class definitions, or in if statements.
    # pass

    # overiding built in init function
    # init function is one of the special function of python when working with classes. 
    # when we create an instance of the class i.e. b1 = Book(), the init function is called to initialize the new object with information. And it is called before any other functions that you have defined on the class. This is specifically an initializer function and not the constructor func like Java or C. 
    # the object is already been created or constructed before the initializer func is called. So, you know that it is safe to start initializing attributes. 
    # whenever we call a method on a Python object, the object itself gets automatically passed in as the first argument. The word 'self' is just the naming convention. We dont need to call it that, but mmost Python programs follow this convention.
    def __init__(self, title):
        # creating a new attibute on an object called title and it is being used to hold the title of the book. 
        self.title = title

# TODO: create instances of the class
b1 = Book("Brave new world")
b2 = Book("War and Peace")

# TODO: print the class and property
# accessing the attribute of an object using the dot property
print(b1)
print(b1.title)