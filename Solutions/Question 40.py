## Question 40
## Define a function which can generate a list
## where the values are square of numbers between
## 1 and 20 (both included). Then the function needs
## to print all values except the first 5 elements in the list.
##
## Hints:
##
## Use ** operator to get power of a number.
## Use range() for loops. Use list.append() to
## add values into a list. Use [n1:n2] to slice a list
##
## Solution

def gen_li(x):
    li = [a**2 for a in range(1,x+1)]
    return li

x = gen_li(20)
print(x[5:])
