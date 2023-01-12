# class of the cards
class Card:
    symbol = ["Spades", "Hearts", "Diamonds", "Clubs"]
    values = [None, None, "2", "3", "4", "5", "6", "7",
              "8", "9", "10", "Jack", "Queen", "King", "Ace"]

    def __init__(self, value, symbol):
        """A constructor of card """
        self.value = value
        self.symbol = symbol

    def __gt__(self, other):
        """Checking which card is the stronger, if the cards have the same symbol the method check the value"""
        if self.symbol > other.symbol:
            return True
        elif self.symbol == other.symbol and self.value > other.value:
            return True
        else:
            return False

    def __eq__(self, other):
        """Checking if the cards are equal by the symbol and value"""
        if self.symbol == other.symbol and self.value == other.value:
            return True
        else:
            return False

    def __repr__(self):
        v = self.values[self.value] + ' ' + self.symbol[self.symbol]
        return v
