# Recursion is when a function that calls itself within its own code. 
# Template: 
# function f() {
#   ...
#   f()
# }
# Recursive functions need to have a breaking condition
# This prevents infinite loops and eventual crashes. 
# Each time the function is called, the old arguments are saved. They are not overwritten. This is called the "Call Stack!" Implemented using stack data structure. 

#The program returns to the statement after the function call was made. If there is no statement, the #program exits the function

# Using recursion to implement power and factorial functions


def power(num, pwr):
    # breaking condition: if we reach zero, return 1
    if pwr == 0:
        return 1
    else:
        return num * power(num, pwr-1)


def factorial(num):
    if (num == 0):
        return 1
    else:
        return num * factorial(num-1)


print("{} to the power of {} is {}".format(5, 3, power(5, 3)))
print("{} to the power of {} is {}".format(1, 5, power(1, 5)))
print("{}! is {}".format(4, factorial(4)))
print("{}! is {}".format(0, factorial(0)))
