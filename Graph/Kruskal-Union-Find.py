# -*- coding: utf-8 -*-
"""
Created on Thu Dec 16 19:59:07 2021

@author: Nekokan1500
"""

from Common import Graph
from Common import UnionFind
                
def Kruskal_UnionFind(graph):
    MST = []
    U = UnionFind(graph.vertices)
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
    for e in E:
        if U.find(e[0]) is not U.find(e[1]):
            MST.append((e[0].value,e[1].value))
            U.union(e[0], e[1])
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
    TE = Kruskal_UnionFind(graph)
    print(TE)
    # output is [('b', 'c'), ('a', 'e'), ('b', 'e'), ('b', 'd')]
    