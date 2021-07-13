#!/usr/bin/env python3
# Copyright 2009-2017 BHG http://bw.org/

from decimal import *  # for money calculation always use the decimal library
x = 7.0
y = 'seven'
z = 'seven "{1:<9}" "{0:>9}"'.format(8,9)
a = 'seven "{1:<09}" "{0:>09}"'.format(8,9)
b = True

m = Decimal('.10')
n = Decimal('.30')

o = m + m + m - n

print('x is {}'.format(x))
print('y is {}'.format(y))
print('z is {}'.format(z))
print('a is {}'.format(a))
print('o is {}'.format(o))
print('b is {}'.format(b))

print(type(x))
print(type(y))
print(type(z))
print(type(a))
print(type(o))
print(type(b))
