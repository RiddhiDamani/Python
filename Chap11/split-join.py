#!/usr/bin/env python3
# Copyright 2009-2017 BHG http://bw.org/


# Python allows u to easily split and join strings based on separator characters.
s = 'This is a long string with a bunch of words in it.'
l = s.split()
print(s)
print(s.split())
print(s.split('i'))

s2 = ':'.join(l)
s3 = '--'.join(l)
print(s2)
print(s3)
