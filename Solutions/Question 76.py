# Question 76
# Please write a program to output a random even number between 0 and 10 inclusive using random module and list comprehension.
#
# Hints: Use random.choice() to a random element from a list.
#
# Solution:

from random import choice

print(choice([i for i in range(1, 11)]))

