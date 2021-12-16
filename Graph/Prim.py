# -*- coding: utf-8 -*-
"""
Created on Mon Dec 13 18:41:37 2021

@author: Nekokan1500
"""

import Heap as hp

class Graph:
    def __init__(self):
        self.vertices = []
        self.edges = {}
    
    def add_node(self,v):
        values = [node.value for node in self.vertices]
        if v not in values:
            node = hp.Node(v,float('inf'))
            self.vertices.append(node)
        else:
            print("Node already in graph")
            
    def add_nodes(self,nodes):
        for node in nodes:
            self.add_node(node)
            
    def get_node(self,v):
        return next(vertex for vertex in self.vertices if vertex.value == v)
    
    def add_edge(self,s,d,cost):
        values = [node.value for node in self.vertices]
        if s in values and d in values:
            if s not in self.edges:
                self.edges[s] = [(d,cost)]
            else:
                self.edges[s].append((d,cost))
        elif s not in values:
            print(str(s) + " is not a node in the graph.")
        elif d not in values:
            print(str(d) + " is not a node in the graph.")


"""
Input: connected undirected graph G = (V,E) in adjacency list representation 
       and a cost c(e) for each edge e in E
Output: the edges of a minimum spanning tree of G    
"""
# straight-forward implementation running in O(mn)
def prim(graph):

    X = [graph.vertices[0]]
    T = []
    while True:
        available_edges = []
        for v_node in X:
            if v_node.value in graph.edges:
                adj_list = graph.edges[v_node.value]
                for edge in adj_list:
                    w_node = graph.get_node(edge[0])
                    if w_node not in X:
                        available_edges.append((v_node,w_node,edge[1]))
        if len(available_edges) == 0:
            break
        else:
            min_cost_edge = min(available_edges,key=lambda x:x[2])
            X.append(min_cost_edge[1])
            T.append((min_cost_edge[0].value,min_cost_edge[1].value))
    return T

def prim_heap(graph):
    # Initialization
    s = graph.vertices[0]
    X = [s]
    T = []
    H = hp.Heap()
    s_edges = graph.edges[s.value]
    s_neighbors = []
    s_neighbor_costs = []
    for edge in s_edges:
        s_neighbors.append(graph.get_node(edge[0]))
        s_neighbor_costs.append(edge[1])
    for v in graph.vertices:
        if v is not s:
            if v in s_neighbors:
                v.key = s_neighbor_costs[s_neighbors.index(v)]
                v.winner = (s.value,v.value)
            # each node is initialized with key = inf and winner = None
            H.insert(v)
    # Main loop
    while H.get_count() > 0:
        w = H.extractMin()
        X.append(w)
        T.append(w.winner)
        # update heap to maintain variant
        w_edges = graph.edges[w.value]
        for edge in w_edges:
            y = graph.get_node(edge[0])
            if y not in X:
                if y.key > edge[1]:
                    H.delete(y.value)
                    y.key = edge[1]
                    y.winner = (w.value,y.value)
                    H.insert(y)
    return T
        
# Test data
graph = Graph()
graph.add_nodes(['a','b','c','d'])
graph.add_edge('a', 'b', 1)
graph.add_edge('b', 'a', 1)
graph.add_edge('a', 'c', 4)
graph.add_edge('c', 'a', 4)
graph.add_edge('b', 'd', 2)
graph.add_edge('d', 'b', 2)
graph.add_edge('c', 'd', 5)
graph.add_edge('d', 'c', 5)
graph.add_edge('a', 'd', 3)
graph.add_edge('d', 'a', 3)    

if __name__ == "__main__":
    T = prim_heap(graph)
    print(T)
                    
    
