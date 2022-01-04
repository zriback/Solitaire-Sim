from collections import deque
from src.Game.SolitiareConfig import SolitaireConfig
import copy
import time


class Solver:
    """
    Class to handling the solving of the SolitairePuzzle
    Uses Breadth First Search (BFS) algorithm to find the shortest amount of steps in order to solve the puzzle
    Algorithm has been modified to prune away unlikely to win games in order to make it faster and feasible to run
    large amounts of games in reasonable amounts of time
    """
    def __init__(self, config: 'SolitaireConfig'):
        # queue that keeps track of configs that still need to be looked at by the solver
        self.queue = deque()
        self.queue.append(config)

        self.pruning_threshold = 2
        self.pruning_interval = 1000
        self.verbose = False

        # predecessor map used for keeping track of already visited configs and building the step path at the end
        self.map = {config: None}

    def solve(self) -> list['SolitaireConfig'] or None:
        """
        Starts the solving of the SolitaireGame. Attempts to find a path from the starting config to a won game state
        :return: list of SolitaireConfigs representing steps to reach the solution. If no solution could be found,
            returns None
        """
        start_time = time.time()

        max_cards_in_foundation = 0
        min_cards_in_hand = 24
        total_added_to_queue = 0
        total_configs_checked = 0
        while len(self.queue) > 0 and not self.queue[0].is_win():

            # just kill it if it is taking too long
            if time.time() - start_time > 500:
                print('Killed a solver.')
                break

            total_configs_checked += 1
            current = self.queue.popleft()
            successors = current.get_successors()
            added = 0

            self.verbose_print('\n\nTotal configs checked: ', total_configs_checked)
            self.verbose_print('Queue length: ', len(self.queue))
            self.verbose_print('Current config:\n', current)

            if current.foundation.get_num_cards() > max_cards_in_foundation:
                max_cards_in_foundation = current.foundation.get_num_cards()

            if current.hand.get_num_cards() < min_cards_in_hand:
                min_cards_in_hand = current.hand.get_num_cards()

            for successor in successors:
                if successor not in self.map:
                    self.map[successor] = current
                    self.queue.append(successor)
                    added += 1

            self.verbose_print('Successors added by this game: ', added)
            total_added_to_queue += added

            # PRUNING
            # every once in a while get rid of configs in the queue that do not have very many cards in the foundation
            if total_added_to_queue > self.pruning_interval:
                games_pruned = 0
                queue_copy = copy.copy(self.queue)
                for config in queue_copy:
                    # or config.hand.get_num_cards() > min_cards_in_hand + self.pruning_threshold
                    if config.foundation.get_num_cards() < max_cards_in_foundation - self.pruning_threshold:
                        self.queue.remove(config)
                        games_pruned += 1
                self.verbose_print('Games have been pruned out of the queue. Games pruned: ', games_pruned)
                self.verbose_print('Max cards in foundation: ', max_cards_in_foundation)

                total_added_to_queue = 0

        result = None
        if len(self.queue) != 0:  # then a solution was found
            steps = deque()
            steps.appendleft(self.queue[0])
            next_step = self.map.get(self.queue[0])
            while next_step is not None:
                steps.appendleft(next_step)
                next_step = self.map.get(next_step)
            result = list(steps)
        print('Execution took ' + str(time.time() - start_time) + ' seconds.')
        return result

    def set_verbose(self, value: bool) -> None:
        """
        Sets whether this solver will be verbose with output
        Defaults to False
        :param value: value for verbose (to set verbose to)
        :return: None
        """
        self.verbose = value

    def verbose_print(self, msg: str, value: any) -> None:
        """
        Conditional printing method depending on the value of self.verbose
        Mostly used for debugging or when more information is needed
        Note that printing slows down the solver
        :param msg: message to print with the value
        :param value: value to print along with the message
        :return: None
        """
        if self.verbose:
            print(msg + str(value))

    def set_pruning_threshold(self, value: int) -> None:
        """
        Sets the pruning threshold for discarding games with not enough cards in the foundation
        Defaults to 2
        :param value: value to set pruning threshold to
        :return: None
        """
        self.pruning_threshold = value

    def set_pruning_interval(self, value: int) -> None:
        """
        Sets the pruning interval for how often to prune the queue of configs
        Defaults to 1000
        :param value: value to set the interval to
        :return: None
        """
        self.pruning_interval = value


if __name__ == '__main__':
    pass
