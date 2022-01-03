import threading
from Solver import Solver
from src.Game.SolitiareConfig import SolitaireConfig
import time


class MultiSolver:
    """
    Class designed to use multiple threads of instances of the Solver class to more quickly play more games of solitaire
    """

    def __init__(self, amount: int, num_threads: int):
        """
        Initialize the multi solver
        :param num_threads: number of threads to make
        """
        self.threads = []
        for _ in range(num_threads):
            self.threads.append(threading.Thread(target=self.multi_solve, args=(amount//num_threads,)))

        self.total_won = 0
        self.total_played = 0

        self.lock = threading.Lock()

    def start(self):
        """
        Starts a joins all threads
        :return: None
        """
        start_time = time.time()
        for thread in self.threads:
            thread.start()
        for thread in self.threads:
            thread.join()
        print('Execution complete. Total execution time was ' + str(time.time() - start_time) + ' seconds.')
        print('\nWon ' + str(self.total_won) + ' out of ' + str(self.total_played) + ' games.')
        print('Win rate: ' + str(self.total_won/self.total_played))

    def multi_solve(self, amount: int) -> None:
        """
        Plays multiple solitaire games
        Results of games won and games played are adde
        :param amount: amount of solitaire games to play
        :return: None
        """
        for _ in range(amount):
            solver = Solver(SolitaireConfig())
            solver.set_pruning_threshold(0)
            result = solver.solve()
            self.lock.acquire()
            if result is not None:  # then the game was won
                self.total_won += 1
            self.total_played += 1
            self.lock.release()
        return None
