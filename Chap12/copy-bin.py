#!/usr/bin/env python3
# Copyright 2009-2017 BHG http://bw.org/

def main():
    infile = open('berlin.jpg', 'rb') # read + binary
    outfile = open('berlin-copy.jpg', 'wb')
    while True:
        # to copy a binary file we use the read and write methods of the file object.
        # size of the buffer - 10KB = 10240 bits
        buf = infile.read(10240)
        if buf:
            outfile.write(buf)
            print('.', end='', flush=True)
        else:
            break
    outfile.close()
    print('\nDone.')


if __name__ == '__main__':
    main()
