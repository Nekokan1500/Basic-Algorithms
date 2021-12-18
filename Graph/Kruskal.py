# -*- coding: utf-8 -*-
"""
Created on Thu Dec 16 14:28:45 2021

@author: Nekokan1500
"""
from collections import deque
from Common import Graph

class Node:
    def __init__(self,value):
        self.value = value
        self.explored = False

# Breadth-first search: check if there is a path from vertice s to d in graph
def BFS(graph,s,d):
    for node in graph.vertices:
        node.explored = False
    s.explored = True
    Q = deque()
    Q.append(s)
    while len(Q) > 0:
        v = Q.popleft()
        if v.value in graph.edges:
            adj_list = graph.edges[v.value]
            for edge in adj_list:
                w = graph.get_node(edge[0])
                if w == d:
                    return True
                else:
                    if w.explored == False:
                        w.explored = True
                        Q.append(w)
    return False

# Kruskal algorithm: straight-forward implementation running in O(mn) time
# Input: connected undirected graph G = (V,E) in adjacency-list representation
#        and a cost c(e) for each e in E
# Output: the edges of a MST of G
def Kruskal(graph):
    # Preprocessing
    T = Graph() # the MST built by adding edges
    MST = [] # edges of the MST
    # Sort edges of E by cost
    E = []
    for s,edges in graph.edges.items():
        for edge in edges:
            d = edge[0]
            s_node = graph.get_node(s)
            d_node = graph.get_node(d)
            cost = edge[1]
            if (s_node,d_node,cost) not in E and (d_node,s_node,cost) not in E:
                E.append((s_node,d_node,cost))
    E = sorted(E,key=lambda x:x[2])
    # Main loop
    for edge in E:
        if BFS(T,edge[0],edge[1]) is False:
            # the new edge does not create a cycle in T
            T.add_nodes([edge[0],edge[1]])
            T.add_edge(edge[0].value, edge[1].value, edge[2])
            T.add_edge(edge[1].value, edge[0].value, edge[2])
            MST.append((edge[0].value,edge[1].value))
    return MST

# Test data
graph = Graph()
graph.add_nodes_by_value(['a','b','c','d','e'])
graph.add_edge('a', 'b', 4)
graph.add_edge('b', 'a', 4)
graph.add_edge('b', 'c', 1)
graph.add_edge('c', 'b', 1)
graph.add_edge('a', 'e', 2)
graph.add_edge('e', 'a', 2)
graph.add_edge('b', 'e', 3)
graph.add_edge('e', 'b', 3)
graph.add_edge('b', 'd', 5)
graph.add_edge('d', 'b', 5)
graph.add_edge('e', 'd', 6)
graph.add_edge('d', 'e', 6)
graph.add_edge('c', 'd', 7)
graph.add_edge('d', 'c', 7)

if __name__ == "__main__":
    TE = Kruskal(graph)
    print(TE)
    # output is [('b', 'c'), ('a', 'e'), ('b', 'e'), ('b', 'd')]