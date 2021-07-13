#!/usr/bin/env python3
# Copyright 2009-2017 BHG http://bw.org/

# A function that is associated with a class is called a method.
# This provides the interface to the class and its objects.
class Animal:
    def __init__(self, **kwargs):
        self._type = kwargs['type'] if 'type' in kwargs else 'kitten'
        self._name = kwargs['name'] if 'name' in kwargs else 'fluffy'
        self._sound = kwargs['sound'] if 'sound' in kwargs else 'meow'

    # serves as both getter and the setter.
    # first arg is self and that makes this is a method, not just a plain function.
    def type(self, t=None):
        # if there is a value associated with t variable, then it will set to  the type variable.
        # if there is no t value, then this if will fail and it'll just return the value of type.
        if t: self._type = t
        # else it will set value none and return it. t has default value of None.
        # this makes it a setter and getter method.
        return self._type

    def name(self, n=None):
        if n: self._name = n
        return self._name

    def sound(self, s=None):
        if s: self._sound = s
        return self._sound

    # special named method which provides string representation of the object
    # and it allows us to print it with simply this print and the object like that.
    # without needing to have a special function just for the print statement.
    def __str__(self):
        return f'The {self.type()} is named "{self.name()}" and says "{self.sound()}".'


def main():
    a0 = Animal(type='kitten', name='fluffy', sound='rwar')
    a1 = Animal(type='duck', name='donald', sound='quack')
    # set the variable sound using the setter getter.
    a0.sound('bark')
    print(a0)
    print(a1)


if __name__ == '__main__': main()

# Methods are the primary interface for classes and objects.
# They work exactly like functions except they are bound to the object through their first arguments
# commonly named self.
