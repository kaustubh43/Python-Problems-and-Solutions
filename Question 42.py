## Question 42
## With a given tuple (1,2,3,4,5,6,7,8,9,10), write a
## program to print the first half values in one line and
## the last half values in one line.
##
##
## Hints:
##
## Use [n1:n2] notation to get a slice from a tuple.
##
## Solution 

def gen_li(x):
    li = [a**2 for a in range(1,x+1)]
    return li

x = tuple(gen_li(20))
print(x)
