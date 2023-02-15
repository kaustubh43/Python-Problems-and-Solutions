# Question 16
# Level 2
#
# Question:
# Use a list comprehension to square each odd number in a list. The list is input by a sequence of comma-separated numbers.
# Suppose the following input is supplied to the program:
# 1,2,3,4,5,6,7,8,9
# Then, the output should be:
# 1,3,5,7,9

x = input('Enter comma separated numbers ')

x1 = x.split(',')
newl = []
for _ in x1:
    newl.append(int(_))

num = [str(k ** 2) for k in newl if k % 2 == 1]
print(','.join(num))

new1 = [str(int(i)**2) for i in x.split(',') if int(i) % 2 == 1]
print(','.join(new1))