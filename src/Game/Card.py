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

    def flip(self) -> None:
        """ Flips the Card over"""
        self.faceup = not self.faceup

    def get_color(self) -> int:
        """
        Returns value based on if this card is black (spade, club) or red (heart, diamond)
        :return: 0 if black, 1 if red
        """
        if self.ID // 13 == 0 or self.ID // 13 == 3:
            return 0  # black
        else:
            return 1  # red

    @staticmethod
    def check_valid_parent(card1: 'Card', card2: 'Card') -> bool:
        """
        Checks if two Cards are valid parents of each other
        :param card1: First card we are checking
        :param card2: Second card we are checking
        :return: True if valid parent, false otherwise
        """
        if card1.get_color() != card2.get_color():
            return True
        else:
            return False

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

    def __str__(self):
        """
        Translates the card into something to be printed out
        :return: str representation of the Card
        """
        result = ''
        suit = self.ID // 13
        value = self.ID % 13

        result += list(Card.values.keys())[list(Card.values.values()).index(value)]
        result += list(Card.suits.keys())[list(Card.suits.values()).index(suit)]

        if self.faceup:
            result += '+'
        else:
            result += '-'

        return result
