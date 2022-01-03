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
                print(str(cards) + '\ n')

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
        foundation_last_cards = self.foundation.get_last_cards()
        hand_card = self.hand.get_card()

        # moving cards from the tableau to the foundation
        # moving cards within the tableau
        # moving stacks within the tableau
        for i in range(len(last_cards)):
            for j in range(len(foundation_last_cards)):
                if Foundation.check_valid_parent(last_cards[i], foundation_last_cards[j]):
                    clone = copy.deepcopy(self)
                    # take the i (child) card and move it to the foundation at the end of pile j
                    clone.foundation.put_card(clone.tableau.take_card(i), j)
                    successors.append(clone)
                    # if card found a valid parent in the foundation, it does not need to keep searching
                    break
            else:  # for loop finished without finding a place in the foundation, so now look in tableau
                if first_cards[i] == last_cards[i]:  # single card can be moved by itself
                    for j in range(len(last_cards)):
                        if Tableau.check_valid_parent(last_cards[i], last_cards[j]):
                            clone = copy.deepcopy(self)
                            # takes the i (child) card and moves it under the j (parent) card
                            clone.tableau.put_card(clone.tableau.take_card(i), j)
                            successors.append(clone)
                            # if a card found a place in the tableau, no point in moving it to another card in the tableau
                            #   just one is enough, so break
                            break
                else:  # long stack must be moved together
                    for j in range(len(last_cards)):
                        if Tableau.check_valid_parent(first_cards[i], last_cards[j]):
                            clone = copy.deepcopy(self)
                            clone.tableau.move_pile(i, j)
                            successors.append(clone)
                            break

        # moving cards from the hand (left over cards)
        # one move is to either take one card from the waste pile and play it, or to deal out more cards from the stock
        #   into the waste pile.
        if hand_card is not None:
            # no point in putting ace in the tableau from the hand
            for i in range(len(foundation_last_cards)):
                if Foundation.check_valid_parent(hand_card, foundation_last_cards[i]):
                    clone = copy.deepcopy(self)
                    clone.foundation.put_card(clone.hand.take_card(), i)
                    successors.append(clone)
                    break
            else:
                for i in range(len(last_cards)):
                    if Tableau.check_valid_parent(hand_card, last_cards[i]):
                        clone = copy.deepcopy(self)
                        clone.tableau.put_card(clone.hand.take_card(), i)
                        successors.append(clone)
                        break

        # moving cards from the foundation to the tableau (depending on the rules you're allowed to do this)
        for i in range(len(foundation_last_cards)):
            # if the card is an ace or a two, there is no point in moving it back down to the tableau, so skip this loop
            if foundation_last_cards[i] is not None and (foundation_last_cards[i].get_value() == 0
                                                         or foundation_last_cards[i].get_value() == 1):
                continue
            for j in range(len(last_cards)):
                if Tableau.check_valid_parent(foundation_last_cards[i], last_cards[j]):
                    clone = copy.deepcopy(self)
                    # take the i (child) card from the foundation pile and move it to the end of the jth tableau pile
                    clone.tableau.put_card(clone.foundation.take_card(i), j)
                    successors.append(clone)
                    break

        if self.hand.has_cards():
            clone = copy.deepcopy(self)
            clone.hand.deal()
            successors.append(clone)

        return successors

    def is_win(self) -> bool:
        """
        Finds if the game has been won
        The game is won if the last card in all the foundation piles is the king (has a value of 12)
        :return: true if the game is won, false otherwise
        """
        for card in self.foundation.get_last_cards():
            if card is None or card.get_value() != 12:
                return False
        return True

    def __str__(self):
        """
        Gets string representation of a solitaire config
        :return: string representation of a SolitaireConfig
        """
        return str(self.foundation) + str(self.tableau) + str(self.hand)

    def __hash__(self):
        return hash(self.tableau) + hash(self.foundation) + hash(self.hand)

    def __eq__(self, other) -> bool:
        """
        Method for determining equality between two SolitaireConfigs
        Two SolitaireConfigs are equal if their hands, tableaus, and foundations are equal
        :param other: other SolitaireConfig to compare with
        :return: True if they are equal, false otherwise
        """
        return isinstance(other, SolitaireConfig) and self.hand == other.hand and self.foundation == other.foundation and self.tableau == other.tableau


if __name__ == "__main__":
    pass

