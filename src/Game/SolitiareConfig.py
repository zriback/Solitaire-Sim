'''
Represents the current state of the game of solitaire
Represents the current configuration
Also gives functionality for finding all the next legal moves, and is able to generate solitaire games that stem from
    those legal moves
Author: Zach Riback
'''
from queue import Queue
from queue import LifoQueue
from random import random


class SolitaireConfig:

    def __init__(self, starting_deck=""):
        self.deck = self.make_deck(starting_deck)

    def make_deck(self, starting_deck: str) -> 'Queue':
        if starting_deck != "":  # use the starting deck config given in this string
            with open('deck.txt') as f:
                starting_deck = f.readline()

        # now add all the cards to the cue


if __name__ == "__main__":
    pass

