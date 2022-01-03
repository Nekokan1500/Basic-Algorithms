# -*- coding: utf-8 -*-
"""
Created on Tue Nov 16 21:07:22 2021

@author: Nekokan1500
"""

import random

# input: array of n distinct integers
#        left and right endpoints l and r, with l <= r
def Partition(array,l,r):
    # select the pivot element
    p = array[l]
    i = l + 1
    for j in range(l+1,r):
        if array[j] < p:
            array[i],array[j] = array[j],array[i]
            i += 1
    array[l],array[i-1] = array[i-1],array[l]
    return (i-1)

def ChoosePivot(array,l,r):
    return random.choice(range(l,r))
    
def QuickSort(array,l,r):    
    if l >= r:
        return
    i = ChoosePivot(array,l,r)
    # move the pivot element to the first position
    array[l],array[i] = array[i],array[l]
    j = Partition(array,l,r)
    QuickSort(array,l,j)
    QuickSort(array,j+1,r)
    
        