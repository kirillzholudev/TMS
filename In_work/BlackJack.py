from random import shuffle
from time import sleep
class Card:

    def __init__(self, mast, val, tuz_value=11): # __init__ всегда должен return None
        self.mast = mast
        self.value = val
    #     self.tuz_value = tuz_value
    #     self.tuz = self.is_tuz()

    # def is_tuz(self):
    #     return self.value == self.tuz_value

    def __repr__(self):
        return f"{self.mast}-{self.value}"


class Deck:

    def __init__(self, masts, values):
        self.__deck = []
        self.masts = masts
        self.values = values
        self.generate_deck()
        self.chesat_kolodu()

    def generate_deck(self):
        for mast in self.masts:
            for value in self.values:
                self.__deck.append(Card(mast, value))

    def chesat_kolodu(self):
        shuffle(self.__deck)

    def get_card(self):
        return self.__deck.pop(0)

    def __repr__(self):
        return f'{len(self.__deck)}/{len(self.values ) * len(self.masts)} Cards'

values = [1,2,3,4,5,6,7,8,9,10,11]
masts = ['chirva', 'pika', 'kresti', 'bubl']

deck = Deck(masts, values)

player_score = 0
computer_score = 0

while player_score < 21 or computer_score < 21:
    ch = input("Take card?")
    per_card = deck.get_card()
    player_score += per_card.value
    print(f'ur card is {per_card}\nand ur score is {player_score}')
    print('computer selects card...')
    sleep(1)
    comp_card = deck.get_card()
    computer_score += comp_card.value
    print(f'and his card is {comp_card}\nand his score is {computer_score}')