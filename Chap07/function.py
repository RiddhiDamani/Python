#!/usr/bin/env python3
# Copyright 2009-2017 BHG http://bw.org/

def main():
    x = kitten()
    puppy(4, 5, 9)
    y = 5
    z = [5]
    m = z
    m[0] = 3
    print(id(z))
    print(id(m))
    print(id(y))
    print(m)
    print(z)
    calf(y)
    print(x)
    print(f'in main: y in {y}')


def kitten():
    return 'Meow.'


def puppy(a, b, c=0):
    print(a, b, c)


def calf(a):
    print(id(a))
    a = 3
    print(id(a))  # id gets changed i.e. new object gets created here
    print('value of a is {}'.format(a))


if __name__ == '__main__': main()
