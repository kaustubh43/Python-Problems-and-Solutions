## Question 32
## Define a function that can accept an integer number as
## input and print the "It is an even number" if the number
## is even, otherwise print "It is an odd number".
##
## Hints:
##
## Use % operator to check if a number is even or odd.
##
## Solution

def oddEven(x):
    if x % 2 == 0:
        print("It is Even")
    else:
        print('It is odd')

oddEven(2)
oddEven(5)
