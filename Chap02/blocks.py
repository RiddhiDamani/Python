#!/usr/bin/env python3
# Copyright 2009-2017 BHG http://bw.org/

x = 5
y = 42

if x < y:   # colon : indicates end of the condition
    print('x < y: x is {} and y is {}'.format(x, y))
else:
    print('x is not < than y')

print('Something else')

if x > y:
    print('x > y: x is {} and y is {}'.format(x, y))
elif x < y:
    print('x < y: x is {} and y is {}'.format(x, y))
elif x == y:
    print('x == y: x is {} and y is {}'.format(x, y))
else:
    print('do something else')

if x == 5:
    print('do 5 stuff')
elif x == 6:
    print('do 6 stuff')
elif x == 7:
    print('do 7 stuff')
else:
    print('do other things')