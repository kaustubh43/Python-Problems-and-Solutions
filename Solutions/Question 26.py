## Question 26:
## Define a function which can compute
## the sum of two numbers.
##
## Hints: Define a function with two numbers as arguments.
## You can compute the sum in the function and return the value.
##
## Solution
##


def summation(*args):
    total = 0
    print(list(args))
    for k in args:
        total += k
    return total

print(summation(1))
