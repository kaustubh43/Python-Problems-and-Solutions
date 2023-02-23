## Question 41
## Define a function which can generate
## and print a tuple where the value are
## square of numbers between 1 and 20 (both included).
##
## Hints:
##
## Use ** operator to get power of a number.
## Use range() for loops. Use list.append() to add values into a list.
## Use tuple() to get a tuple from a list.
##
## Solution

def gen_li(x):
    li = [a**2 for a in range(1,x+1)]
    return li

x = gen_li(20)
print(x[5:])
