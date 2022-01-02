from src.Game.SolitiareConfig import SolitaireConfig
from src.Simulation.Solver import Solver


def main():

    deck = "2S 9C 4H KS 2D QC 10C QH JC 8S 9S KD 6D 10D 5S KH 7C 7S AH 4D 8H 8D 3S JD AS 6S 3D 5C 6H JH 5D 9H 3C AD " \
           "7H JS QS 2H 4S 4C 9D AC 6C 10H QD 10S 7D 5H 2C 8C 3H KC"

    s = SolitaireConfig(deck)

    solver3 = Solver(s)
    solver3.set_pruning_threshold(3)

    solver2 = Solver(s)
    solver2.set_pruning_threshold(2)

    solver1 = Solver(s)
    solver1.set_pruning_threshold(1)

    solver0 = Solver(s)
    solver0.set_pruning_threshold(0)

    steps = None

    #

    if steps is None:
        print('No solution')
    else:  # then there was a solution
        step_num = 0
        for step in steps:
            print('Step ' + str(step_num))
            print(str(step) + '\n\n')
            step_num += 1


if __name__ == "__main__":
    main()
