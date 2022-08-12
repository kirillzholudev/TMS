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
LOC = {'id': 0
    }


class Hero:
    """Возможности героя"""

    def __init__(self, name):
        self.name = name
        self.loc = LOC
        self.choise()

    def location(self):
        pass

    def around_hero(self):
        pass


    def choise(self):
        inp = input("Choces: ")
        for i in range(len(ROOMS)):
            for inp in ROOMS:
                print(ROOMS[i]['doors'])





hero1 = Hero('Kiryl')
hero1()



























