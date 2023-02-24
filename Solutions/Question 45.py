## Question 45
## Write a program which can filter even numbers
## in a list by using filter function. The list
## is: [1,2,3,4,5,6,7,8,9,10].
##
## Hints:
##
## Use filter() to filter some elements in a list.
## Use lambda to define anonymous functions.
##
## Solution

li = [1,2,3,4,5,6,7,8,9,10]

def even_nums(x):
    return x % 2 == 0


x = list(filter(even_nums,li))
print(x)

# Different approach

y = list(filter(lambda k: k%2==0, li))
print(y)
