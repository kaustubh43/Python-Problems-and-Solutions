# Level 3
#
# Question A robot moves in a plane starting from the original point (0,0). The robot can move toward UP, DOWN,
# LEFT and RIGHT with a given steps.
#
# The trace of robot movement is shown as the following: UP 5 DOWN 3 LEFT 3 RIGHT 2 ¡­ The numbers after the
# direction are steps.
#
# Please write a program to compute the distance from current position after a sequence of movement and original point.
#
# If the distance is a float, then just print the nearest integer.
#
# Example: If the following tuples are given as input to the program: UP 5 DOWN 3 LEFT 3 RIGHT 2 Then, the output of
# the program should be: 2
#
# Hints: In case of input data being supplied to the question, it should be assumed to be a console input.
#
# Solution:
from math import sqrt
origin = [0, 0]
current = [0, 0]
while True:
    step = input('Enter the steps: ')
    if len(step) % 2 == 0:
        break
    else:
        print('Please Enter valid Directions')
step = step.split(' ')
for i in range(0, len(step), 2):
    direction = step[i]
    distance = int(step[i+1])
    if direction == 'UP':
        current[1] += distance
    elif direction == 'DOWN':
        current[1] -= distance
    elif direction == 'LEFT':
        current[0] -= distance
    elif direction == 'RIGHT':
        current[0] += distance
    else:
        print('Invalid Directions, Robot will not move')
        continue
print('current coordinates are', current)
travel = sqrt(current[0]**2+current[1]**2)

print(f'Distance travelled by robot is {round(travel)}')
