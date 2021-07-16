# Python Object Oriented Programming by Joe Marini course example
# Using Abstract Base Classes to implement interfaces
# Combination of abstract base classes + multiple inheritance = Interfaces 
# Think of interface as a promise : By implementing an interfac, a particular class makes a promise or a contract to provide a certain kind of behavior or capability. 

from abc import ABC, abstractmethod

# this new JSONify class serves as the interface.
class JSONify(ABC):
    
    @abstractmethod
    def toJSON(self):
        pass

class GraphicShape(ABC):
    def __init__(self):
        super().__init__()

    @abstractmethod
    def calcArea(self):
        pass


class Circle(GraphicShape, JSONify):
    def __init__(self, radius):
        self.radius = radius

    def calcArea(self):
        return 3.14 * (self.radius ** 2)

    def toJSON(self):
        return f"{{\"Circle\" : {str(self.calcArea())} }}"

c = Circle(10)
print(c.calcArea())
print(c.calcArea())
print(c.toJSON())