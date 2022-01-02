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
        while len(self.queue) > 0 and not self.queue[0].is_win():
            # print("queue length: " + str(len(self.queue)))
            num += 1
            # print()
            # print()
            print('Number of current config: ' + str(num))
            # print('Queue length: ' + str(len(self.queue)))
            current = self.queue.popleft()
            # print(str(current))
            config_added = False
            successors = current.get_successors()
            added = 0
            # print('------------------------------------------------')
            for index in range(len(successors)):
                if successors[index] not in self.map:
                    if index == len(successors) - 1:
                        if not config_added or True:
                            self.map[successors[index]] = current
                            self.queue.append(successors[index])
                            added += 1
                            # print(successors[index])
                            # print('--------')
                    else:
                        self.map[successors[index]] = current
                        self.queue.append(successors[index])
                        config_added = True
                        added += 1
                        # print(successors[index])
                        # print('--------')
            if added == 0:
                pass
                # print('Added nothing to the queue from this config.')
            # print("Unique successors added from this config: " + str(added))
            # print('-----------------------------------------------------')

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
