# Question:
# Write a program that accepts a sentence and
# calculate the number of letters and digits.
# Suppose the following input is supplied to the program:
# hello world! 123
# Then, the output should be:

count = {
    'DIGITS' : 0,
    'ALPHABETS' : 0
    }

x = input('Enter the String ')

for _ in x:
    if _.isalpha():
        count['DIGITS'] += 1
    elif _.isdigit():
        count['ALPHABETS'] += 1
    else:
        continue

print(f'The Number of Digits are {count["DIGITS"]} and Alphabets are {count["ALPHABETS"]}')
