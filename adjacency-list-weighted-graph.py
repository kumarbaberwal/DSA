edges=[[0,2,2],[1,2,10],[1,3,0],[2,3,-1]]
noOfEdges=len(edges)

def addEdge(adj, src, dest, weight):
    adj[src].append([dest,weight])
    adj[dest].append([src,weight])
    return adj

def printGraph(adj , v):

    for i in range(v):
        print('Node',i , 'makes an edge with')

        for j in adj[i]:
            print('\tNode', j[0], 'with edge weight = ', j[1])
        print()

v=4
adj=[[] for i in range(v)]

print(adj)

def graph(v, edges, noOfEdges):

    for i in range(noOfEdges):
        addEdge(adj,edges[i][0],edges[i][1],edges[i][2])
    

graph(v, edges, noOfEdges)
printGraph(adj,v)