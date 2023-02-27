## Question 69
## Please write a program using generator to print the numbers
## which can be divisible by 5 and 7 between 0 and n in comma
## separated form while n is input by console.
##
## Example: If the following n is given as input to the program:
##
## 100
##
## Then, the output of the program should be:
##
## 0,35,70
##
## Hints: Use yield to produce the next value in generator.
##
## In case of input data being supplied to the question,
## it should be assumed to be a console input.

def func(x):
    k = 0
    while k <= x:
        if k % 5 == 0 and k % 7 == 0:
            yield k
        k += 1

n = int(input('Enter the value of n'))
values = list()
for j in func(n):
    values.append(str(j))

print(','.join(values))
