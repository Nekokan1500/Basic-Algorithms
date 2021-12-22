# -*- coding: utf-8 -*-
"""
Created on Tue Dec 21 15:04:14 2021

@author: Nekokan1500
"""

import numpy as np

# Dynamic Programming approach to the Knapsack problem

# Input: a list of items with item values v1,...,vn, and item sizes s1,...,sn, 
#        and a knapsack capacity C (all positive integers)
# Output: the maximum total value of a subset S of {1,2,...,n} with
#         sum(si) <= C

class Item():
    def __init__(self,v,s):
        self.value = v
        self.size = s

def Knapsack(items,C):
    # subproblem solutions (index from 0)
    A = np.empty((len(items)+1,C+1))
    A[:] = None
    # base case: i = 0
    A[0] = 0
    # systematically solve all subproblems
    for i in range(1,len(items)+1):
        for c in range(C+1):
            if items[i-1].size > c:
                A[i][c] = A[i-1][c]
            else:
                case_1 = A[i-1][c]
                case_2 = A[i-1][c-items[i-1].size] + items[i-1].value
                A[i][c] = max(case_1,case_2)
    return A

def get_knapsack_solution(items,A):
    # solution list
    S = []
    (N,C) = A.shape
    n = N - 1
    c = C - 1
    for i in range(n,-1,-1):
        if items[i-1].size <= c and A[i-1][c-items[i-1].size] + items[i-1].value >= A[i-1][c]:
            S.append((items[i-1].value,items[i-1].size))
            c = c - items[i-1].size
    return S

# Test data
if __name__ == "__main__":
    items = []
    items.append(Item(3,4))
    items.append(Item(2,3))
    items.append(Item(4,2))
    items.append(Item(4,3))
    A = Knapsack(items,6)
    result = get_knapsack_solution(items, A)
    print(result)
    # output is [(4,3),(4,2)]
