#!/usr/bin/env python3
# Copyright 2009-2017 BHG http://bw.org/

import platform


def main():
    message()
    x = cheer(5)
    print(x)


def message():
    print('This is python version {}'.format(platform.python_version()))
    if True:
        print('hello world')  # this is at next level and it is a comment
    else:  # this is another comment
        print('nothing to print')


def cheer(n):
    'return a string with a silly cheer based on n'
    if n <= 1:
        return "Hurrah!"
    else:
        return "Hip " + cheer(n - 1)


if __name__ == '__main__': main()
