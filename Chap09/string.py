#!/usr/bin/env python3
# Copyright 2009-2017 BHG http://bw.org/

# str is a built-in class
# RevStr is inheriting from str class and
# we are overriding the string representation method to instead of returning the string itself, to
# return a slice of the string where the step goes backwards. And so, this will reverse the string.
class RevStr(str):
    def __str__(self):
        return self[::-1]


def main():
    hello = RevStr('Hello, World.')
    print(hello)


if __name__ == '__main__':
    main()
