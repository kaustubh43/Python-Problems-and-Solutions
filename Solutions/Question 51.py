# Define a class named American and its subclass NewYorker.
#
# Hints:
#
# Use class Subclass(ParentClass) to define a subclass.
#
# Solution:

class American:
    @staticmethod
    def printNationality():
        print("I'm an American")


class NewYorker(American):
    @staticmethod
    def printNationality():
        super().printNationality()
        print("I'm an NewYork")


obj = NewYorker()
obj.printNationality()

