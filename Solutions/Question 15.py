# Question 15
# Level 2
#
# Question:
# Write a program that computes the value of a+aa+aaa+aaaa with a given digit as the value of a.
# Suppose the following input is supplied to the program:
# 9
# Then, the output should be:
# 11106

expression = 'a+aa+aaa+aaaa'
s_exp = expression.split('+')  # Converts to a list ['a', 'aa', 'aaa', 'aaaa']
print(s_exp)

val = '9'
val_exp = [int(len(x) * val) for x in s_exp]
print(val_exp)
print(sum(val_exp))