# Question 53
# Define a class named Rectangle which can be constructed by a length and width.
# The Rectangle class has a method which can compute the area.
#
# Hints:
#
# Use def methodName(self) to define a method.
#
# Solution:


class Rectangle:
    def __init__(self, le, b):
        self.le = le
        self.b = b

    def area(self):
        return self.le * self.b


r1 = Rectangle(5, 4)
print(f'{r1.area()=}')
