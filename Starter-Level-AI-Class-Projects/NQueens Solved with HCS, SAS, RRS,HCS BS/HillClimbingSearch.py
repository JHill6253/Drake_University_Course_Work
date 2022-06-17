"""
HillClimbingSearch
"""

import time

class HillClimbingSearch():

    def __init__(self, problem):
        self.problem = problem
        self.rounds = 0
        self.timeSpent = 0

    """
    hill climbing search 
    initial state is the initial state as defined in the problem supplied in the __init__
    """
    def search(self):
        return self.hillclimb(self.problem.initial)

    """
    Conducts Hill Climbing Search from a given start state.
    state: the start state for the search
    """
    def hillclimb(self, startState):
        startTime = time.time()

        # create a node for the state;
        state = startState
        bestCost = self.problem.cost(state)

        madeAMove = True

        while madeAMove == True:
            self.rounds += 1
            madeAMove = False

            # expand neighbors
            for neighbor in self.problem.actions(state):
                cost = self.problem.cost(neighbor)
                if cost < bestCost:
                    bestCost = cost
                    madeAMove = True
                    state = neighbor
            print(self.rounds, state, bestCost)
        self.timeSpent = time.time() - startTime

        return state





