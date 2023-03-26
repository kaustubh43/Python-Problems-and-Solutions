# Level 3
#
# Question: Define a class with a generator which can iterate the numbers, which are divisible by 7, between a given
#
# range 0 and n.
#
# Hints: Consider use yield
#
# Solution:

class Generators:
    def __init__(self, n):
        self.n = n

    def div_by7(self):
        for k in range(self.n):
            if not k % 7:
                yield k


num = Generators(100)
for i in num.div_by7():
    print(i)
