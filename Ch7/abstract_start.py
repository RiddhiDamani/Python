# Python Object Oriented Programming by Joe Marini course example
# Using Abstract Base Classes to enforce class constraints
# Abstract classes - Imp Point: You cannot create an instance of the abstract classes. 
# Subclasses of the abstract classes provide concrete implementations. Make sure there are some methods of the abstract class that the subclasses have to implement. 
# Abstract base class can be very useful tool for enforcing a set of constraints on the consumers of the class. 

# ABC = abstract base class
from abc import ABC, abstractmethod

class GraphicShape(ABC):
    def __init__(self):
        super().__init__()

    @abstractmethod
    def calcArea(self):
        pass


class Circle(GraphicShape):
    def __init__(self, radius):
        self.radius = radius

    def calcArea(self):
        return 3.14 * (self.radius ** 2)


class Square(GraphicShape):
    def __init__(self, side):
        self.side = side

    def calcArea(self):
        return self.side * self.side

#g = GraphicShape()

c = Circle(10)
print(c.calcArea())
s = Square(12)
print(s.calcArea())
