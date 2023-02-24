# Question 47
# Write a program which can map() and
# filter() to make a list whose elements are
# square of even number in [1,2,3,4,5,6,7,8,9,10].
#
# Hints Use map() to generate a list. Use
# filter() to filter elements of a list. Use lambda
# to define anonymous functions.

data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


def evenOnly(item):
    return item % 2 == 0


x = list(filter(evenOnly, data))
print(x)

# Using different approach
y = list(filter(lambda k: k % 2 == 0, data))
print('Using lambda functions', y)
