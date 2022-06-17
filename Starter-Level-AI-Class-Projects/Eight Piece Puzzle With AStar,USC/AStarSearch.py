"""
A Star Search
name: Johnny Hill
description: This program uses uniform cost search and turn it into a* search using a heuristic state
proposed points: (8 of 8)

"""
from queue import PriorityQueue
from Node import *
import time


class AStarSearch():

    def __init__(self, problem):
        # save the params
        self.problem = problem
        self.nodesSearched = 0
        self.timeSpent = 0


    """
    Searches for a path from the start state to a goal state using the Problem given
    to the constructor
    """
    def search(self):
        return self.astar(self.problem.initial)

    """
    Conducts A Star Search from a given start state.
    state: the start state for the search
    """
    def astar(self, startState):
        startTime = time.time()
        root = Node(startState, path_cost = 0)
        frontier = PriorityQueue()
        root.f = self.problem.h(root.state)
        frontier.put((root.f, root))
        frontierStates = {}
        frontierStates[root.state] = root


        explored = set()
        while not frontier.empty():
            element = frontier.get()
            node = element[1]

            self.nodesSearched += 1

            if self.problem.goal_test(node.state):
                self.timeSpent = time.time() - startTime
                return node

            explored.add(node.state)

            #expand node in frontier
            for action in self.problem.actions(node.state):
                nextState = self.problem.result(node.state, action)

                if nextState not in explored:
                    child = Node(state=nextState, parent=node,
                                  path_cost=self.problem.path_cost(node.path_cost, node.state, action, nextState),
                                  action=action)
                    child.f = child.path_cost+self.problem.h(child.state)


                    if child.state not in frontierStates or frontierStates[child.state].f > child.f:
                        frontier.put((child.f, child))
                        frontierStates[child.state] = child


        return None







