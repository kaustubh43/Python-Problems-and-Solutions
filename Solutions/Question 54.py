# Question 54
# Define a class named Shape and its subclass Square.
# The Square class has an init function which takes a length as argument.
# Both classes have a area function which can print the area of the shape where Shape's area is 0 by default.
#
# Hints:
#
# To override a method in super class, we can define a method with the same name in the super class.
#
# Solution:
class Shape:
    def __init__(self):
        pass

    def area(self):
        return 0


class Square(Shape):
    def __init__(self, length):
        super().__init__()
        self.length = length

    def area(self):
        return self.length * self.length


s1 = Square(5)
print(s1.area())

