# -*- coding: utf-8 -*-
"""
Created on Wed Nov 10 09:08:19 2021

@author: Nekokan1500
"""

# Inputs: p1 and p2 are (x,y) tuples
def getDistance(p1,p2):
    return (p1[0]-p2[0])**2 + (p1[1]-p2[1])**2

def ClosestSplitPair(Px,Py,d):
    x_median = Px[int(len(Px)/2)][0]
    Sy = [p for p in Py if x_median - d < p[0] < x_median + d]
    bestPair = []
    best = d
    l = len(Sy)
    for i in range(l-1):
        for j in range(1,min(7,l-i)):
            d2 = getDistance(Sy[i], Sy[i+j])
            if d2 < best:
                best = d2
                bestPair = [Sy[i],Sy[i+j]]
    return bestPair

# Inputs: Px and Py are lists of (x,y) tuples 
def ClosestPair(Px,Py):
    if len(Px) == 2:
        return Px
    elif len(Px) == 3:
        d1 = getDistance(Px[0],Px[1])
        d2 = getDistance(Px[1],Px[2])
        d3 = getDistance(Px[0],Px[2])
        min_d = min(d1,d2,d3)
        if d1 == min_d:
            return [Px[0],Px[1]]
        elif d2 == min_d:
            return [Px[1],Px[2]]
        elif d3 == min_d:
            return [Px[0],Px[2]]
    else:
        Ly = []
        Ry = []
        k = len(Px)//2
        Lx = Px[:k]
        Rx = Px[k:]
        for i in range(len(Py)):
            if Py[i] in Lx:
                Ly.append(Py[i])
            else:
                Ry.append(Py[i])
        [l1,l2] = ClosestPair(Lx,Ly)
        [r1,r2] = ClosestPair(Rx,Ry)
        d1 = getDistance(l1, l2)
        d2 = getDistance(r1, r2)
        d = min(d1,d2)
        bestSplitPair = ClosestSplitPair(Px,Py,d)
        if len(bestSplitPair) > 0:
                return [bestSplitPair[0],bestSplitPair[1]]
        else:
            if d1 == d:
                return [l1,l2]
            else:
                return [r1,r2]


Px = [(1,1),(2,3),(3,2),(4,4)]
Py = [(1,1),(3,2),(2,3),(4,4)]
print(ClosestPair(Px, Py))