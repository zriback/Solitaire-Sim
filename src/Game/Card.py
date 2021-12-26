
class Card:
    """
    Defines a card, which has a value, ace through king (0 - 12), and a suit (spade, heart, diamond, club)
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

        The card can also either be face up (+) or face down (-)
    """

    def __init__(self, ID):
        """
        Creates a card with the given ID, starts face down
        :param ID: ID for the new Card
        """
        self.ID = ID
        self.faceup = False

    def flip(self):
        """ Flips the Card over"""
        self.faceup = not self.faceup

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
