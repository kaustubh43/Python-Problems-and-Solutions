# Question 86
# Please write a program to generate all sentences
# where subject is in ["I", "You"] and verb is in ["Play", "Love"]
# and the object is in ["Hockey","Football"].
#
# Hints: Use list[index] notation to get an element from a list.
#
# Solution:

x = ['I', 'You']
y = ['Play', 'Love']
z = ['Hockey', 'Football']

for i in x:
    for j in y:
        for k in z:
            print(i, j, k)
