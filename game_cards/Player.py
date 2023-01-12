from DeckOfCards import DeckOfCards
from random import choice
from Card import Card


# class of the player
class Player:
    def __init__(self, name: str, num_cards: int = 26):
        """This method get a name and amount of cards in the hand,
        in the beginning the hand is clear"""
        self.name = name
        self.num_cards = num_cards
        self.hand = []

    def set_hand(self, deck: DeckOfCards):
        """This method set the hand of the player with random cards from the main deck"""
        for card in range(self.num_cards):
            self.hand.append(deck.deal_one())

    def get_card(self):
        """This method dealing a random card from the player hand and then remove it for the hand"""
        pick = choice(self.hand)
        self.hand.remove(pick)
        return pick

    def add_card(self, card: Card):
        """This method adding a card to the player hand"""
        self.hand.append(card)

    def __repr__(self):
        return f"Player: {self.name}, and his cards is: {self.hand}"
