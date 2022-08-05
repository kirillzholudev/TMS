# игральный кубик
from random import randint, randrange


class Cube:

    def __init__(self, edge):
        self.edge = edge

    def throw(self):
        print(f'You have a {self.edge} grain cube')

        my_range = randrange(1, self.edge, 1)
        print(f'After the roll, you dropped a edge with the number {my_range}\n')

# Cube 1
cube1 = Cube(edge=6)
cube1.throw()

# Cube 2
cube2 = Cube(edge=12)
cube2.throw()