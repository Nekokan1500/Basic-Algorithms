# -*- coding: utf-8 -*-
"""
Created on Sat Nov 13 14:54:02 2021

@author: Nekokan1500
"""

import numpy as np

# Naive approach in O(n^2) time:
# The main idea here is to always move to the smallest adjacent neighbor cell 
# with a value smaller than the current cell value until we reach a local minimum.

M = np.array([[30,100,20,19,18],
              [29,101,21,104,17],
              [28,102,16,105,22],
              [27,103,23,106,15],
              [26,25,24,107,14]])

def GetNextCell1(cell):
    x, y = cell[0], cell[1]
    value = M[x][y]
    next_cell = cell
    # compare with cell above
    if x > 0 and value > M[x-1][y]:
        value = M[x-1][y]
        next_cell = (x-1,y)
    # compare with left cell
    if y > 0 and value > M[x][y-1]:
        value = M[x][y-1]
        next_cell = (x,y-1)
    # compare with cell below
    if x < len(M) - 1 and value > M[x+1][y]:
        value = M[x+1][y]
        next_cell = (x+1,y)
    # compare with right cell
    if y < len(M) - 1 and value > M[x][y+1]:
        value = M[x][y+1]
        next_cell = (x,y+1)
    return next_cell

def GetLocalMinimum1(current_cell):
    next_cell = GetNextCell1(current_cell)
    if next_cell == current_cell:
        return current_cell
    else:
        return GetLocalMinimum1(next_cell)


# Divide-and-Conquer approach in O(n) time
# We’ll divide the given matrix into four quadrant sub-matrices. 
# We can guarantee that our local minimum will be inside one of these four 
# sub-matrices. To find in which sub-matrix our local minimum exists, we’ll 
# iterate over the middle row and the middle column to get the cell that has 
# the smallest value among all of the values in the middle row and the middle column.

# After we get the cell with the smallest value, we’ll get the next cell 
# (smallest adjacent cell) of it. Now the sub-matrix that has the next cell will 
# also have the local minimum in it.

def GetMinInMiddleRow(matrix,x):
    minimum = min(matrix[x])
    for i in range(len(matrix[x])):
        if matrix[x][i] == minimum:
            return ((x,i),minimum)
        
def GetMinInMiddleCol(matrix,y):
    minimum = min(matrix[:,y])
    for i in range(len(matrix[:,y])):
        if matrix[i][y] == minimum:
            return ((i,y),minimum)

def GetNextCell2(matrix,cell):
    x, y = cell[0], cell[1]
    value = matrix[x][y]
    next_cell = cell
    # compare with cell above
    if x > 0 and value > matrix[x-1][y]:
        value = matrix[x-1][y]
        next_cell = (x-1,y)
    # compare with left cell
    if y > 0 and value > matrix[x][y-1]:
        value = matrix[x][y-1]
        next_cell = (x,y-1)
    # compare with cell below
    if x < len(matrix) - 1 and value > matrix[x+1][y]:
        value = matrix[x+1][y]
        next_cell = (x+1,y)
    # compare with right cell
    if y < len(matrix) - 1 and value > matrix[x][y+1]:
        value = matrix[x][y+1]
        next_cell = (x,y+1)
    return next_cell

def GetLocalMinimum2(matrix):
    x, y = matrix.shape
    middle_row = x//2
    middle_col = y//2
    (min_middle_row_cell,min_middle_row) = GetMinInMiddleRow(matrix,middle_row)
    (min_middle_col_cell,min_middle_col) = GetMinInMiddleCol(matrix,middle_col)
    min_cell = ()
    if min_middle_row < min_middle_col:
        min_cell = min_middle_row_cell
    else:
        min_cell = min_middle_col_cell   
    next_cell = GetNextCell2(matrix,min_cell)
    if next_cell == min_cell:
        return matrix[min_cell]
    else:
        if next_cell[0] < middle_row:
            if next_cell[1] < middle_col:
                # search the upper-left quadrant
                return GetLocalMinimum2(matrix[:middle_row,:middle_col])
            else:
                # search the upper-right quadrant
                return GetLocalMinimum2(matrix[:middle_row,middle_col:])
        else:
            if next_cell[1] < middle_col:
                # search the lower-left quadrant
                return GetLocalMinimum2(matrix[middle_row:,:middle_col])
            else:
                # search the lower-right quadrant
                return GetLocalMinimum2(matrix[middle_row:,middle_col:])
    

print(GetLocalMinimum2(M))

    