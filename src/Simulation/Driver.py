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
    deck = '2S 9C QH 4H JC 10D KS 8S 5S AH 2D 9S KH 4D 3S QC KD 7C 8H JD 6S 10C 6D 7S 8D AS 3D 5C 6H JH 5D 9H 3C AD 7H JS QS 2H 4S 4C 9D AC 6C 10H QD 10S 7D 5H 2C 8C 3H KC'

    s = SolitaireConfig(deck)
    solver = Solver(s)
    start_time = time.time()
    steps = solver.solve()

    if steps is None:
        print('No solution')
    else:
        step_num = 0
        for step in steps:
            print('Step ' + str(step_num))
            print(str(step) + '\n\n')
            step_num += 1

    print('Execution took ' + str(time.time() - start_time) + ' seconds')




if __name__ == "__main__":
    main()
