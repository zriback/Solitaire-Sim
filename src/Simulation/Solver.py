from collections import deque
from src.Game.SolitiareConfig import SolitaireConfig
import copy

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
        max_cards_in_foundation = 0
        num = 0
        total_added_to_queue = 0
        while len(self.queue) > 0 and not self.queue[0].is_win():
            current = self.queue.popleft()
            # print(str(current))
            config_added = False
            successors = current.get_successors()
            added = 0

            if current.foundation.get_num_cards() > max_cards_in_foundation:
                max_cards_in_foundation = current.foundation.get_num_cards()

            for index in range(len(successors)):
                if successors[index] not in self.map:
                    if index == len(successors) - 1:
                        if not config_added or True:
                            self.map[successors[index]] = current
                            self.queue.append(successors[index])
                            added += 1

                    else:
                        self.map[successors[index]] = current
                        self.queue.append(successors[index])
                        config_added = True
                        added += 1
            total_added_to_queue += added

            num += 1

            # PRUNING
            # every once in a while get rid of configs in the queue that do not have very many cards in the foundation
            if total_added_to_queue > 1000:
                queue_copy = copy.copy(self.queue)
                for config in queue_copy:
                    if config.foundation.get_num_cards() < max_cards_in_foundation - 3:
                        self.queue.remove(config)
                total_added_to_queue = 0

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
