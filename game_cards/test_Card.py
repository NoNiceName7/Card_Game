from unittest import TestCase
from Card import Card


class TestCard(TestCase):
    def setUp(self):
        self.symbols = ["Diamonds", "Spades", "Hearts", "Clubs"]
        self.values = [None, None, "2", "3", "4", "5", "6", "7",
                       "8", "9", "10", "Jack", "Queen", "King", "Ace"]
        self.value = "King"
        self.symbol = "Hearts"

    def test__init__valid_1(self):
        """"Checking a valid value and symbol is exits in lists"""
        self.assertIn(self.value, self.values)
        self.assertIn(self.symbol, self.symbols)

    def test__gt__valid_1_True(self):
        """"Checking 2 valid True cases of self value and symbol greater
         than other value and symbol"""
        symbol2 = self.symbols.index("Diamonds")
        equals = self.symbols.index("Hearts")
        small_value = self.values.index("2")
        self.assertTrue(self.symbols.index(self.symbol) > symbol2)
        self.assertEqual(self.symbols.index(self.symbol), equals)
        self.assertTrue(self.values.index(self.value) > small_value)

    def test__gt__valid_2_False_symbol(self):
        """"Checking a valid False case of self symbol smaller than
         other symbol"""
        symbol2 = self.symbols.index("Clubs")
        self.assertFalse(self.symbols.index(self.symbol) > symbol2)

    def test__gt__valid_3_False_value(self):
        """"Checking a valid False case of self symbol equal to
         other symbol and self value smaller than other value"""
        equals = self.symbols.index("Hearts")
        big_value = self.values.index("Ace")
        self.assertEqual(self.symbols.index(self.symbol), equals)
        self.assertFalse(self.values.index(self.value) > big_value)

    def test__eq__valid_1_True(self):
        """"Checking a valid True case of self symbol equal to
            other symbol and self value equal to other value"""
        equal_value = self.values.index("King")
        equal_symbol = self.symbols.index("Hearts")
        self.assertTrue(self.symbols.index(self.symbol) == equal_symbol)
        self.assertTrue(self.values.index(self.value) == equal_value)

    def test__eq__valid_2_False_symbol(self):
        """"Checking a valid False case of self symbol not equal to
            other symbol and self value equal to other value"""
        equal_value = self.values.index("King")
        not_equal_symbol = self.symbols.index("Spades")
        self.assertFalse(self.symbols.index(self.symbol) == not_equal_symbol)
        self.assertEqual(self.values.index(self.value), equal_value)

    def test__eq__valid_3_False_value(self):
        """"Checking a valid False case of self symbol equal to
            other symbol and self value not equal to other value"""
        not_equal_value = self.values.index("2")
        equal_symbol = self.symbols.index("Hearts")
        self.assertEqual(self.symbols.index(self.symbol),equal_symbol)
        self.assertFalse(self.values.index(self.value) == not_equal_value)

    def test__eq__valid_4_False_both(self):
        """"Checking a valid False case of both self symbol and value
        not equal to other symbol and value"""
        not_equal_value = self.values.index("2")
        not_equal_symbol = self.symbols.index("Spades")
        self.assertFalse(self.symbols.index(self.symbol) == not_equal_symbol)
        self.assertFalse(self.values.index(self.value) == not_equal_value)
