# Please generate a random float where the value is between 10 and 100 using Python math module.
#
# Hints: Use random.random() to generate a random float in [0,1].
#
# Solution:

from random import uniform

print('Random number between 10 to 100 is ', uniform(10.0, 100.0))
