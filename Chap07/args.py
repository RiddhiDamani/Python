#!/usr/bin/env python3
# Copyright 2009-2017 BHG http://bw.org/

def main():
    kitten('meow', 'grrr', 'purr', 'hello')
    x = ('boww bowww', 'ssshhh', 'hello')
    puppy(*x)


def kitten(*args):
    if len(args):
        for s in args:
            print(s)
    else:
        print('Meow.')


def puppy(*args):
    if len(args):
        for s in args:
            print(s)
    else:
        print('Bowww! Boww!!.')


if __name__ == '__main__': main()
