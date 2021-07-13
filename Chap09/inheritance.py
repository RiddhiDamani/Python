#!/usr/bin/env python3
# Copyright 2009-2017 BHG http://bw.org/

# Class inheritance is the fundamental part of OOP
# allows you to extend your class by deriving properties/variables and methods from parent classes.


class Animal:

    # no longer providing default values.
    # it is bcz this is going to be the base class and it's going too be inherited in order to be used.
    # bcz of this we need to do extra checking in our getters and setters.
    # we cannot just return a value, we need to check and see whether the value is actually there.
    # so, using exceptions here - exception tries to return a value and if it fails it returns None instead.
    def __init__(self, **kwargs):
        if 'type' in kwargs:
            self._type = kwargs['type']
        if 'name' in kwargs:
            self._name = kwargs['name']
        if 'sound' in kwargs:
            self._sound = kwargs['sound']

    def type(self, t=None):
        if t: self._type = t
        try:
            return self._type
        except AttributeError:
            return None

    def name(self, n=None):
        if n: self._name = n
        try:
            return self._name
        except AttributeError:
            return None

    def sound(self, s=None):
        if s: self._sound = s
        try:
            return self._sound
        except AttributeError:
            return None


# using duck class to inherit base class animal.
class Duck(Animal):
    def __init__(self, **kwargs):
        self._type = 'duck'
        # check if there is a type in the keyword args, if so we delete that
        if 'type' in kwargs:
            del kwargs['type']
        # through super function we call parent class initializer with our kwargs.
        # super() always calls the parent class.
        super().__init__(**kwargs)


# using kitten class to inherit base class animal.
class Kitten(Animal):
    def __init__(self, **kwargs):
        self._type = 'kitten'
        if 'type' in kwargs: del kwargs['type']
        super().__init__(**kwargs)

    # s - string that will identify the target of its predator
    def kill(self, s):
        print(f'{self.name()} will now kill all {s}!')


def print_animal(o):
    if not isinstance(o, Animal):
        raise TypeError('print_animal(): requires an Animal')
    print(f'The {o.type()} is named "{o.name()}" and says "{o.sound()}".')


def main():
    a0 = Kitten(name='fluffy', sound='rwar')
    a1 = Duck(name='donald', sound='quack')
    print_animal(a0)
    print_animal(a1)
    a0.kill('humans')


if __name__ == '__main__': main()
