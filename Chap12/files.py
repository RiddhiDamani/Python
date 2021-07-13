#!/usr/bin/env python3
# Copyright 20

# Python provides the open() function for opening file
# open() opens the file in read-only default mode.
def main():
    # open the file - open() returns a file object. It takes the file name and opens that file and returns
    # a file object. The file object itself is a iterator, and so we can use a for loop and get one line at a time
    # without having to buffer the entire file in memory

    f = open('lines.txt', 'w') # opens it in write mode. a: append mode, r: read -only, r+ allows to read and write.

    # read each line by line, stripping the new lines off the end of each line and display them
    # rstrip() - each of the line is returned as a string and the string class has an R-strip method
    # which will strip any white space, incl. new lines from the end of the line.
    for line in f:
        print(line.rstrip())


if __name__ == '__main__':
    main()
