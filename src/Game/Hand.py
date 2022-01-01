from collections import deque
from src.Game.Card import Card
import collections


class Hand:
    """
    Represents the deal pile from which new cards are added into the game
    Represented by two piles, one of face down cards (stock) and the other the face up already dealt cards (waste)
    """

    def __init__(self, deck: deque['Card'], deal_amount=3):
        """
        Creates the stock and waste piles
        :param deck: Deck given that will become the stock pile in the beginning
        :param deal_amount: Amount of cards to turn over when dealing new cards to the waste pile. Default is 3
            For easy mode use 1, for a harder game use 3
        """
        self.stock = deck
        self.waste = deque()
        self.deal_amount = deal_amount

    def deal(self) -> None:
        """
        Deals out a certain number of cards
        :return: None
        """
        for i in range(self.deal_amount):
            # move card from stock to the waste pile
            if len(self.stock) == 0:
                self.reset_stock()
            self.waste.appendleft(self.stock.popleft().flip())

    def reset_stock(self) -> None:
        """
        Moves all cards in the waste pile to the stock pile
        Uses when the stock is empty
        :return: None
        """
        # first slip over every card to being face down again
        for card in self.waste:
            card.flip()
        # extending left has the same effect as extending to the right and reversing
        self.stock.extendleft(self.waste)
        self.waste.clear()

    def get_card(self) -> 'Card' or None:
        """
        Accessor method for the top card in the waste pile
        :return: the top face up card from the waste pile
        """
        if len(self.waste) != 0:
            return self.waste[0]
        else:
            return None

    def take_card(self) -> 'Card':
        """
        Gets but also removes the top card from the waste pile
        :return: top face up card from the waste pile
        """
        return self.waste.popleft()

    def __str__(self) -> str:
        """
        Gets string representation for the Hand
        :return: String representation
        """
        result = 'Stock: '
        for card in self.stock:
            result += str(card)
        result += '\nWaste: '
        for card in self.waste:
            result += str(card)
        return result

    def __hash__(self) -> int:
        """
        Compute the hash code for this hand by hashing all the cards in the stock and waste
        :return: the hash code
        """
        return hash(tuple(self.stock)) + hash(tuple(self.waste))


if __name__ == '__main__':
    pass
