#
# Example file for working with classes
#

class myClass():
    # self argument refers to the object itself. It's like the this keyword in javascript. 
    def method1(self):
        print("myClass method1")
    
    def method2(self, someString):
        print("myClass method2 " + someString)

class anotherClass(myClass):
     def method1(self):
        myClass.method1(self)
        print("anotherClass method1")
    
     def method2(self, someString):
        print("anotherClass method2 ")

def main():
    c = myClass()
    c.method1()
    c.method2("Riddhi")
    c2 = anotherClass()
    c2.method1()
    c2.method2("Damani")

if __name__ == "__main__":
    main()
