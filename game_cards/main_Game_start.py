from CardGame import CardGame

# The main game, every player put his name in and get a hand of cards.
name1 = input(f"Enter Player 1 name: ")
name2 = input(f"Enter Player 2 name: ")
game = CardGame(name1, 10, name2, 10)
print(game.p1)
print(game.p2)
print("--- start ---")
# The game run 10 rounds and in each round the program will announce the winner.
for i in range(1, 11):
    print(f"Round no.{i}")
    card_p1 = game.p1.get_card()
    card_p2 = game.p2.get_card()
    print(f"Player 1 card: {card_p1}\n"
          f"Player 2 card: {card_p2}")

    if card_p1 > card_p2:
        game.p1.add_card(card_p1)
        game.p1.add_card(card_p2)
        print(f"Winner of the round is: {game.p1.name}")

    if card_p1 < card_p2:
        game.p2.add_card(card_p2)
        game.p2.add_card(card_p1)
        print(f"Winner of the round is: {game.p2.name}")

    if card_p1 == card_p2:
        print(f"No one win the round,Its a tie!!!")
    print(game.p1)
    print(game.p2)
    print("----------------------------------------------------------------------------------------------------------")

# In the end of the rounds the program check witch player have the bigger peck and announce the winner,
# in a case of a draw the program will announce it.
print(game.get_winner())
