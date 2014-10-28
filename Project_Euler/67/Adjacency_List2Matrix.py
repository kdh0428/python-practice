def AdjacencyList2AdjacencyMatrix(AdjacencyList):
    AdjacencyMatrix = []
    for index in xrange(0,len(AdjacencyList)):
        AdjacencyMatrix.append([0]*len(AdjacencyList))

    for Nodes in AdjacencyList:
        i = Nodes.value
        while Nodes:
            Nodes = Nodes.next 
            if Nodes is None:
                break
            AdjacencyMatrix[i][Nodes.value] = -(Nodes.pathcost)

    Print_Matrix(AdjacencyMatrix)
    return AdjacencyMatrix


def Print_Matrix(AdjacencyMatrix):
    for line in AdjacencyMatrix:
        print line
