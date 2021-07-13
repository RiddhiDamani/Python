#!/usr/bin/env python3
# Copyright 2009-2017 BHG http://bw.org/

class Duck:
    # class definition
    # we have data in form of the variables
    sound = 'Quack quack.'
    movement = 'Walks like a duck.'

    # we have functions in form of the below method definition
    # first parameter of a method is always self.
    # self is not a keyword, we can name it whatever we want it to be.
    # self is a reference to the object (not the class to the object)
    # and so when an object is created from the class, self will reference that object
    # And then everything that references, anything defined in the class is dereference off itself to get the
    # instantiated object version of it.
    # period operator is used to dereference the object.
    # same is true outside of the class.
    def quack(self):
        print(self.sound)

    def move(self):
        print(self.movement)


def main():
    # defined the variable donald from the class Duck
    donald = Duck()
    # invoke object method quack on the object donald.
    # the dot operator dereferences the object so that you can get to the method in this case quack.
    donald.quack()
    donald.move()


if __name__ == '__main__': main()
