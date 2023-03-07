## Question 80
## Please write a program to randomly generate a list with 5 numbers,
## which are divisible by 5 and 7 , between 1 and 1000 inclusive.
##
## Hints: Use random.sample() to generate a list of random values.
##
## Solution:

from random import sample

x = sample([x for x in range(1,1001) if x % 5 == 0 and x % 7 == 0],5)
print(x)
