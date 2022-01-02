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
        Deals it out how a normal human would in a real solitaire game, putting one card on each pile in each pass
        :return: None
        """
        for i in range(7):
            for j in range(i, 7):
                if i == j:
                    self.piles[j].append(deck.popleft().flip())
                else:
                    self.piles[j].append(deck.popleft())

    @staticmethod
    def check_valid_parent(child: 'Card', parent: 'Card') -> bool:
        """
        Checks if two cards can be in a valid child - parent relationship in the tableau
            it is valid if the parent's value is one higher and is the opposite color
            Also valid if child is a king and parent is None
        :param child: Card checking to be the child
        :param parent: Card checking to be the parent
        :return: True if valid relationship, false otherwise
        """
        if child is None:
            return False
        elif parent is None:
            return child.get_value() == 12  # if it is a king the relationship is valid
        else:
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
                    if card.is_faceup():
                        first_cards.append(card)
                        break
            else:
                first_cards.append(None)
        return first_cards

    def put_card(self, card: 'Card', index: int) -> None:
        """
        Puts a given card into the tableau at the end of the given pile
        :param card: the card to put into the tableau
        :param index: index of the pile to put the new card
        :return: None
        """
        self.piles[index].append(card)

    def take_card(self, index: int) -> 'Card':
        """
        Gets the last card from the pile with the associated index
        Flips over the last card to being face up if there is one
        :param index: index of pile to get the card from
        :return: the last card from the pile with the above index
        """
        card = self.piles[index].pop()
        if len(self.piles[index]) != 0 and not self.piles[index][-1].is_faceup():
            self.piles[index][-1].flip()
        return card

    def move_pile(self, from_index: int, to_index: int) -> None:
        """
        Moves all the face up cards from one pile to the end of another pile
        :param from_index: pile to move the cards from
        :param to_index: pile to move the cards to
        :return: None
        """
        cards = deque()
        while len(self.piles[from_index]) > 0 and self.piles[from_index][-1].is_faceup():
            cards.appendleft(self.piles[from_index].pop())
        if len(self.piles[from_index]) != 0:
            self.piles[from_index][-1].flip()
        self.piles[to_index].extend(cards)

    def __str__(self) -> str:
        """
        Gets a string representation for this tableau
        :return: a string that represents the cards in the tableau
        """
        result = ''
        for pile in self.piles:
            for card in pile:
                result += str(card)
            result += '\n'
        return result

    def __hash__(self):
        """
        Gets the hash for this tableau using the cards in all the piles
        :return: the hash for this tableau
        """
        hashcode = 0
        for pile in self.piles:
            hashcode += hash(tuple(pile))
        return hashcode

    def __eq__(self, other) -> bool:
        """
        Method for determining equality between two tableaus
        Two tableaus are equal if all the piles are equal
        :param other: other tableau to compare with
        :return: True if the tableaus are equal, false otherwise
        """
        return isinstance(other, Tableau) and (len(self.piles) == len(other.piles) and
                                               all(x in self.piles for x in other.piles))


if __name__ == '__main__':
    pass
