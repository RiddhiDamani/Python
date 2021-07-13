#!/usr/bin/env python3
# Copyright 2009-2017 BHG http://bw.org/

print('Hello, World.')


def f1():
    def f2():
        print('this is f2')

    return f2


x = f1()  # assigning function object to var x.; f1() returns the f2 function
x()  # since in python everything is an object, hence var is an object too. Hence, we can call the function f1 by
# calling x. #x() takes in the f2 object and invokes it and thus prints the line
# cannot call f2() directly as it is inside the f1() scope.
# f1() is a wrapper of f2()
