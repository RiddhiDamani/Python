# Python Object Oriented Programming by Joe Marini course example
# Understanding multiple inheritance
# One can inherit attributes/methods from more than one class..
# Need to use carefully. 
# What happens if the 2 super classes define the same attribute? Ans: Class A - Why is that? When you access an attribute or call a method in Python, the Python interpreter uses a method resolution order to look it up in the class. So, look up starts from the current class i.e. Class C here and does see the name attribute - so, python interpreter then looks up to the superclasses in which they are defined i.e. from left to right. Since, class A is first, hence we can see class A as o/p. Change the order of class and test?

class A:
    def __init__(self):
        super().__init__()
        self.foo = "foo"
        self.name = "Class A"


class B:
    def __init__(self):
        super().__init__()
        self.bar = "bar"
        self.name = "Class B"


class C(B, A):
    def __init__(self):
        super().__init__()

    def showprops(self):
        print(self.foo)
        print(self.bar)
        print(self.name)



c = C()
c.showprops()
# Using __mro__ method resolution order - can check the order of class methods. 
print(C.__mro__)