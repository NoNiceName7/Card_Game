from Player import Player
from DeckOfCards import DeckOfCards


# Class of the card game.
class CardGame:
    def __init__(self, p1: str, num_cards1: int, p2: str, num_cards2: int):
        """This method get two players and how many cards each one get,
         and give each one of them a peck of random cards"""
        if type(p1) != str:
            raise TypeError("Argument Player1 must be type of str")
        if type(p2) != str:
            raise TypeError("Argument Player2 must be type of str")
        if type(num_cards1) != int:
            raise TypeError("Argument number of cards 1 must be type of int")
        if type(num_cards2) != int:
            raise TypeError("Argument number of cards 2 must be type of int")
        if p1 == '':
            p1 = "Anonymous1"
        if p2 == '':
            p2 = "Anonymous2"
        self.p1 = Player(p1, num_cards1)
        self.p2 = Player(p2, num_cards2)
        self.deck = DeckOfCards()
        self.new_game()

    def new_game(self):
        """This method take the full deck and shuffle it,
        after that the method dealing cards to the players hand"""
        self.deck.card_shuffle()
        self.p1.set_hand(self.deck)
        self.p2.set_hand(self.deck)

    def get_winner(self):
        """This method check the length of the hand of each player and announce the winner"""
        if len(self.p1.hand) > len(self.p2.hand):
            return f"The winner of the game is: {self.p1.name}"
        elif len(self.p1.hand) < len(self.p2.hand):
            return f"The winner of the game is: {self.p2.name}"
        else:
            return f"No one win the game, its a tie!!!"
