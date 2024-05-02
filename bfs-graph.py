edges=[[0,1],[0,2],[1,0],[1,3],[2,0],[2,4],[3,1],[3,4],[3,5],[4,2],[4,3],[4,5],[5,3],[5,4],[5,6],[6,5]]
noOfEdges=len(edges)
vertices=7

def addEdge(adj,src,dest):
    adj[src].append(dest)
    # print(adj)

def graph(vertices,edges,noOfEdges):
    adj=[[] for i in range(vertices)]

    for i in range(noOfEdges):
        addEdge(adj,edges[i][0],edges[i][1])
    
    bfs(adj)


def bfs(adj):
    import queue
    qu=queue.Queue()
    arr=[False]*7
    qu.put(0)

    while not qu.empty():
        cursor=qu.get()
        if arr[cursor]==False:
            print(cursor,end=' ')
            arr[cursor]=True
            for i in range(len(adj[cursor])):
                qu.put(adj[cursor][i])           

graph(vertices,edges,noOfEdges)
