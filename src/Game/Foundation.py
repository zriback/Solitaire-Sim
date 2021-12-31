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

    def valid_spot(self, card: 'Card') -> bool:
        """
        Given a card determines if there is a valid place for it in the foundation piles
        :param card: the given card
        :return: true if there is a valid place, false otherwise
        """
        for pile in self.piles:
            if card.get_value() == 0 and len(pile) == 0:  # the card is an ace and the pile is empty
                return True
            elif len(pile) != 0 and Card.check_valid_foundation_parent(card, pile[-1]):
                return True

    def __str__(self):
        """
        Gets a string representation of the foundation
        :return: A string representation of the foundation piles
        """
        result = ''
        for pile in self.piles:
            for card in pile:
                result += str(card)
            result += '\n'
        return result


if __name__ == '__main__':
    pass
