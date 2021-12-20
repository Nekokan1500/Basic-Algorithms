# -*- coding: utf-8 -*-
"""
Created on Sun Dec 19 20:57:46 2021

@author: Nekokan1500
"""

from Common import Graph
from Common import Node

class WISNode(Node):
    def __init__(self, value, weight):
        self.value = value
        self.weight = weight

# Weighted Independent Set problem
# Input: a PATH graph G with vertex set {v1,v2,...,vn} and a nonnegative weight
#        wi for each vertext vi
# Output: the total weight of a maximum weight independent set of G

# global array for storing sub-problem solutions
A = []

def wis(vertices):
    global A
    if len(vertices) == 0:
        return A[0]
    elif len(vertices) == 1:
        return A[1]
    else:
        for i in range(2,len(vertices)+1):
            # case 1: vn is not in Solution
            mwis_1 = A[i-1]
            # case 2: vn is in Solution
            mwis_2 = A[i-2] + vertices[i-1].weight
            A[i] = max(mwis_1,mwis_2)
    return A[len(vertices)]

# Test data
graph = Graph()
graph.add_node(WISNode('a',3))
graph.add_node(WISNode('b',2))
graph.add_node(WISNode('c',1))
graph.add_node(WISNode('d',6))
graph.add_node(WISNode('e',4))
graph.add_node(WISNode('f',5))

if __name__ == "__main__":
    A = [None]*(len(graph.vertices)+1)
    A[0] = 0
    A[1] = graph.vertices[0].weight
    TW = wis(graph.vertices)
    print(TW)
        