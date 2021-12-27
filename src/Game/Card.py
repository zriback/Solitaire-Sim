
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
        if self.suit == 0 or self.suit == 3:
            return 0  # black
        else:
            return 1  # red

    def is_valid_parent(self, other: 'Card') -> bool:
        """
        Checks if another card is a valid parent for this card, i.e. they are different colors
        :param other: Card we are checking as the parent of this one
        :return: True if valid parent, false otherwise
        """
        if self.get_color() != other.get_color():
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


    def __str__(self):
        """
        Translates the card into something to be printed out
        :return: str representation of the Card
        """
        result = ''
        suit = self.ID // 13
        value = self.ID % 13

        if value == 0:
            result += 'A'
        elif value == 10:
            result += 'J'
        elif value == 11:
            result += 'Q'
        elif value == 12:
            result += 'K'
        else:
            result += str(value+1)

        if suit == 0:
            result += 'S'
        elif suit == 1:
            result += 'H'
        elif suit == 2:
            result += 'D'
        elif suit == 3:
            result += 'C'

        if self.faceup:
            result += '+'
        else:
            result += '-'

        return result


Card.get_color()
c = Card(0)
c.get_color()
