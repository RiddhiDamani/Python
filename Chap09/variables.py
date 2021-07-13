#!/usr/bin/env python3
# Copyright 2009-2017 BHG http://bw.org/

# Data may be associated with a class or an object
class Animal:
    # acts as a constructor
    # initializes 3 different variables.
    # these are object variables and they only exists when the object is created from the class.
    # they do not exist in the class itself.

    # creating a mutable (can be changed) variable. this is a class variable and not an object variable.
    # bcz it is defined in a class and not in any methods.
    x = [1, 2, 3]

    def __init__(self, **kwargs):
        self._type = kwargs['type'] if 'type' in kwargs else 'kitten'
        self._name = kwargs['name'] if 'name' in kwargs else 'fluffy'
        self._sound = kwargs['sound'] if 'sound' in kwargs else 'meow'

    def type(self, t=None):
        if t: self._type = t
        return self._type

    def name(self, n=None):
        if n: self._name = n
        return self._name

    def sound(self, s=None):
        if s: self._sound = s
        return self._sound

    def __str__(self):
        return f'The {self.type()} is named "{self.name()}" and says "{self.sound()}".'


def main():
    a0 = Animal(type='kitten', name='fluffy', sound='rwar')
    a1 = Animal(type='duck', name='donald', sound='quack')
    print(a0)
    print(a1)

    # these are object variables. They are bound to the objects and not to the class itself.
    a0._name = 'Joe'  # not a good idea to assign this way. should not access the _ variables directly.
    # _name is a protected member of the class.
    print(a1._name)

    print(a0.x)
    a1.x[0] = 7
    # this x variable is associated with the class and not the object, hence it will be reflected to all the objects.
    # this is encapsulation - major benefit of object oriented programming.
    print(a0.x)


if __name__ == '__main__':
    main()

# if variables are encapsulated that means they belong to the object and not to the class. i.e. type, name, sound
# x is not encapsulated. i.e. it belongs to the class. Hence, it exist i.e. it is exactly the same object
# in every instance of the class. And every object that is created by the class because it only exists in the class.
# so, that makes it not encapsulated.
# you shd never put mutable data in the class.
# setters and getters is one of the principles of encapsulation. One shd never access this variables directly and that's
# why they have underscores in front of them. In many lang. there is a concept of private variables, but python does not
# have it. hence, we use a convention of underscore that means do not touch it. it's protected variables.
# You shd never set them directly from outside of the class methods. hence, we have methods that sets and gets it.
# even when u r printing the variable, use the getter method to do so.
