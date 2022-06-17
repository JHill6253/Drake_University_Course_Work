"""
SimulatedAnnealing Search
"""
import time
import random
from math import e


class SimulatedAnnealingSearch:

    def __init__(self, problem, startTemp, decAmount):
        # save the
        self.problem = problem
        self.rounds = 0
        self.timeSpent = 0
        self.startingTemp = startTemp
        self.decAmount = decAmount

    """
    Simulated Annealing search 
    initial state is the initial state as defined in the problem supplied in the __init__
    starting temperature
    decrement amount given as variables in __init__
    """

    def search(self):
        return self.simulatedAnnealing(self.problem.initial)

    """
    Conducts Simulated Annealing Search from a given start state.
    state: the start state for the search
    """
    def simulatedAnnealing(self, startState):
        startTime = time.time()
        temp = self.startingTemp
        state = startState
        while temp > 0:
            currentCost = self.problem.cost(state)
            neighbor = random.choice(self.problem.actions(state))
            nextCost = self.problem.cost(neighbor)
            diff = currentCost - nextCost

            randRoll = random.random()
            if diff > 0:
                state = neighbor
            elif randRoll < e**(diff/temp):
                state = neighbor
            temp -= self.decAmount

        self.timeSpent = time.time() - startTime
        return state








