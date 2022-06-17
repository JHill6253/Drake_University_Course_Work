""""
Beam Search
"""

import time
import random
from queue import PriorityQueue

class BeamSearch:

    def __init__(self, problem, beamSize):
        # input the problem and the size of the beam
        self.problem = problem
        self.timeSpent = 0
        self.beamSize = beamSize

    """
    beam search 
    initial state is the initial state as defined in the problem supplied in the __init__
    """
    def search(self):
        return self.beamSearch(self.problem.initial)

    """
    Conducts Beam Search from a given start state.
    state: the start state for the search
    beam size is given in self.beamSize
    """
    def beamSearch(self, startState):
        startTime = time.time()
        beam = [startState]

        #add beamSize neighbors to beam
        for i in range(self.beamSize-1):
            neighbor = self.problem.shuffle(startState)
            beam.append(neighbor)

        madeAMove = True
        while madeAMove == True:
            madeAMove = False
            # for each beam, add all of the neighbors to the neighbors list
            neighborsList = PriorityQueue()

            for b in beam:
                for neighbor in self.problem.actions(b):
                    neighborsList.put((self.problem.cost(neighbor), neighbor))

            #lowest neighbor
            element = neighborsList.get()
            neighborScore = element[0]
            node = element[1]

            # what is the highest value in the beam?
            val = -float("inf")
            ndx = 0
            for i in range(len(beam)):
                if self.problem.cost(neighbor) > val:
                    val = self.problem.cost(beam[i])
                    ndx = i

            if val > neighborScore:
                madeAMove = True
                del beam[ndx]
                beam.append(node)


        #return the best element on the beam
        # what is the lowest value in the beam?
        val = float("inf")
        ndx = 0
        for i in range(len(beam)):
            if self.problem.cost(beam[i]) < val:
                val = self.problem.cost(beam[i])
                ndx = i

        self.timeSpent = time.time() - startTime
        return beam[ndx]






