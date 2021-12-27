# -*- coding: utf-8 -*-
"""
Created on Sun Dec 26 17:47:09 2021

@author: Nekokan1500
"""

import numpy as np

from Bellman_Ford import BFGraph

class FWGraph(BFGraph):
    def __init__(self):
        self.vertices = []
        self.edges = {}
    
    # override the add_edge() method of the parent class - Graph
    def add_edge(self, s, d, cost):
        self.edges[(s,d)] = cost
        

# Implementation of the Floyd-Warshall algorithm
# Input: directed graph G = (V,E) in adjacency-list or adjacency-matrix
#        representation
#        a real-valued length for each edge in E
# Output: dist(v,w) for every vertex pair (v,w) in V, or a declaration that 
#         G contains a negative cycle

def Floyd_Warshall(graph):
    n = len(graph.vertices)
    # subproblems (k indexed from 0, v,w from 1)
    # k is the number of vertices allowed in a subproblem
    A = np.empty((n+1,n,n))
    A[:] = None
    # base cases (k = 0)
    for v in graph.vertices:
        for w in graph.vertices:
            if v is w:
                A[0][v.value-1][w.value-1] = 0
            # (v,w) is an edge of G
            elif (v.label,w.label) in graph.edges:
                A[0][v.value-1][w.value-1] = graph.edges[(v.label,w.label)]
            else:
                A[0][v.value-1][w.value-1] = float('inf')
    # systematically sove all subproblems
    for k in range(1,n+1):
        for v in graph.vertices:
            for w in graph.vertices:
                case_1 = A[k-1][v.value-1][w.value-1]
                case_2 = A[k-1][v.value-1][k-1] + A[k-1][k-1][w.value-1]
                A[k][v.value-1][w.value-1] = min(case_1,case_2)
    # check for a negative cycle
    for v in graph.vertices:
        if A[n][v.value-1][v.value-1] < 0:
            return "negative cycle"
    return A

# Test data
graph = FWGraph()
graph.add_node_by_value('s', 1)
graph.add_node_by_value('u', 2)
graph.add_node_by_value('v', 3)
graph.add_node_by_value('w', 4)
graph.add_node_by_value('t', 5)
graph.add_edge('s', 'u', 2)
graph.add_edge('s', 'w', -10)
graph.add_edge('u', 'v', -4)
graph.add_edge('w', 't', -10)
graph.add_edge('v', 't', 5)

if __name__ == "__main__":
    R = Floyd_Warshall(graph)
    print(R)