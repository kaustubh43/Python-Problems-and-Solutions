## Question 43
## Write a program to generate and print another tuple
## whose values are even numbers in the given tuple (1,2,3,4,5,6,7,8,9,10).
##
## Hints:
##
## Use "for" to iterate the tuple Use tuple() to generate a tuple from a

x = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
li = list()

for k in x:
    if k % 2 == 0:
        li.append(k)

tp = tuple(li)
print(tp)
