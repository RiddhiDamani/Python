#!/usr/bin/env python3
# Copyright 2009-2017 BHG http://bw.org/

class Animal:

    # special class method name call init - special name for a class function which operates as an
    # initializer or a constructor - first arg is always self, apart from it we are passing 3 other arguments here.
    # self makes this as an object method 'coz this self points at the object.
    # 3 parameters : type, name and sound are used to initialize object variables.
    def __init__(self, type, name, sound):
        # these are object variables bcz they are never initialized until after the object is defined.
        # object variables all have an underscores at the beginning of their name : ex: _type
        # this is traditional and this discourages users of the object from accessing these
        # variables directly.
        self._type = type
        self._name = name
        self._sound = sound

    # alternative approach
    # def __init__(self, **kwargs):
    # order of the arguments can be made random in this way.
    # also we can give a default value in this case.
    #    self._type = kwargs['type'] if 'type' in kwargs else 'kitten'
    #    self._name = kwargs['name'] if 'name' in kwargs else 'fluffy'
    #    self._sound = kwargs['sound'] if 'sound' in kwargs else 'rwar'

    # Instead we have accessors or getters which simply returns the value of those object variables.
    def type(self):
        return self._type

    def name(self):
        return self._name

    def sound(self):
        return self._sound


def print_animal(o):
    if not isinstance(o, Animal):
        raise TypeError('print_animal(): requires an Animal')
    # when we print the animals, we use those getters inorder to access those variables.
    print('The {} is named "{}" and says "{}".'.format(o.type(), o.name(), o.sound()))


def main():
    # a0 and a1 are 2 objects from the animal class
    # and I am initializing it with various parameters - type of the animal, name of the animal and sound.
    a0 = Animal('kitten', 'fluffy', 'rwar')
    # a0 = Animal(type = 'kitten', name = 'fluffy', sound = 'rwar')
    a1 = Animal('duck', 'donald', 'quack')

    # calling print_animal function that accepts an animal object and prints the animal
    print_animal(a0)
    print_animal(a1)

    # calling it directly from the constructor - from the class without creating an intermediary object.
    # function parameters work exactly like assignments in Python.
    print_animal(Animal('velociraptor', 'veronica', 'hello'))
    print_animal(Animal())  # gives the default object


if __name__ == '__main__':
    main()

# object is an instance of the class
# an object is created by calling the class as if it were a function
# constructor is used to initialize the object
