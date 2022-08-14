from math import ceil


class WinDoor:
    def __init__(self, height, width, name: str):
        self.width = width
        self.height = height
        self.name = name
        self.square = height * width

    def __repr__(self):
        return f'{self.name} {self.height}height{self.width}'


class Room:
    def __init__(self, height, width_r, length_r):
        self.total_roll = None
        self.square = 2 * height * (width_r + length_r)
        self.new_square = None
        self.wd = []
        self.width_r = width_r
        self.length_r = length_r
        self.height = height

    def addWD(self, height, width, name: str):
        self.wd.append(WinDoor(height, width, name))

    def workSurface(self):
        self.new_square = self.square
        for i in self.wd:
            self.new_square -= i.square
        return self.new_square

    def wallpaper(self, dl, sh):  # Length and width of the roll
        self.total_roll = self.new_square / (dl * sh)
        return ceil(self.total_roll)


class Interface:
    def __init__(self):
        self.room = Room(
            float(input("Enter Height of room: ")),
            float(input("Enter Width of room: ")),
            float(input("Enter Length of room: "))
        )
        self.addwindoor = self.windoor()
        self.square = self.room.workSurface()
        self.roll_wallpaper = self.roll()

    def windoor(self):
        ch_1 = str(input('Do you have a window or door? Y/N\n'
                         '--> '))
        work_1 = True
        while work_1:
            if ch_1 == 'Y' or 'y':
                i = input('1. Add window\n'
                          '2. Add door\n'
                          '3. Next step\n'
                          '--> ')
                count_w = 0
                count_d = 0
                if i == '1':
                    count_w += 1
                    self.room.addWD(
                        float(input(f"Window {count_w}. Enter the window height: ")),
                        float(input("\t\tEnter the window width: ")),
                        input("\t\tEnter the window name: ")
                    )
                    continue
                if i == '2':
                    count_d += 1
                    self.room.addWD(
                        float(input(f"Door {count_d}. Enter the door height: ")),
                        float(input("\t\tEnter the door width: ")),
                        input("\t\tEnter the door name: ")
                    )
                    continue
                else:
                    work_1 = False
            else:
                break

    def roll(self):
        return self.room.wallpaper(
            float(input("Enter the length of the wallpaper: ")),
            float(input("Enter the width of the wallpaper: "))
        )

    def __repr__(self):
        return (
            f"\nYour work surface: {self.square} "
            f"\nYou need: {self.roll_wallpaper}, roll(s) of wallpaper"
        )


start_interface = Interface()
print(start_interface)
