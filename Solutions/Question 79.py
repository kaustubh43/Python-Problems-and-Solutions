# Question 79
# Please write a program to randomly generate a list with 5 even numbers between 100 and 200 inclusive.
#
# Hints: Use random.sample() to generate a list of random values.
#
# Solution:
from random import sample

print(sample([i for i in range(100, 200) if i % 2 == 0], 5))
