# Question 48
# Write a program which can filter() to make a list whose elements are even number between 1 and 20 (both included).
#
# Hints:
#
# Use filter() to filter elements of a list. Use lambda to define anonymous functions.
#
# Solution

x = list(filter(lambda k: k % 2 == 0, range(1, 21)))
print(x)
