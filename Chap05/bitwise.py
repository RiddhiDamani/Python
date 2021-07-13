#!/usr/bin/env python3
# Copyright 2009-2017 BHG http://bw.org/

x = 0x0a  # initialized using hexadecimal literal numbers
y = 0x01
# z = x & y
# z = x | y
# z = x ^ y # Ex-OR = only if one or the other, not both, operands have that bit set.  i.e. 1 n 0 = 1, but 1 n 1 = 0
z = x << y  # Shift left operator - bits gets shifted left by 1.
z = x >> y  # Shift right operator - bits gets shifted right by 1.


# 02 means 2 characters wide; x is for hexadecimal display of an integer value
print(f'(hex) x is {x:02x}, y is {y:02x}, z is {z:02x}')  # printed using hexadecimal form - 02x gives us 2 character
# str

# 08 means 8 characters wide; b is for binary representation of the value
print(f'(bin) x is {x:08b}, y is {y:08b}, z is {z:08b}')  # printed using binary form
