import os
from collections import deque
from src.Game.Tableau import Tableau
from src.Game.SolitiareConfig import SolitaireConfig
from src.Game.Hand import Hand


def main():
    s = SolitaireConfig()
    t = Tableau()
    t.initial_deal(s.deck)
    print(t)

    h = Hand(s.deck)
    print(h)


if __name__ == "__main__":
    main()
