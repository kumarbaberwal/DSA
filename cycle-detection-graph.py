edges=[[0,1],[0,2],[1,0],[1,3],[2,0],[2,4],[3,1],[3,4],[3,5],[4,2],[4,3],[4,5],[5,3],[5,4],[5,6],[6,5]]
noOfEdges=len(edges)
vertices=7

def addEdge(adj:list[list[int]], src:int, dest:int) -> None:
    adj[src].append(dest)
    # print(adj)

def dfs(adj:list[list[int]], current:int, arr:list[bool]):
    print(current, end='  ')
    arr[current]=True
    for i in range(len(adj[current])):
        curr=adj[current][i]
        if arr[curr]==False:
            dfs(adj, curr, arr)

def graph(vertices:int, edges:list[list[int]], noOfEdges:int) -> None:
    adj=[[] for i in range(vertices)]

    for i in range(noOfEdges):
        addEdge(adj, edges[i][0], edges[i][1])
    
    arr=[False]*vertices
    for i in range(vertices):
        if arr[i]==False:
            dfs(adj, i, arr)



if __name__=="__main__":
    graph(vertices, edges, noOfEdges)