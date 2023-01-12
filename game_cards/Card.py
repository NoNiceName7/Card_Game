# class of the cards
class Card:
    symbols = ["Diamonds", "Spades", "Hearts", "Clubs"]
    values = [None, None, "2", "3", "4", "5", "6", "7",
              "8", "9", "10", "Jack", "Queen", "King", "Ace"]

    def __init__(self, value, symbol):
        """A constructor of Card"""
        self.value = value
        self.symbol = symbol

    def __gt__(self, other):
        """Checking which card is the stronger,
        if the cards have the same symbol the method check the value"""
        # Club > Hearts > Spades > Diamond
        if self.symbol > other.symbol:
            # 2 Diamond < Ace Clubs
            return True
        # 2 < 3 < 4 < 5 < 6 < 7 < 8 < 9 < 10 < Jack < Queen < King < Ace
        elif self.symbol == other.symbol and self.value > other.value:
            # 8 Clubs < King Clubs
            return True
        else:
            return False

    def __eq__(self, other):
        """Checking if the cards are equal by the symbol and value"""
        if self.symbol == other.symbol and self.value == other.value:
            # 2 Diamonds == 2 Diamonds
            return True
        else:
            # 2 Diamond != Ace Clubs
            return False

    def __repr__(self):
        v = str(self.values[self.value]) + ' ' + str(self.symbols[self.symbol])
        return v
