import os
from collections import deque
from src.Game.Tableau import Tableau
from src.Game.SolitiareConfig import SolitaireConfig
from src.Simulation.Solver import Solver
from src.Game.Hand import Hand
from src.Game.Card import Card
import copy


def main():
    s = SolitaireConfig()
    print(str(s))
    solver = Solver(s)
    steps = solver.solve()

    if len(steps) == 0:
        print('Unsolvable')
    else:
        step_num = 0
        for step in steps:
            print('Step: ' + str(step_num))
            print(str(step))
            print()
            step_num += 1



if __name__ == "__main__":
    main()
