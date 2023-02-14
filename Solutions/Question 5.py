## Question:
## Define a class which has at least two methods:
## getString: to get a string from console input
## printString: to print the string in upper case.
## Also please include simple test function to test the class methods.

class StringOutput:
    def __init__(self):
        self.s = ""


    def getString(self):
        self.s = input("Enter the string ")


    def printString(self):
        print(self.s)


obj1 = StringOutput()
obj1.getString()
obj1.printString()

