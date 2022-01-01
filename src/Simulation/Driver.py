import os
from collections import deque
from src.Game.Tableau import Tableau
from src.Game.SolitiareConfig import SolitaireConfig
from src.Simulation.Solver import Solver
from src.Game.Hand import Hand
from src.Game.Card import Card
import copy
import sys
import time


def main():
    won = 0
    total = 0

    start_time = time.time()
    for _ in range(1):
        s = SolitaireConfig()
        solver = Solver(s)
        if solver.solve() is not None:
            won += 1
        total += 1

    print('Winning %: ' + str((won/total)*100))
    print('Execution took ' + str(time.time() - start_time) + ' seconds')



if __name__ == "__main__":
    main()
