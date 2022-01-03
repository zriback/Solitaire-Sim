from src.Game.SolitiareConfig import SolitaireConfig
from src.Simulation.Solver import Solver


def main():

    # fast_deck = "['JS', 'AD', '2D', 'KC', '9H', '9D', '6D', 'KH', 'QC', '5D', 'KS', 'AS', '4S', '10C', 'KD', '10D', 'QH', '5H', '10S', 'AC', '8H', '8C', '6S', 'JD', '2C', 'JC', '10H', '5S', '6H', '3S', 'AH', '7D', 'JH', '5C', '8S', '4D', '3D', '7H', '2S', '4H', '2H', '9S', '3C', '4C', '7S', '3H', '6C', '8D', 'QS', 'QD', '7C', '9C']\ n "

    # this deck took 187 seconds with a threshold of 2 with only foundation pruning
    # thresh2_deck = "['10C', '4S', '9C', '6H', '10H', 'KD', '8H', 'QS', 'JC', '8D', 'AS', '2S', '2C', '6C', 'KS', 'JD', '2H', '5H', 'KC', 'QC', '3C', '3S', '10D', '6S', 'JS', '7D', '5S', '2D', '6D', 'AC', '4C', '8C', '4H', '5C', 'AH', 'AD', '3H', '5D', '7C', '3D', 'QD', '4D', '10S', 'KH', '7S', 'JH', '9H', '9D', '9S', '7H', '8S', 'QH']\ n"

    # deck = "6C KH 10D 4S 2S 10C AD 4D 9C 4C 3D 10S JH 6D 3H 9D 9H AH 6S 3C 8H 7C 5H 4H 7H KD 8C 2H 2D 10H 7S 8S " \
    #        "5D AS 2C KS 9S 5C 3S JC JD QD JS AC QC 8D QH QS 5S 6H 7D KC"

    # deck = "2S 9C 4H KS 2D QC 10C QH JC 8S 9S KD 6D 10D 5S KH 7C 7S AH 4D 8H 8D 3S JD AS 6S 3D 5C 6H JH 5D 9H 3C AD " \
    #             "7H JS QS 2H 4S 4C 9D AC 6C 10H QD 10S 7D 5H 2C 8C 3H KC"
    #
    # s = SolitaireConfig(deck)
    # solver = Solver(s)
    # solver.set_verbose(True)
    # solver.set_pruning_threshold(3)
    #
    # steps = solver.solve()

    # deck = "2S 9C 4H KS 2D QC 10C QH JC 8S 9S KD 6D 10D 5S KH 7C 7S AH 4D 8H 8D 3S JD AS 6S 3D 5C 6H JH 5D 9H 3C AD " \
    #        "7H JS QS 2H 4S 4C 9D AC 6C 10H QD 10S 7D 5H 2C 8C 3H KC"
    #
    s = SolitaireConfig()

    solver3 = Solver(s)
    solver3.set_pruning_threshold(3)

    solver2 = Solver(s)
    solver2.set_pruning_threshold(2)

    solver1 = Solver(s)
    solver1.set_pruning_threshold(1)

    solver0 = Solver(s)
    solver0.set_pruning_threshold(0)

    if solver0.solve() is not None:
        print('Solved using a threshold of 0.\n')
    else:
        print('No solution found using a threshold of 0.\n')

    if solver1.solve() is not None:
        print('Solved using a threshold of 1.\n')
    else:
        print('No solution found using a threshold of 1.\n')

    if solver2.solve() is not None:
        print('Solved using a threshold of 2.\n')
    else:
        print('No solution found using a threshold of 2.\n')

    if solver3.solve() is not None:
        print('Solved using a threshold of 3.\n ')
    else:
        print('No solution found using a threshold of 3.\n')

    # if steps is None:
    #     print('No solution')
    # else:  # then there was a solution
    #     step_num = 0
    #     for step in steps:
    #         print('Step ' + str(step_num))
    #         print(str(step) + '\n\n')
    #         step_num += 1


if __name__ == "__main__":
    main()
