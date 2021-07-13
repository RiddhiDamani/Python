#!/usr/bin/env python3
# Copyright 2009-2017 BHG http://bw.org/

import sys, os, random, datetime


def main():
    v = sys.version_info
    print('Python version {}.{}.{}'.format(*v))
    a = sys.platform
    print(a)
    b = os.name
    print(b)
    c = os.getenv('PATH')
    print(c)
    d = os.getcwd()
    print(d)
    e = os.urandom(25).hex()
    print(e)
    f = random.randint(1, 100)
    print(f)
    g = list(range(25))
    print(g)
    random.shuffle(g)
    print(g)
    now = datetime.datetime.now()
    print(now.year, now.month, now.day)

if __name__ == '__main__':
    main()
