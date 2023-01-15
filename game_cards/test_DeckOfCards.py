from unittest import TestCase
from DeckOfCards import DeckOfCards


class TestDeckOfCards(TestCase):
    def test_setUp(self):
        self.symbols = ["Diamonds", "Spades", "Hearts", "Clubs"]
        self.values = [None, None, "2", "3", "4", "5", "6", "7",
                       "8", "9", "10", "Jack", "Queen", "King", "Ace"]
        self.value = "King"
        self.symbol = "Hearts"

    def test__init__valid(self):
        """"Checking a valid case of deck of 52 cards"""
        deck = DeckOfCards()
        self.assertEqual(len(deck.cards), 52)

    def test__card_shuffle__valid(self):
        """"Checking a valid case of original hand first 13 cards after shuffling
         not equal to other hand"""
        original_hand = DeckOfCards()
        other_hand = ["2 Diamonds", "3 Diamonds", "4 Diamonds", "5 Diamonds", "6 Diamonds"
            , "7 Diamonds", "8 Diamonds", "9 Diamonds", "10 Diamonds", "Jack Diamonds",
                      "Queen Diamonds", "King Diamonds", "Ace Diamonds"]
        original_hand.card_shuffle()
        self.assertNotEqual(original_hand.cards[:14], other_hand)

    def test__deal_one__valid(self):
        """"Checking valid case of removing one card from deck"""
        deck = DeckOfCards()
        deck.deal_one()
        self.assertEqual(len(deck.cards), 51)
