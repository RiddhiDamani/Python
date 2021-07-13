#!/usr/bin/env python3
# Copyright 2009-2017 BHG http://bw.org/


# Exceptions are powerful runtime error reporting mechanism commonly used in object oriented systems.
# ValueError: is the token i.e. it is the name of the error that is being generated here.
# sys has lot of constants in it.
import sys
def main():
    print('Hello, World.')
    try:
        # x = int('foo')
        # x = 5 / 3
         x =  5 / 0
    # capturing the error gracefully
    # if you don't catch the errors it will stop the execution of your python script.
    except ValueError:
        print('I caught a ValueError!')
    except ZeroDivisionError:
        print('Don\'t divide by zero')
    # if you don't know which error it is!
    except:
        print(f'unknown error! : {sys.exc_info()[1]}')
    # else block gets executed only if you don't have any errors!
    else:
        print('Good Job!')
        print(x)


if __name__ == '__main__':
    main()
