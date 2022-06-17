"""
RandomRestartSearch
"""


import time

class RandomRestartSearch:

    def __init__(self, problem, restarts):
        # input the problem and the number of restarts
        self.problem = problem
        self.rounds = 0
        self.timeSpent = 0
        self.numberOfRestarts = restarts

    """
    Searches for a state from the initial state of the problem using Random Restart
      uses self.numberOfRestarts
    """
    def search(self):


        for i in range(self.numberOfRestarts):
            print("restarting")
            startTime = time.time()
            statehold = self.problem.shuffle(self.problem.initial)
            bestCost = self.problem.cost(statehold)
            madeAMove = True



            while madeAMove == True:
                self.rounds += 1
                madeAMove = False

                # expand neighbors
                for neighbor in self.problem.actions(statehold):
                    cost = self.problem.cost(neighbor)
                    if cost < bestCost:
                        bestCost = cost
                        madeAMove = True
                        statehold = neighbor
                print(self.rounds, statehold, bestCost)
            self.timeSpent = time.time() - startTime

        return statehold








