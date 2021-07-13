#!/usr/bin/env python3
# Copyright 2009-2017 BHG http://bw.org/

def main():
    seq = range(11)
    seq2 = [x * 2 for x in seq]
    seq3 = [x for x in seq if x % 3 != 0]  # we get only the elements that are not divisible by 3
    seq4 = [(x, x ** 2) for x in seq]
    print_list(seq)
    print_list(seq2)
    print_list(seq3)
    print_list(seq4)
    from math import pi
    seq5 = [round(pi, i) for i in seq]
    print_list(seq5)
    # can also create a dictionary
    seq6 = {x: x**2 for x in seq}
    print(seq6)
    # can also create a set
    seq7 = {x for x in 'superduper' if x not in 'pd'}
    print_list(seq7)


def print_list(o):
    for x in o:
        print(x, end=' ')
    print()


if __name__ == '__main__': main()
