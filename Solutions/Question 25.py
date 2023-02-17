## Question 25
## Level 1
##
## Question: Define a class, which have a class parameter
## and have a same instance parameter.
##
## Hints: Define a instance parameter, need add it in
## init method You can init a object with construct parameter
## or set the value later
class Human:
    name = 'Human'


    def __init__(self, name = None):
        self.name =  name

human1 = Human('Jeffrey')
print(f'{human1.name}')

human2 = Human()
human2.name = 'Ramu'
print(f'{human2.name}')
