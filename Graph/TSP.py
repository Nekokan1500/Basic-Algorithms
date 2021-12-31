# -*- coding: utf-8 -*-
"""
Created on Thu Dec 30 10:47:11 2021

@author: Nekokan1500
"""

from Common import Graph

class TSPGraph(Graph):
    def add_edge(self,s,d,cost):
        self.edges[(s,d)] = cost
        self.edges[(d,s)] = cost
        
# utility function that get all possible paths starting from vertex S and 
# and eventually back to it
def permutation(vertices):
    n= len(vertices)
    if n == 0 or n == 1:
        return [vertices]
    else:
        P = []
        for i in range(n):
            v = vertices[i]
            rest = vertices[:i] + vertices[i+1:]
            for p in permutation(rest):
                P.append([v] + p)
        return P
                
# Implementation of TSP using exhaustive search
# Input: a complete undirected graph G = (V,E). Each edge in E has a real-valued cost
# Output: a tour with the minimum possible sum of edge costs
def TSP(graph):
    # tour with minimum possible sum of edge costs
    min_tour = ()
    min_cost = float('inf')
    # take the first vertice as starting point
    s = graph.vertices[0]
    others = graph.vertices[1:]
    paths = permutation(others)
    for path in paths:
        total_length = graph.edges[(s.value,path[0].value)]
        for i in range(len(path)-1):
            total_length += graph.edges[(path[i].value,path[i+1].value)]
        total_length += graph.edges[(path[-1].value,s.value)]
        if total_length < min_cost:
            min_cost= total_length
            min_tour = ([s.value]+[v.value for v in path]+[s.value],min_cost)
    return min_tour

# test data
graph = TSPGraph()
graph.add_nodes_by_value(['a','b','c','d'])
graph.add_edge('a', 'b', 1)
graph.add_edge('a', 'c', 4)
graph.add_edge('a', 'd', 3)
graph.add_edge('b', 'c', 5)
graph.add_edge('b', 'd', 2)
graph.add_edge('c', 'd', 6)


if __name__ == "__main__":
    P = TSP(graph)
    print(P) # (['a', 'b', 'd', 'c', 'a'], 13)
