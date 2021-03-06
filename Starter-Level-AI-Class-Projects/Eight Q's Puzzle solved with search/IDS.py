"""
Depth First Search (DFS)

implements a Depth First Search as defined by the Russel-Norvig text

"""

from collections import deque
from Node import *
import time

class IDS():
    """
    Creates a new Graph Search object

    model: a Problem model of the environment
    """
    def __init__(self, problem):
        # save the params
        self.problem = problem
        self.nodesSearched = 0
        self.timeSpent = 0
        self.depthSearched = 0

    """
    Searches for a path from the start state to a goal state using the Problem given
    to the constructor
    """

    def search(self):
        self.startTime = time.time()

        for depth in range(55555):
            print('depth', depth)
            result = self.IDS(self.problem.initial, depth)
            if result != None:
                self.timeSpent = time.time() - self.startTime
                return result



    """
    Conducts Depth First Graph Search from a given start state.
    state: the start state for the search
    """
    def IDS(self, startState ,depth):
        ''' TODO -- The following algorithm is a traditional graph-search
             TODO -- NEED TO update how nodes are removed from frontier
         '''

        startTime = time.time()

        # create a node for the state
        root = Node(startState)
        # create the frontier and expanded sets
        frontier = deque([root])


        while len(frontier) > 0:
            node = frontier.pop()
            self.nodesSearched += 1
            if self.problem.goal_test(node.state):
                self.timeSpent = time.time() - startTime
                return node



            # expand node in frontier
            for action in self.problem.actions(node.state):

                nextState = self.problem.result(node.state, action)
                child = Node(state=nextState, parent=node,
                             path_cost=self.problem.path_cost(node.path_cost, node.state, action, nextState),
                             action=action)

                if child.depth <= depth and child not in frontier:
                    frontier.append(child)

        return None
