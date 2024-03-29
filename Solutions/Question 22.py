# Level 3
#
# Question: Write a program to compute the frequency of the words from the input.
#
# The output should output after sorting the key alphanumerically.
#
# Suppose the following input is supplied to the program: New to Python or choosing between Python 2 and Python 3?
#
# Read Python 2 or Python 3.
#
# Then, the output should be: 2:2 3.:1 3?:1 New:1 Python:5 Read:1 and:1 between:1 choosing:1 or:2 to:1
#
# Hints In case of input data being supplied to the question, it should be assumed to be a console input.
#
# Solution:

freq = {}
data = input()
for i in data.split():
    freq[i] = freq.get(i, 0) + 1

letters = freq.keys()
print(letters)

for i in letters:
    print(f'{i}:{freq.get(i)} ', end=' ')
