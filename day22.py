file = open('input22.txt').read().strip().split('\n\n')
player1, player2 = file
print(player1)
player1 = player1.split('\n')
player2 = player2.split('\n')
player1.pop(0)
player2.pop(0)

player1 = [int(x) for x in player1]
player2 = [int(x) for x in player2]


def check_cards():
    card1 = player1.pop(0)
    card2 = player2.pop(0)
    if card1 > card2:
        player1.append(card1)
        player1.append(card2)
    else:
        player2.append(card2)
        player2.append(card1)

def winner():
    if len(player1) >0:
        return player1
    return player2

round = 0
while len(player1) >0 and len(player2) >0:
    check_cards()
    round +=1

multiplier = []
result =0
for x in range(len(winner()),0, -1):
    multiplier.append(x)
for x in range(len(winner())):
    result+= winner()[x] * multiplier[x]
print(result)