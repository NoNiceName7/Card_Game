from random import shuffle
from Card import Card
from random import shuffle, choice
class DeckOfCards:
    def __init__(self):
        self.cards = []
        for value in range(2, 15):
            for symbol in range(4):
                self.cards.append(Card(value,symbol))

    def Card_shuffle(self):
        shuffle(self.cards)

    def deal_one(self):
        rand_card = choice(self.cards)
        self.cards.remove(rand_card)
        return rand_card


