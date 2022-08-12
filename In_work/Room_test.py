l = 5.5   # длина
w = 3     # ширина
h = 2.75  # высота

l_w = 10
w_w = 1

s_1 = (l + w) * 2
lanes = s_1 / w_w
lanes_in_1 = l_w // (h + 0.1)  # без обрезков (только целе полосы)
sum_roll = s_1 / lanes_in_1



class WinDoor:
    def __init__(self, x, y, name="unk"):
        self.x = x
        self.y = y
        self.name = name
        self.square = x * y

    def __repr__(self):
        return f'{self.name} {self.x}x{self.y}'


door = WinDoor(0.9, 3.14, 'PiDoor')


class Room:
    def __init__(self, x, y, z):
        self.square = z * (x + y)
        self.wd = []
        self.sides = []
        self.x = x
        self.y = y
        self.z = z
        self.addSides()

    def addSides(self):
        self.sides.append(WinDoor((self.z, self.x, self.y)))

    def addWD(self, w, h, name='unk'):
        self.wd.append(WinDoor(w, h, name))

    def workSurface(self):
        new_square = self.square
        for i in self.wd:
            new_square -= i.square
        return new_square

    def wallpaper(self, dl, sh):      # Length and width of the roll
        size = (self.x + self.y) * 2
        lines = dl // (self.z + 0.1)
        total_roll = size / lines
        return f'You need {round(total_roll)} roll'





room_1 = Room(5.5, 3, 2.75)
print(room_1.square)

room_1.addWD(1.5, 1.5, 'big_win')
room_1.addWD(1, 2, 'Fiodoor')
room_1.addWD(0.20, 0.40, 'schel')
print(room_1.wd)
print(room_1.square())


print(room_1.workSurface())

print(room_1.wallpaper(10, 1))


