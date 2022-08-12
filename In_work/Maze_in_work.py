LEVEV1 = [
    {
        "id": "room-1",
        "name": "Ominous Dark Room",
        "doors": ["room-6", "room-2", "room-10"]
    },
    {
        "id": "room-6",
        "name": "Your room (clean up)",
        "doors": ["room-1", "room-10", "room-5"]
    },
    {
        "id": "room-10",
        "name": "Exiting the labyrinth",
        "doors": ['room-7', 'room-8', 'room-11']
    }
]
CHOICE1 = []



class Start:
    def choices(self):
        for i in range(len(LEVEV1)):
            print(LEVEV1[i]['doors'])
            inp = input('Which room? ')
            for inp in LEVEV1:

                print('You in', LEVEV1[i]['id'])

            total = 1
            for i in range(total):
                if inp in LEVEV1[i]['id']:
                    print('ok')
                    total += 1
                else:
                    continue

t1 = Start()
t1.choices()