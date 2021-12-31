class Card:
    """
    Defines a card, which has a value, ace through king (0 - 12), and a suit (spade, heart, diamond, club)
    and a Color black (0) or red (1)
    This is all represented with a single number 0-51, known as the ID
    To get the suit from the ID:
        ID // 13:
        = 0 - spade
        = 1 - heart
        = 2 - diamond
        = 3 - club
    To get the value from the ID
        ID % 13
        = 0 - ace
        = 1 - two
        ...
        = 11 - queen
        = 12 - king
    To get the color from the ID
        ID // 13 == 0 or 3 is BLACK (0)
        ID // 13 == 1 or 2 is RED (1)

        The card can also either be face up (+) or face down (-)
    """
    suits = {
        "S": 0,
        "H": 1,
        "D": 2,
        "C": 3
    }

    values = {
        "A": 0,
        "2": 1,
        "3": 2,
        "4": 3,
        "5": 4,
        "6": 5,
        "7": 6,
        "8": 7,
        "9": 8,
        "10": 9,
        "J": 10,
        "Q": 11,
        "K": 12,
    }

    def __init__(self, ID: int) -> None:
        """
        Creates a card with the given ID, starts face down
        :param ID: ID for the new Card
        """
        self.ID = ID
        self.faceup = False

    def flip(self) -> 'Card':
        """ Flips the Card over and returns it"""
        self.faceup = not self.faceup
        return self

    def get_color(self) -> int:
        """
        Returns value based on if this card is black (spade, club) or red (heart, diamond)
        :return: 0 if black, 1 if red
        """
        if self.get_suit() == 0 or self.get_suit() == 3:
            return 0  # black
        else:
            return 1  # red

    @staticmethod
    def check_valid_tableau_parent(child: 'Card', parent: 'Card') -> bool:
        """
        Checks if two cards can be in a valid child - parent relationship in the tableau
            it is valid if the parent's value is one higher and is the opposite color
        :param child: Card checking to be the child
        :param parent: Card checking to be the parent
        :return: True if valid relationship, false otherwise
        """
        return child.get_color() != parent.get_color() and child.get_value() == parent.get_value() - 1

    @staticmethod
    def check_valid_foundation_parent(child: 'Card', parent: 'Card') -> bool:
        """
        Checks if two cards can be in a valid child - parent relationship in the foundation
        :param child: Card checking to be the child
        :param parent: Card checking to be the parent
        :return: True if valid relationship, false otherwise
        """
        return child.get_suit() == parent.get_suit() and child.get_value() == parent.get_value() + 1

    @staticmethod
    def find_ID(card_string: str) -> int:
        """
        Takes the string representation of a Card and find the ID associated with it
        :param card_string: string representation of the card
        :return: ID of the card from 0 to 51
        """
        card_string.strip('+-')
        ID = 0

        ID += Card.suits.get(card_string[-1]) * 13
        ID += Card.values.get(card_string[:-1])

        return ID

    def get_value(self) -> int:
        """
        Calculates the numeric equivalent for the value of this card using the ID
        :return: the value
        """
        return self.ID % 13

    def get_suit(self) -> int:
        """
        Calculates the numeric equivalent of the suit for this card using the ID
        :return: the suit
        """
        return self.ID // 13

    def __str__(self) -> str:
        """
        Translates the card into something to be printed out
        :return: str representation of the Card
        """
        result = ''
        suit = self.get_suit()
        value = self.get_value()

        result += list(Card.values.keys())[list(Card.values.values()).index(value)]
        result += list(Card.suits.keys())[list(Card.suits.values()).index(suit)]

        if self.faceup:
            result += '+'
        else:
            result += '-'
        return '[' + result + ']'


if __name__ == "__main__":
    pass
