# Question 52
# Define a class named Circle which can be constructed by a radius.
# The Circle class has a method which can compute the area.
#
# Hints:
#
# Use def methodName(self) to define a method.
#
# Solution:
from math import pi


class Circle:
    def __init__(self, rad):
        self.r = rad

    def area(self):
        return pi * self.r ** 2


c1 = Circle(4)
print(c1.area())


