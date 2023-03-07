## Question 81
## Please write a program to randomly print a
## integer number between 7 and 15 inclusive.
##
## Hints: Use random.randrange() to a random integer in a given range.
##
## Solution:

from random import randrange

MIN_NUM = 7
MAX_NUM = 15
x = randrange(MIN_NUM, MAX_NUM + 1)
print(x)
