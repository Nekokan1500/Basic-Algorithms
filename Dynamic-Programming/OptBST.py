# -*- coding: utf-8 -*-
"""
Created on Thu Dec 23 20:08:07 2021

@author: Nekokan1500
"""

import numpy as np

class Node():
    def __init__(self,v):
        self.value = v
        self.parent = None
        self.left = None
        self.right = None

# Implementation of Optimal Binary Search Tree (BST) using dynamic programming
# Input: keys {1,2,...,n} with nonnegative frequencies (weights) of p1,p2,...,pn
# Output: the minimum weighted search time of a BST with the keys {1,2,...,n}

# p is the input weights array
def OptBST(p):
    n = len(p)
    if n == 1:
        return Node(1)
    # subproblems
    A = np.empty((n+2,n+1))
    A[:] = None
    # base cases: i = j + 1
    for i in range(1,n+2):
        A[i][i-1] = 0
    # systematically solve all subproblems (i <= j)
    for s in range(n):
        for i in range(1,n-s+1):
            # calculate the cost at root node
            root_cost = 0
            for k in range(i,i+s+1):
                root_cost += p[k-1]
            # calculate min cost of r ways of building the BST
            r_cases = []
            for r in range(i,i+s+1):
                r_cases.append(A[i][r-1] + A[r+1][i+s])
            # populate the value of A[i][i+s]
            A[i][i+s] = root_cost + min(r_cases)
    return get_optBST(A)

# reconstruct the tree from matrix A
def get_optBST(A):
    (x,y) = A.shape
    i = 1
    s = y - 2
    # initialize the nodes
    nodes = []
    for n in range(1,y):
        nodes.append(Node(n))
    # Start from A[1][1+s]
    root_cost = 0
    for k in range(i,i+s+1):
        root_cost += A[k][k]
    for r in range(i,i+s+1):
        case = round(A[i][r-1] + A[r+1][i+s],2)
        min_value = round(A[i][i+s] - root_cost,2)
        if case == min_value:
            # r is the root node in this iteration
            # Add nodes to the left subtree
            li = r - 1
            while li > 0:
                nodes[li].left = nodes[li-1]
                nodes[li-1].parent = nodes[li]
                li -= 1
            ri = r - 1
            while ri < i+s-1:
                nodes[ri].right = nodes[ri+1]
                nodes[ri+1].parent = nodes[ri]
                ri += 1
    return nodes

# Test
if __name__ == "__main__":
    nodes = OptBST([0.4,0.3,0.2,0.1])
