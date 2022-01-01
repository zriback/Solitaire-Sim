import os
from collections import deque
from src.Game.Tableau import Tableau
from src.Game.SolitiareConfig import SolitaireConfig
from src.Game.Hand import Hand
from src.Game.Card import Card
import copy


def main():
    s = SolitaireConfig()
    s.tableau.move_pile(2, 1)
    print(str(s))


if __name__ == "__main__":
    main()
