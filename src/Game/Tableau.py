from collections import deque
from src.Game.Card import Card


class Tableau:
    """
    Represents the main seven piles in the game of solitaire
    """

    def __init__(self):
        self.piles = []
        for _ in range(7):
            self.piles.append(deque())

    def initial_deal(self, deck: deque['Card']) -> None:
        """
        Performs the initial deal given an initial deck to start from
        :return: None
        """
        for i in range(7):
            for j in range(i + 1):
                self.piles[i].append(deck.popleft())
            self.piles[i][-1].flip()  # flip the final card over to being face up

    def __str__(self) -> str:
        result = ''
        for pile in self.piles:
            for card in pile:
                result += str(card)
            result += '\n'
        return result

    @staticmethod
    def check_valid_parent(child: 'Card', parent: 'Card') -> bool:
        """
        Checks if two cards can be in a valid child - parent relationship in the tableau
            it is valid if the parent's value is one higher and is the opposite color
        :param child: Card checking to be the child
        :param parent: Card checking to be the parent
        :return: True if valid relationship, false otherwise
        """
        return child.get_color() != parent.get_color() and child.get_value() == parent.get_value() - 1

    def get_last_cards(self) -> list['Card']:
        """
        Gets a list of the last cards for all the piles in the tableau
        None object in the returns list signifies an empty pile (the absence of a pile)
        :return: A list of the the at max seven cards at the bottom of each pile
        """
        last_cards = []
        for pile in self.piles:
            if len(pile) != 0:
                last_cards.append(pile[-1])
            else:
                last_cards.append(None)
        return last_cards

    def get_first_cards(self) -> list['Card']:
        """
        Gets a list of the first (highest) face up cards in each pile
        A None object in the list signifies an empty pile (the absence of a pile in the tableau)
        :return: A list of the first face up cards in each pile from the tableau
        """
        first_cards = []
        for pile in self.piles:
            if len(pile) != 0:
                for card in pile:
                    if card.is_face_up():
                        first_cards.append(card)
                        break
            else:
                first_cards.append(None)
        return first_cards


if __name__ == '__main__':
    pass
