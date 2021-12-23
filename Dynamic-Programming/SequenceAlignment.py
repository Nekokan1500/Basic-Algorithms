# -*- coding: utf-8 -*-
"""
Created on Wed Dec 22 17:00:22 2021

@author: Nekokan1500
"""

import numpy as np

# Implementation of Sequence Alignment using dynamic programming

# Input: strings X = x1,x2,...,xm and Y = y1,y2,...,yn over the alphabet {A,C,G,T},
#        a mismatch penalty a{xy} for each x,y,
#        a gap penalty a{gap} > 0
# Output: the Needleman-Wunsch score of X and Y
# Running time is O(mn)

def NW(X_str,Y_str,p_m,p_gap):
    # preprocess input
    X = list(X_str)
    Y = list(Y_str)
    m,n = len(X),len(Y)
    # initialize mismatch penalties
    P = np.zeros((m,n))
    for i in range(m):
        for j in range(n):
            if X[i] != Y[j]:
                P[i][j] = p_m
    # subproblem solutions (indexed from 0)
    A = np.empty((m+1,n+1))
    A[:] = None
    # base case #1 (j=0)
    for i in range(m+1):
        A[i][0] = i*p_gap
    # base case #2 (i=0)
    for j in range(n+1):
        A[0][j] = j*p_gap
    # systematically sove all subproblems
    for i in range(1,m+1):
        for j in range(1,n+1):
            # case 1: match xi and yj
            score_1 = A[i-1][j-1] + P[i-1][j-1]
            # case 2:
            score_2 = A[i-1][j] + p_gap
            # case 3:
            score_3 = A[i][j-1] + p_gap
            A[i][j] = min(score_1,score_2,score_3)
    return get_sequence(X_str, Y_str, P, p_gap, A)

# Reconstruct the solution from the returned penalty matrix
def get_sequence(X_str,Y_str,P,p_gap,A):
    X = list(X_str)
    Y = list(Y_str)
    (M,N) = A.shape
    S_x = ""
    S_y = ""
    i = M - 1
    j = N - 1
    while i > 0:
        while j > 0:
            # case 1
            if A[i][j] == A[i-1][j-1] + P[i-1][j-1]:
                S_x = X[i-1] + S_x
                S_y = Y[j-1] + S_y
                i -= 1
                j -= 1
            elif A[i][j] == A[i-1][j] + p_gap:  # case 2
                S_y = "-" + S_y
                S_x = X[i-1] + S_x
                i -= 1
            else:
                S_x = "-" + S_x
                S_y = Y[j-1] + S_y
                j -= 1
    return S_x,S_y,A[M-1][N-1]

# Test data
if __name__ == "__main__":
    S_x,S_y,NW_Score = NW("AGTACG","ACATAG",2,1)
    print(S_x) # A-GTACG
    print(S_y) # ACATA-G
    print(int(NW_Score)) # 4
                