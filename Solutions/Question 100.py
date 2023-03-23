# Write a program to solve a classic ancient Chinese puzzle:
#
# We count 35 heads and 94 legs among the chickens and rabbits in a farm.
#
# How many rabbits and how many chickens do we have?
#
# Hint: Use for loop to iterate all possible solutions.
#
# Solution:


def solve(num_head, num_legs):
    ns = 'No Solution'
    for i in range(num_head + 1):
        j = num_head - i
        if 2 * i + 4 * j == num_legs:
            return i, j
    return ns


heads = 35
legs = 94
solutions = solve(heads, legs)
print(solutions)

