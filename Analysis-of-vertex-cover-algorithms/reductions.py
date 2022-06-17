"""All graphs in this assignment are undirected and represented with an
adjacency matrix. If a graph has N vertices, then the vertices are identified
by the numbers: 0, 1, 2, ..., N-1.

Consider the following undirected graph:

          +---+     +---+  
          | 0 |-----| 1 |
          +---+     +---+
            |
            |
          +---+
          | 2 |
          +---+  

This graph is represented by the following adjacency matrix:

G = [[0, 1, 1],
     [1, 0, 0],
     [1, 0, 0]]

Note that G[0][1] and G[1][0] are both 1s since there is an edge between
vertices 0 and 1. However, G[1][2] and G[2][1] are both 0s because there is
no edge between vertices 1 and 2."""

from itertools import combinations

def maximum_clique(G, k):
    """Checks if the graph G contains a clique of size >= k

    Parameters:
        G, a undirected graph (adjacency matrix)
        k, a non-negative integer    
    Returns:
        True   if G has a clique of size >= k
        False  otherwise"""
    # For each subset of vertices with size k...
    for C in combinations(range(len(G)), k):
        # If every pair of vertices, (u,v), has an edge...
        if all(G[u][v] == 1 for u, v in combinations(C, 2)):
            return True
    # If we get here, no k-subset is a clique
    return False


################################################################################
# Part 1
################################################################################

def independent_set(g, k):
    """Checks if the graph G contains an independent set of size >= k
    
    Parameters:
        G, a undirected graph (adjacency matrix)
        k, a non-negative integer
        
    Returns:
        True   if G has an independent set of size >= k
        False  otherwise"""
    for kVerts in combinations(range(len(g)), k):
        tmp = [[0] * len(g[i]) for i in range(len(g))]
        for u, v in combinations(kVerts, 2):
            if g[u][v]:
                tmp[u][v] = 1
                tmp[v][u] = 1
        if not maximum_clique(tmp, 2):
            return True
    return False

################################################################################
# Part 2
################################################################################

def vertex_cover(G, k):
    """Checks if the graph G contains a vertex cover of size <= k
    
    Parameters:
        G, a undirected graph (adjacency matrix)
        k, a non-negative integer
        
    Returns:
        True   if G has a vertex cover of size <= k
        False  otherwise"""
    return independent_set(G, max(0, len(G) - k))


