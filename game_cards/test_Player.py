from unittest import TestCase, mock
from Player import Player
from DeckOfCards import DeckOfCards
from unittest.mock import patch
from Card import Card


class TestPlayer(TestCase):
    def setUp(self):
        self.p1 = Player("Amit", 10)
        self.deck = DeckOfCards()
        self.symbols = ["Diamonds", "Spades", "Hearts", "Clubs"]
        self.values = [None, None, "2", "3", "4", "5", "6", "7",
                       "8", "9", "10", "Jack", "Queen", "King", "Ace"]
        self.value = self.values.index("2")
        self.symbol = self.symbols.index("Clubs")
        self.card1 = Card(self.value, self.symbol)

    def test__init__valid(self):
        """Checking a case of valid __init__"""
        self.assertEqual(self.p1.name, "Amit")
        self.assertEqual(self.p1.num_cards, 10)
        self.assertEqual(self.p1.hand, [])

    def test__init__invalid_name(self):
        """Checking a case of invalid player name type"""
        with self.assertRaises(TypeError):
            p2 = Player([], 10)

    def test__init__invalid_number_of_cards(self):
        """Checking a case of invalid number of cards in player hand type"""
        with self.assertRaises(TypeError):
            p2 = Player("Amit", "25")

    def test__init__empty_name(self):
        """Checking a case of empty name"""
        p2 = Player("", 10)
        self.assertEqual(p2.name, "Anonymous")

    def test__init__number_of_cards_in_range(self):
        """Checking a case of number of cards in player hand in range
        10<= num_cards <= 26"""
        p2 = Player("Amit", 26)
        p1 = Player("Liav", 10)
        self.assertEqual(p2.num_cards, 26)
        self.assertEqual(p1.num_cards, 10)

    def test__init__number_of_cards_out_of_range(self):
        """Checking a case of number of cards in player hand out of range
        10 > num_cards > 26"""
        p2 = Player("Amit", 32)
        p1 = Player("Liav", 1)
        self.assertEqual(p2.num_cards, 26)
        self.assertEqual(p1.num_cards, 26)

    def test_set_hand_valid_hand(self):
        """Checking a valid case of set hand"""
        with patch("DeckOfCards.DeckOfCards.deal_one") as mock_card:
            mock_card.return_value = "2 Diamonds"
            self.p1.set_hand(self.deck)
            self.assertEqual(self.p1.hand, ["2 Diamonds", "2 Diamonds", "2 Diamonds",
                                            "2 Diamonds", "2 Diamonds", "2 Diamonds",
                                            "2 Diamonds", "2 Diamonds", "2 Diamonds",
                                            "2 Diamonds"])

    def test_set_hand_valid_length(self):
        """Checking a valid case of player hand length"""
        self.p1.set_hand(self.deck)
        self.assertEqual(self.p1.num_cards, len(self.p1.hand))

    def test_set_hand_invalid_deck(self):
        """Checking a case of invalid setting player hand
        the deck isn't DeckOfCards type"""
        with self.assertRaises(TypeError):
            self.p1.set_hand(10)

    @mock.patch("DeckOfCards.DeckOfCards.deal_one", return_value="2 Diamonds")
    def test_get_card_valid(self, mock_card_deck):
        """Checking a valid case of get card"""
        self.p1.set_hand(self.deck)
        self.assertEqual(self.p1.get_card(), "2 Diamonds")

    def test_add_card_valid(self):
        """Checking a valid case of adding a card to player hand"""
        self.p1.add_card(self.card1)
        self.assertIn(self.card1, self.p1.hand)

    def test_add_card_invalid_card(self):
        """Checking a case of invalid card type"""
        with self.assertRaises(TypeError):
            self.p1.add_card([])
