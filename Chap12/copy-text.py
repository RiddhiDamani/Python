#!/usr/bin/env python3
# Copyright 2009-2017 BHG http://bw.org/

# Reading and writing text file is easy in python
# python principle : explicit is always better than implicit
def main():
    infile = open('lines.txt', 'rt')  # opening in read mode and text mode. 'rt' is default mode
    outfile = open('lines-copy.txt', 'wt')  # write + text mode
    for line in infile:
        #outfile.writelines(line)
        # rstrip method strips the line endings from the file; then print to outfile
        print(line.rstrip(), file=outfile)
        print('.', end='', flush=True)  # end='' that prevents print from printing a new line after each dot so that
        # they'll just go across the line and make little progress bar. flush = True : this flushes the output buffer.
    outfile.close() # close the outfile.
    print('\ndone.')


if __name__ == '__main__':
    main()
