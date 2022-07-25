from random import randint
a = (randint(0,9) for i in range(8))
for i in a:
    print(next(a), end='')