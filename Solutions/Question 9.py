## Question 9
## Write a program that accepts sequence of lines
## as input and prints the lines after making all
## characters in the sentence capitalized.
## Suppose the following input is supplied to the
## program:
## Hello world
## Practice makes perfect
## Then, the output should be:
## HELLO WORLD
## PRACTICE MAKES PERFECT
##
## Hints:
## In case of input data being supplied to the question,
## it should be assumed to be a console input.

print("Copy paste your sentences here")
contents = []
while True:
    try:
        line = input()
    except EOFError:
        break
    contents.append(line.upper())

contents.upper()
