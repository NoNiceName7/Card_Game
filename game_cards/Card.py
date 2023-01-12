# class of the cards
class Card:
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
