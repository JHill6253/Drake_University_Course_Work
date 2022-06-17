# CS 143 Artificial Intelligence Assignment #7
# author: (Johnny Hill)
# proposed points: X (8 of 8)  -- not changing this line automatically results a 1 point deduction


from NQueensProblem import *
from HillClimbingSearch import *
from RandomRestartSearch import *
from SimulatedAnnealingSearch import *
from BeamSearch import *

# create the problem model
nqueens = NQueensProblem((3,2,1,4,3,2,1,2,3,4,5,6,7,8,9,1))

print("==============")
print("HILL CLIMBING ")
# search using a Hill Climbing Search
myHCSearch = HillClimbingSearch(nqueens)
state = myHCSearch.search()

print("Number of rounds:", myHCSearch.rounds)
print("solution: ", state)
print("total cost .. ", nqueens.cost(state))
print("Time Spent with Hill Climbing search:", myHCSearch.timeSpent)

print("==============")
print("==============")
print("RANDOM RESTART ")
# search using a Hill Climbing Random Restart Search
myRRSearch = RandomRestartSearch(nqueens, 5)
state = myRRSearch.search()

print("solution: ", state)
print("total cost .. ", nqueens.cost(state))
print("Time Spent with Hill Climbing search:", myRRSearch.timeSpent)

print("==============")
print("==============")
print("SIMULATED ANNEALING")
# search using Simulated Annealing Search
# start temperature = 30; decrement amount = .001
mySASearch = SimulatedAnnealingSearch(nqueens,startTemp=40,decAmount=.001)
state = mySASearch.search()
print("solution: ", state)
print("total cost .. ", nqueens.cost(state))
print("Time Spent with Simulated Annealing search:", mySASearch.timeSpent)

print("==============")
print("==============")
print("BEAM")
# search using Simulated Annealing Search with 3 beams
myBeamSearch = BeamSearch(nqueens,5)
state = myBeamSearch.search()
print("solution: ", state)
print("total cost .. ", nqueens.cost(state))
print("Time Spent with Beam search:", myBeamSearch.timeSpent)