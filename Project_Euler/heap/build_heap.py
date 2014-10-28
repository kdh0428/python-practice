#!/usr/bin/env python

import math
b_sort = [4,1,3,2,16,9,10,14,8,7]


def Parent(N):
    return N/2

def Left_Node(N):
    return 2*N+1

def Right_Node(N):
    return 2*N+2

def Max_Heap(heap_list,i):
    l = Left_Node(i)
    r = Right_Node(i)
    if l < len(heap_list) and heap_list[l] > heap_list[i]:
        largest = l
    else:
        largest = i
    if r < len(heap_list) and heap_list[r] > heap_list[largest]:
        largest = r
    if largest != i:
        heap_list[largest],heap_list[i] = heap_list[i],heap_list[largest]
        Max_Hap(heap_list,largest)


def Build_Heap(heap_list):
    for i in xrange(int(math.ceil(float(len(heap_list)/2))),-1,-1):
        Max_Heap(heap_list,i)
