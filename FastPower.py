# -*- coding: utf-8 -*-
"""
Created on Fri Nov 12 09:48:38 2021

@author: Nekokan1500
"""

def FastPower(a,b):
    if b == 1:
        return a
    else:
        c = a*a
        ans = FastPower(c, b//2)
    if b % 2 == 1:
        return a*ans
    else:
        return ans
    
print(FastPower(15, 7))