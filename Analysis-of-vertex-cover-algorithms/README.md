# Analysis-of-vertex-cover-algorithms

Suppose your boss asks you to find a fast solution to the maximum_clique problem. Ultimately, she wants you to write a function that matches the following specification:


## Prologue 
The graph G is represented as an adjacency list, so it looks something like the following:

After hours of writing code, the best solution you’ve been able to find is a brute force one that iterates over all possible groups of vertices and checks if they are a clique:

from itertools import combinations

Since the number of combinations is exponential, your boss isn’t very happy with your algorithm. She wants you to show that the maximum_clique problem is 
NP
-complete before you give up on a polynomial time solution.

## Part 1: Reducing from Independent SetPermalink
You recall that the independent_set problem is related to the maximum_clique problem, so you set out to show that maximum_clique is at least as hard as independent_set. To do so, you need to reduce independent_set to maximum_clique; in other words, you need to solve independent_set using maximum_clique.

For this part of the assignment, you need to finish implementing the following function:

## Part 2: Reducing from Vertex CoverPermalink
After you show your reduction from independent_set to maximum_clique, your boss is still unconvinced because she is unsure that independent_set is a hard problem. However, she knows for certain that the vertex_cover problem is 
NP
-complete because she knows of the following reductions:

Thus, she also wants you to demonstrate that independent_set is a hard problem by doing a reduction from vertex_cover.

For this part of the assignment, you need to finish implementing the following function:

