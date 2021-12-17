# -*- coding: utf-8 -*-
"""
Created on Thu Dec 16 19:59:07 2021

@author: Nekokan1500
"""

class Node:
    def __init__(self,value):
        self.value = value
        self.parent = None    # parent's index
        self.size = None

class Graph:
    def __init__(self):
        self.vertices = []
        self.edges = {}
    
    def add_node(self,v):
        if v not in self.vertices:
            self.vertices.append(v)
            
    def add_node_by_value(self,v):
        values = [node.value for node in self.vertices]
        if v not in values:
            node = Node(v)
            self.vertices.append(node)
            
    def add_nodes(self,nodes):
        for node in nodes:
            self.add_node(node)
    
    def add_nodes_by_value(self,nodes):
        for node in nodes:
            self.add_node_by_value(node)
            
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

class UnionFind:
    def __init__(self,nodes):
        self.array = nodes
        self.__initialize()
        
    def __initialize(self):
        for i in range(len(self.array)):
            self.array[i].parent = i
            self.array[i].size = 1
        
    def find(self,x):
        if x not in self.array:
            return None
        else:
            x_index = self.array.index(x)
            while True:
                if self.array[x_index].parent == x_index:
                    return x_index
                else:
                    x_index = self.array[x_index].parent
                    
    def union(self,x,y):
        i = self.find(x)    # index of x's parent
        j = self.find(y)    # index of y's parent
        if i == j:
            return
        else:
            if self.array[i].size >= self.array[j].size:
                self.array[j].parent = i
                self.array[i].size += self.array[j].size
            else:
                self.array[i].parent = j
                self.array[j].size += self.array[i].size
                
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
    