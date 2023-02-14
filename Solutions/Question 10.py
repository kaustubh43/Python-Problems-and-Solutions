##Question:
##Write a program that accepts a sequence of
##whitespace separated words as input and prints
##the words after removing all duplicate words and
##sorting them alphanumerically.
##Suppose the following input is supplied to the program:
##hello world and practice makes perfect and hello world again
##Then, the output should be:
##again and hello makes perfect practice world

raw = input("Enter the string: ")
uni = []
for x in raw.split(' '):
    if x not in uni:
        uni.append(x)
    else:
        continue

uni.sort()
print(' '.join(uni))





    

