"""
Getting card values and suits
11 = J, 12 = Q, 13 = K, 14 = A
"""

import math
import random
import time

cardValues = list(range(2, 15))
suits = ["Clubs", "Diamonds", "Hearts", "Spades"]

faceCards = {
    "J": 11,
    "Q": 12,
    "K": 13,
    "A": 14,
    11: "J",
    12: "Q",
    13: "K",
    14: "A"
}


class Card:
    def __init__(self, value, suit):
        self._value = value
        self._suit = suit

    @property
    def getValue(self):
        return self._value

    @property
    def getSuit(self):
        return self._suit


def generateDeck(cardValues, suits):
    cards = []
    for value in cardValues:
        for suit in suits:
            if value in faceCards:
                _card = Card(faceCards[value], suit)
            else:
                _card = Card(value, suit)
            cards.append(_card)
    return cards


def shuffleDeck(cards):
    keepGoing = "y"
    while keepGoing == "y":
        numOfShuffles = input("How many times would you like the dealer to shuffle the deck?\t")
        if math.isnan(float(numOfShuffles)):
            print("I'm sorry, that is not a number. Please try again.")
            continue
        elif int(numOfShuffles) <= 0:
            print("I'm sorry, the deck must be shuffled at least once. Please try again.")
            continue
        else:
            print("\nCards are now being shuffled\n")
            for shuffle in range(int(numOfShuffles)):
                random.shuffle(cards)
                print("%d Shuffle..." % int(shuffle + 1))
                time.sleep(2)
            break


cards = generateDeck(cardValues, suits)

for card in cards:
    print(card.getValue, card.getSuit)

shuffleDeck(cards)

for card in cards:
    print(card.getValue, card.getSuit)
