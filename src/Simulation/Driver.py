from src.Game.SolitiareConfig import SolitaireConfig
from src.Simulation.Solver import Solver
from src.Simulation.MultiSolver import MultiSolver


def main():

    # s = SolitaireConfig(deck)
    # solver = Solver(s)
    # solver.set_verbose(True)
    # steps = solver.solve()
    #
    # if steps is None:
    #     print('No solution')
    # else:  # then there was a solution
    #     step_num = 0
    #     for step in steps:
    #         print('Step ' + str(step_num))
    #         print(str(step) + '\n\n')
    #         step_num += 1

    ms = MultiSolver(30, 10)  # x games using y threads
    ms.start()


if __name__ == "__main__":
    main()
