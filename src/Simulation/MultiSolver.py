from multiprocessing import Process, Lock, Queue
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
        self.processes = []
        self.queue = Queue()
        for _ in range(num_threads):
            self.processes.append(Process(target=self.multi_solve, args=(amount//num_threads, self.queue)))

        self.total_won = 0
        self.total_played = 0

        self.lock = Lock()

    def start(self):
        """
        Starts a joins all threads
        :return: None
        """
        start_time = time.time()
        for process in self.processes:
            process.start()
        for process in self.processes:
            process.join()

        # read in results from the queue once everything has finished
        while not self.queue.empty():
            result = self.queue.get()
            if result:
                self.total_won += 1
            self.total_played += 1

        print('Execution complete. Total execution time was ' + str(time.time() - start_time) + ' seconds.')
        print('\nWon ' + str(self.total_won) + ' out of ' + str(self.total_played) + ' games.')
        print('Win rate: ' + str(self.total_won/self.total_played))

    def multi_solve(self, amount: int, queue: 'Queue') -> None:
        """
        Plays multiple solitaire games
        Results of games won and games played are added
        :param amount: amount of solitaire games to play
        :param queue: multi processing used to communicate results back to the original process
        :return: None
        """
        for _ in range(amount):
            solver = Solver(SolitaireConfig())
            solver.set_pruning_threshold(1)
            result = solver.solve()
            self.lock.acquire()
            if result is not None:  # then the game was won
                queue.put(True)
            else:
                queue.put(False)
            self.lock.release()

    # I have no idea why you have to do this but without it you get a "TypeError: Cannot pickle 'weakref' object"
    def __getstate__(self):
        state = self.__dict__.copy()
        state['processes'] = None
        return state
