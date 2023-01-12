from Card import Card
from DeckOfCards import *
from Player import *
from CardGame import *

name1=input(f"Enter Player 1 name :")
name2=input(f"Enter Player 2 name :")
game=CardGame(name1,10,name2,10)
print(game.p1)
print(game.p2)
for i in range(10):
    card_p1=game.p1.get_card()
    card_p2=game.p2.get_card()
    print(f"Player 1 card : {card_p1}\n"
          f"Player 2 card : {card_p2}")
    if card_p1>card_p2:
        game.p1.add_card(card_p1)
        game.p1.add_card(card_p2)
        print(f"Winner of the round is : {game.p1.name}")

    if card_p1<card_p2:
        game.p2.add_card(card_p2)
        game.p2.add_card(card_p1)
        print(f"Winner of the round is : {game.p2.name}")

    if card_p1==card_p2:
        print(f"No one win the round,Its a tie")
    print(game.p1)
    print(game.p2)

if len(game.p1.hand)>len(game.p2.hand):
    print(f"Winner of the game is : {game.p1.name}")
if len(game.p1.hand)<len(game.p2.hand):
    print(f"Winner of the game is : {game.p2.name}")
if len(game.p1.hand)==len(game.p2.hand):
    print(f"Its a draw no one wins !")

