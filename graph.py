# row,column=3,3
# graph=[[0]*column]*row

# print(graph)
# graph[0][0]=1
# print(graph)

# Graphs using adjacency list 

def addedge(graph, src, dest):
    graph[src].append(dest)

v=4

def graph(v, edges, noOfEdges):
    graph=[0]*v

    for i in range(len(graph)):
        graph[i]=[]

    for i in range(noOfEdges):
        addedge(graph,edges[i][0],edges[i][1])

    adjList(graph,v)

def adjList(graph,v):
    for i in range(v):
        print(i,' -> ',end='')
        for x in graph[i]:
            print(x, " ",end='')

        print()

edges=[[0,2],[1,2],[1,3],[2,0],[2,1],[2,3],[3,1],[3,2]]

noOfEdges=8

graph(v,edges,noOfEdges)