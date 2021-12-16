# -*- coding: utf-8 -*-
"""
Created on Thu Dec  2 20:06:57 2021

@author: Nekokan1500
"""

class Node:
    def __init__(self,value,key):
        self.key = key
        self.value = value
        self.left = None
        self.right = None
        self.parent = None
        self.winner = None # for Prim algorithm

class Heap:
    def __init__(self):
        self.array = []
        
    def heapify(self,a_list):
        self.array = a_list
        for i in range(len(self.array)-1,-1,-1):
            self.siftdown(i)
            
    def delete(self,value):
        node = next(node for node in self.array if node.value == value)
        index = self.array.index(node)
        n = len(self.array)
        if index == n-1:    # the one to delete happens to be the last one in array
            self.array.pop()
        else:
            self.array[index],self.array[n-1] = self.array[n-1],self.array[index]
            self.array.pop()
            if index == 0:  # the one to delete happens to be the root node
                self.siftdown(0)
            else:
                p_index = -(-index//2) - 1
                if self.array[index].key < self.array[p_index].key:
                    self.siftup(index)
                else:
                    self.siftdown(index)
    
    def siftup(self,i):
        swap = True
        while swap:
            if i > 0:
                p_index = -(-i//2) - 1
                if self.array[p_index].key > self.array[i].key:
                    self.array[p_index],self.array[i] = self.array[i],self.array[p_index]
                    i = p_index
                else:
                    swap = False
            else:
                swap = False
    
    def siftdown(self,i):
        n = len(self.array)
        swap = True
        while swap:
            index_1 = i*2 + 1 # index of left child
            index_2 = i*2 + 2 # index of right child
            key1 = None
            key2 = None
            if index_1 <= n-1: 
                key1 = self.array[index_1].key
                if index_2 <= n-1:
                    key2 = self.array[index_2].key
            if key1 != None and key2 != None:
                if self.array[i].key > key1 and self.array[i].key > key2:
                    if key1 <= key2:
                        self.array[i],self.array[index_1] = self.array[index_1],self.array[i]
                        i = index_1
                    else:
                        self.array[i],self.array[index_2] = self.array[index_2],self.array[i]
                        i = index_2
                elif self.array[i].key > key1 and self.array[i].key <= key2:
                        self.array[i],self.array[index_1] = self.array[index_1],self.array[i]
                        i = index_1
                elif self.array[i].key > key2 and self.array[i].key <= key1:
                        self.array[i],self.array[index_2] = self.array[index_2],self.array[i]
                        i = index_2
                else:
                    swap = False
            elif key1 != None and key2 == None:
                if self.array[i].key > key1:
                    self.array[i],self.array[index_1] = self.array[index_1],self.array[i]
                    i = index_1
                else:
                    swap = False
            else: # no more child
                swap = False
        
    def insert(self,item):
        self.array.append(item)
        self.siftup(len(self.array)-1)    
                
    def get_min(self):
        if len(self.array) > 0:
            return self.array[0].key
        else:
            return 0
                
    def extractMin(self):
        n = len(self.array)
        if n == 0:
            return None
        if n == 1:
            return self.array.pop()
        else:
            self.array[0],self.array[n-1] = self.array[n-1],self.array[0]
            m = self.array.pop()
            self.siftdown(0)
            return m
    
    def print_heap(self):
        for item in self.array:
            print("Node: " + str(item.value) + "; Key: " + str(item.key))
            
    def get_count(self):
        return len(self.array)
            

# Heap that supports ExtractMax
class Heap1:
    def __init__(self):
        self.array = []
        
    def insert(self,item):
        self.array.append(item)
        swap = True
        while swap:
            index = self.array.index(item)
            if index > 0:
                p_index = -(-index//2) - 1
                if self.array[p_index].key < item.key:
                    self.array[p_index],self.array[index] = self.array[index],self.array[p_index]
                else:
                    swap = False
            else:
                swap = False
                
    def get_max(self):
        if len(self.array) > 0:
            return self.array[0].key
        else:
            return 0
                
    def extractMax(self):
        n = len(self.array)
        if n == 0:
            return None
        if n == 1:
            return self.array.pop()
        else:
            self.array[0],self.array[n-1] = self.array[n-1],self.array[0]
            m = self.array.pop()
            n = len(self.array)
            last_node = self.array[0]
            swap = True
            while swap:
                index = self.array.index(last_node)
                index_1 = index*2 + 1 # index of left child
                index_2 = index*2 + 2 # index of right child
                key1 = None
                key2 = None
                if index_1 <= n-1: 
                    key1 = self.array[index_1].key
                    if index_2 <= n-1:
                        key2 = self.array[index_2].key
                if key1 != None and key2 != None:
                    if last_node.key < key1 and last_node.key < key2:
                        if key1 >= key2:
                            self.array[index],self.array[index_1] = self.array[index_1],self.array[index]
                        else:
                            self.array[index],self.array[index_2] = self.array[index_2],self.array[index]
                    elif last_node.key < key1 and last_node.key >= key2:
                        self.array[index],self.array[index_1] = self.array[index_1],self.array[index]
                    elif last_node.key < key2 and last_node.key >= key1:
                        self.array[index],self.array[index_2] = self.array[index_2],self.array[index]
                    else:
                        swap = False
                elif key1 != None and key2 == None:
                    if last_node.key < key1:
                        self.array[index],self.array[index_1] = self.array[index_1],self.array[index]
                    else:
                        swap = False
                else: # no more child
                    swap = False
            return m
    
    def print_heap(self):
        for item in self.array:
            print("Node: " + str(item.value) + "; Key: " + str(item.key))
            
    def get_count(self):
        return len(self.array)


if __name__ == "__main__":
    heap = Heap()
    heap.insert(Node('a',13))
    heap.insert(Node('b',4))
    heap.insert(Node('c',11))
    heap.insert(Node('d',4))
    heap.insert(Node('e',9))
    heap.insert(Node('f',8))
    heap.insert(Node('g',12))
    heap.insert(Node('h',9))
    heap.insert(Node('i',4))
    heap.insert(Node('j',3))
    heap.print_heap()
    #print(heap.extractMin().key)
    #heap.print_heap()
    #print(heap.extractMin().key)
    #heap.print_heap()
    #print(heap.extractMin().key)
    #heap.print_heap()
    #print(heap.extractMin().key)
    #heap.print_heap()
    #print(heap.extractMin().key)
    #heap.print_heap()