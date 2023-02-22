## Question 33
## Define a function which can print a dictionary
## where the keys are numbers between 1 and 3 (both included)
## and the values are square of keys.
##
## Hints:
##
## Use dict[key]=value pattern to put entry into a dictionary.
## Use ** operator to get power of a number.

def get_dict():
    d1 = {x:x**2 for x in range(1,21)}
    print(d1)


get_dict()
