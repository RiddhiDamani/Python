#!/usr/bin/env python3
# Copyright 2009-2017 BHG http://bw.org/

x = [1, 2, 3, 4, 5]
# for loop is sequencing through the list x and for each item in the list
# it assigns i the value of the item, and then i is used in the print function.
x[2] = 42
for i in x:
    print('i is {}'.format(i))

print('---------------------------')
y = (1, 2, 3, 4, 5)
# cannot reassign values in Tuples
# y[2] = 42
for i in y:
    print('i is {}'.format(i))

print('---------------------------')
z = range(5)
for i in z:
    print('i is {}'.format(i))

print('---------------------------')
a = range(5, 10)
for i in a:
    print('i is {}'.format(i))

print('---------------------------')
b = range(5, 50, 5)
for i in b:
    print('i is {}'.format(i))

print('---------------------------')
c = {'one': 1, 'two': 2, 'three': 3, 'four': 4, 'five': 5}
for i in c:
    print('i is {}'.format(i))

print('---------------------------')
d = {'one': 1, 'two': 2, 'three': 3, 'four': 4, 'five': 5}
for k, v in d.items():
    print('k: {}, v: {}'.format(k, v))

print('---------------------------')
e = (1, 2, 3, 4, 5)
print('e is {}'.format(e))
print(type(e))

print('---------------------------')
f = (1, 'two', 3.0, [4, 'four'], 5)
g = (1, 'two', 3.0, [4, 'four'], 5)
print('f is {}'.format(f))
print(type(f))
print(type(f[1]))
print(id(f))
print(id(g))

# to check if x[0] and y[0] are same object? yes, it is. the literal '1' is same object. hence, it returns yeps
if x[0] is y[0]:
    print('yeps!')
else:
    print('Nopes')

# to check if x is same object as y? no, both are different object, so returns nope.
if x is y:
    print('yeps!')
else:
    print('Nopes')

# checks whether the object x is of type tuple, list
if isinstance(x, tuple):
    print('tuple!')
elif isinstance(x, list):
    print('list!')
else:
    print('Nopes')