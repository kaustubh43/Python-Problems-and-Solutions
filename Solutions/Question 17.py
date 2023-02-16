## Question 17
## Level 2
##
## Question: Write a program that computes the net amount
## of a bank account based a transaction log from console input.
## The transaction log format is shown as following: D 100 W 200
##
## D means deposit while W means withdrawal.
## Suppose the following input is supplied to the program:
## D 300 D 300 W 200 D 100
## Then, the output should be: 500
##
## Hints: In case of input data being supplied to the question,
## it should be assumed to be a console input.
x = input('input the string: ')
x = x.split(' ')
dep = []
wit = []
net = 0
for i in x:
    if i == 'D':
        net += int(x[x.index(i)+1])
    elif i == 'W' and int(x[x.index(i)+1]) <= net:
         net -= int(x[x.index(i)+1])
    else:
        continue
print(f'The Balance is ₹{net}')
