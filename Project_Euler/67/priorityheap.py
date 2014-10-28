import math
def Parent(N):
    return int(math.floor((N-1)/2))

def Left_Node(N):
    return 2*N+1

def Right_Node(N):
    return 2*N+2


def Heap_Increase(heap,v,i):
    if heap[i].priority < v.priority:
        pass
    else:
        
        while i > 0 and abs(heap[Parent(i)].priority) < abs(heap[i].priority):
            heap[Parent(i)],heap[i] = heap[i],heap[Parent(i)]
            i = Parent(i)

def Priority_Heap(heap,Graph_list,v):
    for i in xrange(0,len(heap)):
            Heap_Increase(heap,v,i)

def Heap_Scan(heap,Graph_list,v):
    check = 0
    for i in xrange(0,len(heap)):
        if heap[i].value == v.value:
            check = 1
            if heap[i].priority > v.priority:
                
                heap[i].priority = v.priority
                Graph_list[v.value].priority = v.priority
                break
    if check == 0:
        heap.append(Graph_list[v.value])
