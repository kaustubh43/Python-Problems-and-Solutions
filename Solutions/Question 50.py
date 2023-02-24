# Question 50
# Define a class named American which has a static method called printNationality.
#
# Hints: Use @staticmethod decorator to define class static method.
#
# Solution

class American:
    @staticmethod
    def printNationality():
        print("I'm an American")


obj = American()
obj.printNationality()
American.printNationality()
