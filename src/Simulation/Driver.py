import os
from collections import deque
from src.Game.Tableau import Tableau
from src.Game.SolitiareConfig import SolitaireConfig
from src.Game.Hand import Hand
from src.Game.Card import Card
import copy


def main():
    # s = SolitaireConfig()
    # print(str(s))

    s1 = SolitaireConfig()
    s2 = copy.deepcopy(s1)

    s1.foundation.piles[0] = "5"
    print(s1)
    print(s2)


if __name__ == "__main__":
    main()
