# Question 56
# Write a function to compute 5/0 and use try/except to catch the exceptions.
#
# Hints:
#
# Use try/except to catch exceptions.
#
# Solution:

def zero():
    return 5 / 0


try:
    zero()
except ZeroDivisionError as err:
    print(err)
except Exception as err:
    print(err)
finally:
    print("You're in the finally block")
