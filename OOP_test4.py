from random import randint, randrange


class Cube:
    edge = 0
    b = []

    def throw(self):
        print(f'You have a {self.edge} grain cube')

        for i in range(1, self.edge + 1):
            self.b.append(i)

        my_range = randrange(len(self.b))
        print(f'After the roll, you dropped a edge with the number {my_range}\n')

# Cube 1
throw1 = Cube()
throw1.edge = randint(6, 12)
throw1.throw()

# Cube 2
throw2 = Cube()
throw2.edge = randint(6, 12)
throw2.throw()

