"""
Represents the current state of the game of solitaire
Represents the current configuration
Also gives functionality for finding all the next legal moves, and is able to generate solitaire games that stem from
    those legal moves
Author: Zach Riback
"""
import random
from collections import deque
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
        successors = []
        last_cards = self.tableau.get_last_cards()
        first_cards = self.tableau.get_first_cards()

        # moving cards within the tableau
        for i in range(len(last_cards)):
            for j in range(len(last_cards)):
                if Tableau.check_valid_parent(last_cards[i], last_cards[j]):
                    clone = copy.deepcopy(self)
                    # takes the i (child) card and moves it under the j (parent) card
                    clone.tableau.put_card(clone.tableau.take_card(i), j)
                    successors.append(clone)

        # moving whole stacks within the tableau
        for i in range(len(first_cards)):
            for j in range(len(last_cards)):
                if Tableau.check_valid_parent(first_cards[i], last_cards[j]):
                    clone = copy.deepcopy(self)
                    clone.tableau.move_pile(i, j)
                    successors.append(clone)

        foundation_last_cards = self.foundation.get_last_cards()
        # moving cards from the tableau to the foundation
        for i in range(len(last_cards)):
            for j in range(len(foundation_last_cards)):
                if Foundation.check_valid_parent(last_cards[i], foundation_last_cards[j]):
                    clone = copy.deepcopy(self)
                    # take the i (child) card and move it to the foundation at the end of pile j
                    clone.foundation.put_card(clone.tableau.take_card(i), j)
                    successors.append(clone)

        # moving cards from the foundation to the tableau (depending on the rules you're allowed to do this)
        for i in range(len(foundation_last_cards)):
            for j in range(len(last_cards)):
                if Tableau.check_valid_parent(foundation_last_cards[i], last_cards[j]):
                    clone = copy.deepcopy(self)
                    # take the i (child) card from the foundation pile and move it to the end of the jth tableau pile
                    clone.tableau.put_card(clone.foundation.take_card(i), j)
                    successors.append(clone)

        # moving cards from the hand (left over cards)
        # one move is to either take one card from the waste pile and play it, or to deal out more cards from the stock
        #   into the waste pile.


        return successors

    def __str__(self):
        """
        Gets string representation of a solitaire config
        :return: string representation of a SolitaireConfig
        """
        return str(self.foundation) + str(self.tableau) + str(self.hand)

    def __hash__(self):
        return hash(self.tableau) + hash(self.foundation) + hash(self.hand)


if __name__ == "__main__":
    pass

