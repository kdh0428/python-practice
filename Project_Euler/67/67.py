#!/usr/bin/env python
# -*- coding: utf-8 -*-


import Adjacency_List2Matrix
import priorityheap


problem = open("./triangle.txt")

#이 클래스는 그래프의 인접 리스트를 표시하기 위한 연결리스트 클래스 입니다
class Graph_Node:
    def __init__(self,value,pathcost=0):
        self.value = value 
        self.pathcost = pathcost
        self.priority = pathcost
        self.next = None
        self.unvisited = True

Graph_list = [] #인접리스트의 시작 노드들을 저장하는 리스트 입니다.

Node_Num = 1
while True :
    
    line = problem.readline()
    if not line:
        break
    pathcosts = map(lambda x: int(x),line.split())
    min_index,max_index = 0,2
    
    if len(pathcosts) < 2:   # 초기 노드에 의한 루프의 불규칙성을 해결하기 위함입니다. pathcosts의 length가 2 미만일 경우 발생
        Node = Graph_Node(0,0)
        Node.next = Graph_Node(1,-pathcosts[0])
        Graph_list.append(Node)

        
    for Nodes in xrange(Node_Num,len(pathcosts)-1+Node_Num):
        Node = Graph_Node(Nodes,0)
        Graph_list.append(Node)
        Count = len(pathcosts)+Node_Num-1
        pre_node = Node
        Node_Num += 1

        for pathcost in pathcosts[min_index:max_index]:
        
            if pathcost == 0:
                break
            Next_Node = Graph_Node(Count,-pathcost)
            Count += 1
            pre_node.next = Next_Node
            pre_node = Next_Node
        min_index += 1
        max_index += 1

"""
for Nodes in Graph_list:
    while Nodes:
        print "Nodes.value:%d Nodes.pathcost:%d " % (Nodes.value,Nodes.pathcost)
        Nodes = Nodes.next 

"""

heap = []
visited = []
heap.append(Graph_list[0])

def Print_heap(heap):
    for Nodes in heap:
        print "Nodes.value:%d   Nodes.priority:%d   Nodes.pathcost:%d" % (Nodes.value,Nodes.priority,Nodes.pathcost)


        


Maximum_sum = 0
while heap:                                       #힙안에 아무것도 없다면 모든 경로탐색이 되었음을 의미
    print "pop 직전 heap",Print_heap(heap[0:1])
    v = heap.pop(0)
   # if Graph_list[v.value].unvisited is False:
   #     pass
   # Graph_list[v.value].unvisited = False
    Graph_list[v.value].pathcost = v.pathcost
    if abs(v.priority) > abs(v.pathcost):
        pathcost = v.priority
    else:
        pathcost = v.pathcost
    if v.next is not None:
        v = v.next
        while v and v.unvisited:
            if v.priority > v.pathcost + pathcost: 
                v.priority  = v.pathcost + pathcost
                if Maximum_sum < abs(v.priority):
                    Maximum_sum = abs(v.priority)
            next_node = v.next
            v.next = Graph_list[v.value].next 
            Graph_list[v.value] = v
            priorityheap.Heap_Scan(heap,Graph_list,v)
            priorityheap.Priority_Heap(heap,Graph_list,v)
   #         Print_heap(heap)
    #        raw_input("***********************************************")
            v = next_node
print Maximum_sum


