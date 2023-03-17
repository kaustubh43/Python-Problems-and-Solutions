## With a given list [12,24,35,24,88,120,155,88,120,155],
##
## write a program to print this list after removing all duplicate
##
## values with original order reserved.
##
## Hints: Use set() to store a number of values without duplicate.
##
## Solution:

def remove_duplicates(li):
    ni_li = []
    s = set()
    for k in li:
        if k not in s:
            s.add(k)
            ni_li.append(k)
    return ni_li



data = [12, 24, 35, 24, 88, 120, 155, 88, 120, 155]
print(remove_duplicates(data))



