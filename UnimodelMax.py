# -*- coding: utf-8 -*-
"""
Created on Fri Nov 12 10:00:05 2021

@author: Nekokan1500
"""

# input: integer array with length >= 2
# solution 1
def unimodalmax(array):
    if len(array) == 2 or len(array) == 3:
        return array[1]
    k = len(array)//2
    array_left = array[:k]
    array_right = array[k:]
    modal_left = unimodalmax(array_left)
    modal_right = unimodalmax(array_right)
    m = max(modal_left, modal_right)
    return max(m,array_right[0])


# solution 2
def unimodalmax2(array):
    if len(array) == 2 or len(array) == 3:
        return array[1]
    k = len(array)//2
    if array[k] > array[k-1] and array[k] > array[k+1]:
        return array[k]
    else:
        if array[k] < array[k-1]:
            return unimodalmax2(array[:k])
        else:
            return unimodalmax2(array[k:])
    
print(unimodalmax2([1,4,3,2,1]))