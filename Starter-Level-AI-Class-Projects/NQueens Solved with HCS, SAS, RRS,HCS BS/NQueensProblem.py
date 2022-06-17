import random

class NQueensProblem:
    """The problem of placing N queens on an NxN board with none attacking
      each other.  A state is represented as an N-element tuple, where
      a value of r in the c-th entry means there is a queen at column c,
      row r
      """

    def __init__(self, initial):
        self.N = len(initial)
        self.initial = initial

    def actions(self, state):
        """ state: a tuple that is the state of a NQueens configuration
            returns a list of successors or neighbors of possible configurations from the input state """

        possible_actions = []
        for col in range(self.N):
            for val in range(self.N):
                if state[col] != val:
                    new_state = list(state)
                    new_state[col] = val
                    possible_actions.append(tuple(new_state))
        return possible_actions

    def cost(self, state):
        """Return number of conflicting queens for a given node"""
        num_conflicts = 0

        for col in range(self.N-1):
            for nstep in range(col+1,self.N):
                diff = nstep - col
                if state[nstep] == state[col]:
                    num_conflicts +=1
                elif state[nstep] + diff == state[col]:
                    num_conflicts +=1
                elif state[nstep] - diff == state[col]:
                    num_conflicts +=1

        return num_conflicts

    def shuffle(self, state):
        # return a random state
        s = list(state)
        for col in range(self.N):
            s[col] = random.randint(0,self.N-1)
        return tuple(s)
