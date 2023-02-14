'''
Question 12
Write a program, which will find all such numbers
between 1000 and 3000 (both included) such that
each digit of the number is an even number.
The numbers obtained should be printed in a
comma-separated sequence on a single line.
'''

def check_odd(item):
    """Checks if the numbers in list are odd"""
    return int(item) % 2 == 0

nums = [str(x) for x in range(1000,3000)]
even_digits = []

for k in nums:
    if list(k) == list(filter(check_odd, k)):
        even_digits.append(k)


print(', '.join(even_digits))


        
        
