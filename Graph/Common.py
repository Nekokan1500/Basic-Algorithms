# -*- coding: utf-8 -*-
"""
Created on Fri Dec 17 20:17:25 2021

@author: Nekokan1500
"""

class Node:
    def __init__(self,value):
        self.value = value
        
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
            
    def print_vertices(self):
        for v in self.vertices:
            print("Vertex " + str(v.value) + " cluster: " + str(v.cluster))
            
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