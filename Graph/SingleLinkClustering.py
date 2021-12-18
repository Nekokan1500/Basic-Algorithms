# -*- coding: utf-8 -*-
"""
Created on Fri Dec 17 19:58:44 2021

@author: Nekokan1500
"""

import numpy as np
from collections import deque
from Common import Graph
from Common import UnionFind

class Point:
    def __init__(self,x,y):
        self.value = (x,y)
        self.cluster = None
        self.explored = False
        
def calc_distance(p1,p2):
    return np.sqrt(np.power((p1.value[0]-p2.value[0]),2) + np.power((p1.value[1]-p2.value[1]),2))

# Find connected components of the input graph
def find_cc(graph):
    numCC = 0
    for node in graph.vertices:
        if node.explored == False:
            node.explored = True
            numCC += 1
            # call BFS starting at i
            Q = deque()
            Q.append(node)
            while len(Q) > 0:
                v = Q.popleft()
                v.cluster = numCC
                if v.value in graph.edges:
                    adj_list = graph.edges[v.value]
                    for w in adj_list:
                        w_node = graph.get_node(w[0])
                        if w_node.explored == False:
                            w_node.explored = True
                            Q.append(w_node)
    return numCC

# Single-Link Clustering via Kruskal's algorithm
# Input: graph: a complete undirected graph G = (X,E). X is the collection of data points
#        k: number of desired clusters
# Output: k clusters
def SLC(graph,k):
    T = Graph()
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
    counter = 0
    for e in E:
        if counter <= len(graph.vertices) - k:
            if U.find(e[0]) is not U.find(e[1]):
                T.add_node(e[0])
                T.add_node(e[1])
                T.add_edge(e[0].value, e[1].value, e[2])
                T.add_edge(e[1].value, e[0].value, e[2])
                U.union(e[0], e[1])
            counter += 1
    find_cc(T)
    return T

# test data
graph = Graph()
data_file = open('SLC_Test_Data.txt','r')
for line in data_file.readlines():
    values = line.split(',')
    p = Point(int(values[0]),int(values[1]))
    graph.add_node(p)
for i in range(len(graph.vertices)):
    for j in range(len(graph.vertices)):
        p1 = graph.vertices[i]
        p2 = graph.vertices[j]
        if p1 is not p2:
            d = calc_distance(p1, p2)
            graph.add_edge(p1.value, p2.value, d)

T = SLC(graph,2)
T.print_vertices()
        
        

