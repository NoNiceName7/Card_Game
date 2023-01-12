from Card import Card
from DeckOfCards import *
from random import choice
#class of player
class Player:
    def __init__(self,name:str,num_cards:int=26):
        self.name=name
        self.num_cards=num_cards
        self.hand=[]
    def set_hand(self,deck:DeckOfCards):
        for card in range(self.num_cards):
            self.hand.append(deck.deal_one())
    def get_card(self):
        pick=choice(self.hand)
        self.hand.remove(pick)
        return pick
    def add_card(self,card:Card):
        self.hand.append(card)

    def __repr__(self):
        return f"Player :{self.name},and his cards is :{self.hand}"



