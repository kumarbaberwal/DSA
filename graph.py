# row,column=3,3
# graph=[[0]*column]*row

# print(graph)
# graph[0][0]=1
# print(graph)

# Graphs using adjacency list 

def addedge(graph1, src, dest):
    graph1[src].append(dest)
    print(graph1)

v=4

def graph(v, edges, noOfEdges):
    graph1=[0]*v

    for i in range(len(graph1)):
        graph1[i]=[]

    for i in range(noOfEdges):
        addedge(graph1,edges[i][0],edges[i][1])

    adjList(graph1,v)

def adjList(graph1,v):
    for i in range(v):
        print(i,' -> ',end='')
        for x in graph1[i]:
            print(x, " ",end='')

        print()

edges=[[0,2],[1,2],[1,3],[2,0],[2,1],[2,3],[3,1],[3,2]]

noOfEdges=len(edges)
print(noOfEdges)
graph(v,edges,noOfEdges)
