# -*- coding: utf-8 -*-
"""
Created on Thu Dec  2 20:06:57 2021

@author: Nekokan1500
"""

# Count number of inversions in a list of numbers

def countInv(array):
    if len(array) == 0 or len(array) == 1:
        return (array,0)
    else:
        n = int(len(array)/2)
        (C,leftInv) = countInv(array[0:n])
        (D,rightInv) = countInv(array[n:])
        (B,splitInv) = countSplitInv(C,D)
        return (B,leftInv+rightInv+splitInv)


def countSplitInv(array_left,array_right):
    n = len(array_left) + len(array_right)
    i = 0
    j = 0
    splitInv = 0
    array_sorted = []
    for k in range(n):
        if array_left[i] < array_right[j]:
            array_sorted.append(array_left[i])
            if i == len(array_left)-1:
                array_sorted += array_right[j:]
                return (array_sorted,splitInv)
            else:
                i += 1
        else:
            array_sorted.append(array_right[j])
            splitInv += len(array_left) - i
            if j == len(array_right)-1:
                array_sorted += array_left[i:]
                return (array_sorted,splitInv)
            else:
                j += 1


array = [5,4,6,2,1,3]
print(countInv(array))
                    
