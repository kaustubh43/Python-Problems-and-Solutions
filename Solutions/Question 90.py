# Question 90
# By using list comprehension, please write a program generate a 3x5x8 3D array who's each element is 0.
#
# Hints: Use list comprehension to make an array.
#
# Solution

matrix = [[[0 for col in range(3)] for col in range(5)] for col in range(8)]
print(matrix)
