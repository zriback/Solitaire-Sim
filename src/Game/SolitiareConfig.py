"""
Represents the current state of the game of solitaire
Represents the current configuration
Also gives functionality for finding all the next legal moves, and is able to generate solitaire games that stem from
    those legal moves
Author: Zach Riback
"""
import random
from collections import deque
from random import random
import copy

from src.Game.Card import Card
from src.Game.Foundation import Foundation
from src.Game.Hand import Hand
from src.Game.Tableau import Tableau


class SolitaireConfig:

    def __init__(self, starting_deck=""):
        # make the deck from which the field will be dealt
        self.deck = SolitaireConfig.make_deck(starting_deck)

        # now the tableau is dealt out
        self.tableau = Tableau()
        self.tableau.initial_deal(self.deck)
        self.hand = Hand(self.deck)
        self.foundation = Foundation()

    @staticmethod
    def make_deck(starting_deck: str) -> 'deque':
        if starting_deck == "":  # use the starting deck config given in this file
            with open('../Data/default_deck.txt') as f:
                cards = f.readline().split(' ')
                random.shuffle(cards)
        else:
            cards = starting_deck.split(' ')

        # now add all the cards to the queue
        q = deque()
        for card in cards:
            ID = Card.find_ID(card)
            q.append(Card(ID))

        return q

    def get_successors(self) -> list['SolitaireConfig']:
        """
        Finds all legal moves and generates the resulting configs from playing those moves
        :return: A list of SolitaireConfigs representing the games stemming from playing each legal move that it finds
        """
        # first make a deep copy of this solitaire config
        clone = copy.deepcopy(self)

        # moving cards within the tableau
        first_cards = self.tableau.get_first_cards()
        for card in first_cards:
            if Tableau.check_valid_tableau_parent()


        # moving cards from the tableau to the foundation


        # moving cards from the stock


        # moving cards from the foundation to the tableau (sometimes legal to do this)



    def __str__(self):
        """
        Gets string representation of a solitaire config
        :return: string representation of a SolitaireConfig
        """
        return str(self.foundation) + str(self.tableau) + str(self.hand)


if __name__ == "__main__":
    pass

