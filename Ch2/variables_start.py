# 
# Example file for variables
#

# Declare a variable and initialize it
f = 0
#print(f)


# re-declaring the variable works
#f = "abc"
#print(f)


# ERROR: variables of different types cannot be combined
# TypeError: can only concatenate str (not "int") to str
# print("this is a string" + 123)
#print("this is a string" + str(123))

# Global vs. local variables in functions
# Inside the function the f gets its own local copy to store the variable value. 
# To affect the local copy and make it a global - you need to declare f as global.
# Telling function that f is now global
def someFunc():
     global f
     f = "def"
     print(f)

someFunc()
print(f)

# del statement deletes the definition of a variable that was previously declared. 
# we can undefine variables in real time by using the del statement
del f 
print(f)

