class Mystery:
    points = 0

    def __init__(self, name):
       self.name = name

    def __repr__(self):
        return f'{self.name}'

a1 = Mystery('user')
print(a1)