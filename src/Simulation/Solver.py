from collections import deque
from src.Game.SolitiareConfig import SolitaireConfig


class Solver:
    """
    Class to handling the solving of the SolitairePuzzle
    Uses Breadth First Search (BFS) algorithm to find the shortest amount of steps in order to solve the puzzle
    """
    def __init__(self, config: 'SolitaireConfig'):
        # queue that keeps track of configs that still need to be looked at by the solver
        self.queue = deque()
        self.queue.append(config)

        # predecessor map used for keeping track of already visited configs and building the step path at the end
        self.map = {config: None}

    def solve(self) -> list['SolitaireConfig'] or None:
        """
        Starts the solving of the SolitaireGame. Attempts to find a path from the starting config to a won game state
        :return: list of SolitaireConfigs representing steps to reach the solution. If no solution could be found,
            returns None
        """
        num = 0
        amount_max = 3
        while len(self.queue) > 0 and not self.queue[0].is_win():
            amount = 0
            print("queue length: " + str(len(self.queue)))
            num += 1
            # print(str(num))
            current = self.queue.popleft()
            # print(str(current) + "\n\n ")

            successors = current.get_successors()
            for config in successors:
                if config not in self.map.keys():
                    amount += 1
                    self.map[config] = current
                    self.queue.append(config)

                    # only add one
                    if amount >= amount_max:
                        break

        # if the queue is empty then a solution was never found
        if len(self.queue) == 0:
            return None
        else:
            steps = deque()
            steps.appendleft(self.queue[0])
            next_step = self.map.get(self.queue[0])
            while next_step is not None:
                steps.appendleft(next_step)
                next_step = self.map.get(next_step)
            return list(steps)

    def solve_dfs(self, config: 'SolitaireConfig'):

        if config.is_win():
            return True
        else:
            for successor in config.get_successors():
                sol = self.solve_dfs(successor)
                if sol:
                    return True
        return False
