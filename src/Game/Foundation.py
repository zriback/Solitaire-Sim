from collections import deque
import collections
from src.Game.Card import Card


class Foundation:
    """
    Stores information about the Foundation, or the four piles at the top
    The game is won when all the cards are in the foundation
    """

    def __init__(self):
        self.piles = []
        for _ in range(4):
            self.piles.append(deque())

    # def valid_spot(self, card: 'Card') -> bool:
    #     """
    #     Given a card determines if there is a valid place for it in the foundation piles
    #     :param card: the given card
    #     :return: true if there is a valid place, false otherwise
    #     """
    #     for pile in self.piles:
    #         if card.get_value() == 0 and len(pile) == 0:  # the card is an ace and the pile is empty
    #             return True
    #         elif len(pile) != 0 and Card.check_valid_foundation_parent(card, pile[-1]):
    #             return True

    @staticmethod
    def check_valid_parent(child: 'Card', parent: 'Card') -> bool:
        """
        Checks if two cards can be in a valid child - parent relationship in the foundation
        :param child: Card checking to be the child
        :param parent: Card checking to be the parent
        :return: True if valid relationship, false otherwise
        """
        if child is None or parent is None:
            return False
        else:
            return child.get_suit() == parent.get_suit() and child.get_value() == parent.get_value() + 1

    def get_last_cards(self):
        """
        Gets a list of the last Cards in the foundation piles
        A None object in the list denotes an empty pile (no cards in the pile)
        :return: A list of the last cards in the foundation piles
        """
        last_cards = []
        for pile in self.piles:
            if len(pile) != 0:
                last_cards.append(pile[-1])
            else:
                last_cards.append(None)
        return last_cards

    def __str__(self):
        """
        Gets a string representation of the foundation
        :return: A string representation of the foundation piles
        """
        result = ''
        for pile in self.piles:
            result += "Foundation: "
            for card in pile:
                result += str(card)
            result += '\n'
        return result

    def __hash__(self) -> int:
        """
        Gets the hashcode for this foundation using the cards in all the piles
        :return: hash for this foundation
        """
        hashcode = 0
        for pile in self.piles:
            hashcode += hash(tuple(pile))
        return hashcode


if __name__ == '__main__':
    pass
