import os
from collections import deque
from src.Game.Tableau import Tableau
from src.Game.SolitiareConfig import SolitaireConfig


def main():
    s = SolitaireConfig()
    t = Tableau()
    t.deal(s.deck)
    print(t)


if __name__ == "__main__":
    main()
