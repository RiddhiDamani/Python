#!/usr/bin/env python3
# Copyright 2009-2017 BHG http://bw.org/

# Strings are the first class objects in Python3.
# The below is a literal string. You can call methods on it.
# A string is immutable - it cannot be changed. So, when we use one of the below transformation methods,
# the return string is a different object.
print('Hello, World.')
print('Hello, World.'.upper())
print('Hello, World.'.swapcase())
print('Hello, World. {} '.format(42 * 7))

s = 'Hello Riddhi'
print(s.upper())


# str is a built-in string class in Python3
class MyString(str):
    def __str__(self):
        return self[::-1]


x = MyString('Hello Coder! ')
print(x)

# .upper() - prints all upper case letters
# .lower() - prints all lower case letters
# .capitalize() - capitalizes just the first letter of the string and makes everything else lowercase
# .title() - capitalizes the first letter of every word
# .swapcase() - swap the case of every letter. i.e. lower to upper and upper to lower
# .casefold() - makes everything lower case. casefold is more aggressive and it removes all distinction even in unicode.


s1 = 'Helo Coder!'
s2 = s1.upper()
# both are different objects
print(id(s1))
print(id(s2))


s1 = 'Helo Coder!'
s2 = 'How are you?'
# Literal strings can be concatenated like this.
s3 = s1 + ' ' + s2
s4 = 'Riddhi S. '  ' ' 'Damani'
print(s3)
print(s4)

#format() method is used to format the strings
x = 42
y = 73
print('the number is {} {}'.format(x, y))
print('the number is {xx} {bb}'.format(xx = x, bb = y))
print('the number is {1} {0} {0}'.format(x, y))

# formatting instructions are preceded by colon ; number of spaces including the value. I can also have leading zero.
# sign takes up one of the 5 positions.
print('the number is {0:<5} {1:+05}'.format(x, y))
print(f'the number is {x}')


y = 42 * 747 * 100
print('the number is {:,}'.format(y).replace(',','.'))
# can specify fixed number of decimal places
# 3 places to the right of decimal point.
print('the number is {:.3f}'.format(y))

z = 42
print('the number is {:b}'.format(z))
print(f'the number is {x:.3f}')