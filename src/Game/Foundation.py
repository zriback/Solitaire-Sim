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

    @staticmethod
    def check_valid_parent(child: 'Card', parent: 'Card') -> bool:
        """
        Checks if two cards can be in a valid child - parent relationship in the foundation
        :param child: Card checking to be the child
        :param parent: Card checking to be the parent
        :return: True if valid relationship, false otherwise
        """
        if child is None:
            return False
        elif parent is None:
            return child.get_value() == 0
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

    def put_card(self, card: 'Card', index: int) -> None:
        """
        Puts a card at the end of one of the piles in the foundation
        :param card: the card to add
        :param index: the index of the pile to add the card at the end of
        :return: None
        """
        self.piles[index].append(card)

    def take_card(self, index: int) -> 'Card':
        """
        Takes card from the end of the given pile
        :param index: index of the pile to take from
        :return: the card taken from the end of the pile
        """
        return self.piles[index].pop()

    def get_num_cards(self) -> int:
        """
        Gets the total number of cards in the foundation
        :return: total number of cards in the foundation
        """
        cards = 0
        for pile in self.piles:
            cards += len(pile)
        return cards

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

    def __eq__(self, other) -> bool:
        """
        Method for determining equality between two Foundations
        Two foundations are equal if all the piles are the same
            the order the piles are in should not matter
        :param other: other foundation to compare to
        :return: True if foundations are equal, false otherwise
        """
        return isinstance(other, Foundation) and (len(self.piles) == len(other.piles) and
                                                  all(x in self.piles for x in other.piles))


if __name__ == '__main__':
    pass
