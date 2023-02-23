## Write a program which accepts a string
## as input to print "Yes" if the string is "yes" or
## "YES" or "Yes", otherwise print "No".
##
## Hints:
##
## Use if statement to judge condition.
##
## Solution

x = input('Enter user input: ')
 
if x.lower() == 'yes':
    print('Yes')
else:
    print('No')

