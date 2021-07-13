#!/usr/bin/env python3
# Copyright 2009-2017 BHG http://bw.org/

s = 'Hello, World.'
print(repr(s))  # repr() method prints the string itself. it is string representation for a value or of an object


# repr() function will either print the return from the repr method of the class or if it does not have that it'll
# just print this, we just change this

class bunny:
    def __init__(self, n):
        self._n = n

    # allows us to customize text how it's gonna represent in different context.
    def __repr__(self):
        return f'repr: the number of bunnies is {self._n}'

    def __str__(self):
        return f'str: the number of bunnies is {self._n}'


x = bunny(47)
print(repr(x))  # it is a bunny object and gives you the memory address.
print(ascii(x))  # ascii works just like repr method except it'll escape any special characters.
print(chr(128406))  # unicode position for live long and prosper hand emoji. represents the character of a number
print(ord('🖖'))  # ord gives you the number of a character

m = (1, 2, 3, 4, 5)
s = (6, 7, 8, 9, 10)
n = len(m)
o = list(reversed(m))  # gives the reversed object string - can create a list out of that of the tuple x.
p = sum(m)
# p = max(m) # largest value in the collection
# p = min(m) # smallest value in the collection
q = any(m) # if any of the items are true. (0,0,0) returns false but, (1, 0,0) returns true
q = all(m) # checks all items - if all true then returns true else returns false.
t = zip(m , s) # zip returns an iterator with 2 values in each item
print(m)
print(n)
print(o)
print(p)
for a, b in t:
    print(f'{a} - {b}')


w = ('cat','dog', 'rabbit')
# enumerate gives us 2 values an index and a value
for i, v in enumerate(w) :
    print(f'{i}: {v}')

# type function operates on the object and returns the class of that object or type of that object
x = 42
y = type(x)
y = isinstance(x, int)
print(x)
print(y)

# id represents a unique number for a particular object
# if you have the same objects then the number will be the same
# different objects have different ids.
r = id(x)
print(r)

x=abs(int(float(-4.5+3.2)))
print(x-1j)