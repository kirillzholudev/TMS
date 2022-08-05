ROOMS = [
    {
        "id": "room-1",
        "name": "Your room",
        "doors": {1: "room-2", 2: "room-6"}

    },
    {
        "id": "room-2",
        "name": "Dark room",
        "doors": ["room-3", "room-4"]
    },
    {
        "id": "room-10",
        "name": "Exiting the labyrinth",
        "doors": []
    },
    {
        "id": "room-1",
        "name": "Your room",
        "doors": {1: "room-2", 2: "room-6"}

    },
    {
        "id": "room-6",
        "name": " ",
        "doors": ["room-1", "room-10", "room-5"]
    },
    {
        "id": "room-10",
        "name": "Exiting the labyrinth",
        "doors": []
    }
]

CHOISE = [
    {"1": 1},
    {"2": 2},
    {"3": 3}

]

class Hero:
    """Возможности героя"""

    def __init__(self):
        self.loc = ROOMS[0]['id']


    def location(self):
        pass


    def around_hero(self):
        print(f'Вы находитесь в: {self.loc}')


    def choise(self, a):

        pass



hero1 = Hero()




work = True
while work:
    print('Варинаты:\n'
          '1. Осмотрется\n'
          'Ваш выбор:')
    inp = input()
    if inp == 1:
        hero1.around_hero()


























