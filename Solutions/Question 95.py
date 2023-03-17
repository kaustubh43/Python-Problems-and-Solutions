## Define a class Person and its two child classes:
##
## Male and Female. All classes have a method "getGender"
##
## which can print "Male" for Male class and "Female" for Female class.
##
## Hints: Use Subclass(Parentclass) to define a child class.
##
## Solution:
class Person:
    def getGender(self):
        print('Unknown')


class Male(Person):
    def getGender(self):
        print('Male')


class Female(Person):
    def getGender(self):
        print('Female')

boy = Male()
girl = Female()
boy.getGender())
girl.getGender())
