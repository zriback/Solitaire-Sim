from collections import deque
from src.Game.Card import Card


class Tableau:

    def __init__(self):
        self.piles = []
        for _ in range(7):
            self.piles.append(deque())

    def deal(self, deck: deque['Card']) -> None:
        """
        Performs the initial deal given an initial deck to start from
        :return: None
        """
        for i in range(7):
            for j in range(i + 1):
                self.piles[i].append(deck.popleft())
            self.piles[i][-1].flip()  # flip the final card over to being face up

    def __str__(self):
        result = ''
        for pile in self.piles:
            for card in pile:
                result += str(card)
            result += '\n'
        return result


if __name__ == '__main__':
    pass
