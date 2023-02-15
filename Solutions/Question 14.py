# Question 14
# Level 2
#
# Question:
# Write a program that accepts a sentence and calculate the number of upper case letters and lower case letters.
# Suppose the following input is supplied to the program:
# Hello world!
# Then, the output should be:
# UPPER CASE 1
# LOWER CASE 9

def count_case(item):
    d = {
        'UPPER': 0,
        'LOWER': 0
    }
    for _ in item:
        if _.isupper():
            d['UPPER'] += 1
        elif _.islower():
            d['LOWER'] += 1
        else:
            continue
    return [d['UPPER'], d['LOWER']]


x = input('Enter a string to count upper and lower case')
upper, lower = count_case(x)
print(f'Upper case are {upper} and lower cases are {lower}')