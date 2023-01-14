from Card import Card
from random import shuffle, choice


# Class that make the main deck of the game
class DeckOfCards:
    def __init__(self):
        """This method create the main deck of the game"""
        self.cards = []
        for value in range(2, 15):
            for symbol in range(4):
                self.cards.append(Card(value, symbol))

    def card_shuffle(self):
        """This method shuffle the deck so the deck will be random"""
        shuffle(self.cards)

    def deal_one(self):
        """This method dealing a random card from the deck,
        show it and removing it from the deck"""
        rand_card = choice(self.cards)
        self.cards.remove(rand_card)
        return rand_card
