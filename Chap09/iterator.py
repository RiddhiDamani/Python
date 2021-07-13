#!/usr/bin/env python3
# Copyright 2009-2017 BHG http://bw.org/

# An iterator is a class that provides a sequence of items, generally used in a loop.
class inclusive_range:

    # constructor that sets up all the variables and it checks the arguments, it checks how many arguments we have.
    # if there is just one - it stops.
    def __init__(self, *args):
        numargs = len(args)
        self._start = 0
        self._step = 1

        if numargs < 1:
            raise TypeError(f'expected at least 1 argument, got {numargs}')
        elif numargs == 1:
            self._stop = args[0]
        elif numargs == 2:
            (self._start, self._stop) = args
        elif numargs == 3:
            (self._start, self._stop, self._step) = args
        else:
            raise TypeError(f'expected at most 3 arguments, got {numargs}')

        # initializes starting point in the iterator.
        self._next = self._start

    # special iterator method - this simply identifies this object as an iterator object
    def __iter__(self):
        return self

    # next function is an iterator in itself.
    def __next__(self):
        if self._next > self._stop:
            raise StopIteration
        else:
            _r = self._next
            self._next += self._step
            return _r


def main():
    for n in inclusive_range(25):
        print(n, end=' ')
    print()


if __name__ == '__main__':
    main()

# Iterator is functionally identical to a generator function. A generator function is easier to implement; but its
# good to know how iterators work!
