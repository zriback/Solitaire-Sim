import os
from collections import deque
from src.Game.Tableau import Tableau
from src.Game.SolitiareConfig import SolitaireConfig
from src.Game.Hand import Hand
from src.Game.Card import Card
import copy


def main():
    s = SolitaireConfig()
    print(str(s))
    sucs = s.get_successors()

    for suc in sucs:
        print(str(suc))


if __name__ == "__main__":
    main()
