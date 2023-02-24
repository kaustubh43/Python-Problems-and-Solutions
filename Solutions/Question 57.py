# Question 57
# Define a custom exception class which takes a string message as attribute.
#
# Hints:
#
# To define a custom exception, we need to define a class inherited from Exception.
#
# Solution:
class Custom_Exception(Exception):
    """
    This is a custom Exception class
    Attributes -msg
    """
    def __init__(self, message):
        self.message = message


err = Custom_Exception('Something is wrong')
print(err.message)