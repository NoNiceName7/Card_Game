
from Card import Card
from DeckOfCards import *
from Player import *
from random import choice
#class of DeckOfCards
class CardGame:
    def __init__ (self,p1,num_cards1,p2,num_cards2):
        self.p1=Player(p1,num_cards1)
        self.p2=Player(p2,num_cards2)
        self.deck=DeckOfCards()
        self.new_game()

    def new_game(self):
        self.deck.Card_shuffle()
        self.p1.set_hand(self.deck)
        self.p2.set_hand(self.deck)
    def get_winner(self):
        if len(self.p1.hand)>len(self.p2.hand):
            return self.p1.name
        elif len(self.p1.hand)<len(self.p2.hand):
            return self.p2.name
        else:
            return None





