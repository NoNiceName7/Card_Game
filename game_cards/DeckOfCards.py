from random import shuffle
from Card import Card
from random import shuffle, choice
class DeckOfCards:
    def __init__(self):
        """A constructor of DeckOfCards """
        self.cards = []
        for value in range(2, 15):
            for symbol in range(4):
                self.cards.append(Card(value,symbol))

    def Card_shuffle(self):
        """shuffling a pack of cards"""
        shuffle(self.cards)

    def deal_one(self):
        """Picking a random card from the deck and removing him """
        rand_card = choice(self.cards)
        self.cards.remove(rand_card)
        return rand_card


