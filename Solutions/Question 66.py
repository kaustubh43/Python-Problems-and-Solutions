# Question 64
# Write a program to compute 1/2+2/3+3/4+...+n/n+1 with a given n input by console (n>0).
#
# Example: If the following n is given as input to the program:
#
# 5
#
# Then, the output of the program should be:
#
# 3.55
#
# In case of input data being supplied to the question, it should be assumed to be a console input.
#
# Hints: Use float() to convert an integer to a float
#
# Solution:

def fib(x):
    a, b = 0, 1
    for i in range(x):
        yield a
        a, b = b, a + b



y = fib(50)
for k in y:
    print(k)
