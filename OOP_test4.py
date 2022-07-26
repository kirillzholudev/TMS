from random import randint, randrange


class Cube:
    edge = randint(6, 12)
    b = []

    def status_cube(self):
        edge = Cube.edge
        print(f'You have a {edge} grain cube')

    def throw(self):
        edge = Cube.edge
        b = Cube.b
        for i in range(1, edge+1):
            b.append(i)
        my_range = randrange(len(b))
        print(f'After the roll, you dropped a edge with the number {my_range}')


throw1 = Cube()
throw1.status_cube()
throw1.throw()
