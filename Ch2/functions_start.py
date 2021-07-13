# Most applications regardless of the programming langugage they are written in are broken up into smaller blocks known as functions. 

# Example file for working with functions
#

# define a basic function
def func1():
    print("I am a function")

# function that takes arguments
def func2(arg1, arg2):
    print(arg1, " ", arg2)


# function that returns a value
def cube(x):
    return x * x * x

# function with default value for an argument
def power(num, x=1):
    result = 1 
    for i in range(x):
        result = result * num
    return result

#function with variable number of arguments
# *args = variable argument list
#  we can combine variable arg list with a set of formal arguments, but variable argument list always has to be the last parameter.
def multi_add(*args):
    result = 0
    for x in args:
        result = result + x
    return result


func1()
print(func1())
# demonstrates that functions themshelves are object that can b passed around to other pieces of Python code. 
print(func1)
func2(10, 20)
print(func2(10,20))
print(cube(3))
print(power(2))
print(power(2,3))
print(power(x=3, num=2))
print(multi_add(10,20,40))
