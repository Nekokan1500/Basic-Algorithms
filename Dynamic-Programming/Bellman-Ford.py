# -*- coding: utf-8 -*-
"""
Created on Sat Dec 25 15:39:09 2021

@author: Nekokan1500
"""

from Common import Graph

import numpy as np

class Node():
    def __init__(self,l,v):
        self.label = l
        self.value = v
        
class BFGraph(Graph):
    def __init__(self):
        self.vertices = []
        self.edges = []
    
    # override the add_edge() method of the parent class - Graph
    def add_edge(self, s, d, cost):
        self.edges.append((s,d,cost))
        
    def add_node_by_value(self,l,v):
        labels = [node.label for node in self.vertices]
        if l not in labels:
            node = Node(l,v)
            self.vertices.append(node)
            
    def get_node(self,l):
        return next(vertex for vertex in self.vertices if vertex.label == l)
                    

# Implementation of the Bellman-Ford algorithm
# Input: - directed graph G = (V,E) in adjacency list representation
#        - a source vertex s in V
#        - a real-valued length le for each e in E
# Output: dist(s,v) for every vertex v in V
#         or a declaration that G contains a negative cycle

def Bellman_Ford(graph,s):
    # subproblems (i index from 0, v indexes V)
    n = len(graph.vertices)
    A = np.empty((n+1,n))
    A[:] = None
    # base cases
    A[0][s.value] = 0
    for v in graph.vertices:
        if v is not s:
            A[0][v.value] = float('inf')
    # systematically solve all subproblems
    for i in range(1,n+1):
        stable = True
        for v in graph.vertices:
            # case 1: shortest path to v has i-1 or fewer edges
            case_1 = A[i-1][v.value]
            # case 2: shortes path to v has i edges
            cases = []
            # get all edges with v as the ending node
            v_edges = [e for e in graph.edges if e[1] == v.label]
            for edge in v_edges:
                # get starting node w of each edge leading to node v
                w = graph.get_node(edge[0])
                cases.append(A[i-1][w.value] + edge[2])
            if len(cases) == 0:
                min_of_cases = 0
            else:
                min_of_cases = min(cases)
            A[i][v.value] = min(case_1,min_of_cases)
            if A[i][v.value] != A[i-1][v.value]:
                stable = False
        if stable == True:
            return A
    return "negative cycle"

# test data
graph = BFGraph()
s_node = Node('s',0)
graph.add_node(s_node)
graph.add_node_by_value('v', 1)
graph.add_node_by_value('u', 2)
graph.add_node_by_value('w', 3)
graph.add_node_by_value('t', 4)
graph.add_edge('s', 'v', 4)
graph.add_edge('s', 'u', 2)
graph.add_edge('u', 'v', -1)
graph.add_edge('u', 'w', 2)
graph.add_edge('w', 't', 2)
graph.add_edge('v', 't', 4)

if __name__ == "__main__":
    R = Bellman_Ford(graph, s_node)
    print(R)


            
    