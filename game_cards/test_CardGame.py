from unittest import TestCase
from CardGame import CardGame


class TestCardGame(TestCase):
    def setUp(self):
        self.game = CardGame("Liav", 10, "Amit", 10)

    def test__init__new_game_valid(self):
        """"Checking a valid case of creating new game"""
        self.assertEqual(self.game.p1.name, "Liav")
        self.assertEqual(self.game.p2.name, "Amit")
        self.assertEqual(len(self.game.p1.hand), 10)
        self.assertEqual(len(self.game.p2.hand), 10)
        self.assertEqual(len(self.game.deck.cards), 32)

    def test__init__invalid_type_p1(self):
        """"Checking invalid case of Player 1 as int"""
        with self.assertRaises(TypeError):
            game = CardGame(55, 10, "Amit", 10)

    def test__init__invalid_type_p2(self):
        """"Checking invalid case of Player 2 as int"""
        with self.assertRaises(TypeError):
            game = CardGame("Liav", 10, 99, 10)

    def test__init__invalid_type_num_cards1(self):
        """"Checking invalid case of num_card1 as list"""
        with self.assertRaises(TypeError):
            game = CardGame("Liav", [10, 20], "Amit", 10)

    def test__init__invalid_type_num_cards2(self):
        """"Checking invalid case of num_card2 as str"""
        with self.assertRaises(TypeError):
            game = CardGame("Liav", 10, "Amit", "23asd")

    def test__init__valid_empty_p1(self):
        """"Checking a valid case of Player 1 anonymous"""
        game = CardGame('', 10, "Amit", 10)
        self.assertEqual(game.p1.name, "Anonymous1")

    def test__init__valid_empty_p2(self):
        """"Checking a valid case of Player 2 anonymous"""
        game = CardGame("Liav", 10, '', 10)
        self.assertEqual(game.p2.name, "Anonymous2")

    def test__get_winner_valid_p1(self):
        """"Checking a valid case of player 1 is the winner 13 cards against 10"""
        self.game.p1.hand = ["2 Diamonds", "3 Diamonds", "4 Diamonds", "5 Diamonds", "6 Diamonds",
                             "7 Diamonds", "8 Diamonds", "9 Diamonds", "10 Diamonds", "Jack Diamonds",
                             "Queen Diamonds", "King Diamonds", "Ace Diamonds"]
        self.assertEqual(self.game.get_winner(), "The winner of the game is: Liav")

    def test__get_winner_valid_p2(self):
        """"Checking a valid case of player 2 is the winner 13 cards against 10"""
        self.game.p2.hand = ["2 Diamonds", "3 Diamonds", "4 Diamonds", "5 Diamonds", "6 Diamonds",
                             "7 Diamonds", "8 Diamonds", "9 Diamonds", "10 Diamonds", "Jack Diamonds",
                             "Queen Diamonds", "King Diamonds", "Ace Diamonds"]
        self.assertEqual(self.game.get_winner(), "The winner of the game is: Amit")

    def test__get_winner_valid_tie(self):
        """"Checking a valid case of a tie"""
        self.game.p1.hand = ["2 Diamonds", "3 Diamonds", "4 Diamonds", "5 Diamonds", "6 Diamonds",
                             "7 Diamonds", "8 Diamonds", "9 Diamonds", "10 Diamonds", "Jack Diamonds",
                             "Queen Diamonds", "King Diamonds", "Ace Diamonds"]
        self.game.p2.hand = ["2 Diamonds", "3 Diamonds", "4 Diamonds", "5 Diamonds", "6 Diamonds",
                             "7 Diamonds", "8 Diamonds", "9 Diamonds", "10 Diamonds", "Jack Diamonds",
                             "Queen Diamonds", "King Diamonds", "Ace Diamonds"]
        self.assertEqual(self.game.get_winner(), "No one win the game, its a tie!!!")
