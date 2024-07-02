# edges=[[0,1],[0,4],[1,0],[1,2],[2,1],[2,3],[3,2],[4,0],[4,5],[5,4]] #f0r NO Cycle
edges=[[0,1],[0,4],[1,0],[1,2],[1,4],[2,1],[2,3],[3,2],[4,0],[4,1],[4,5],[5,4]]
noOfEdges=len(edges)
vertices=6

def addEdge(adj:list[list[int]], src:int, dest:int) -> None:
    adj[src].append(dest)
    print(adj)

def dfs(adj:list[list[int]], current:int, arr:list[bool]):
    print(current, end='  ')
    arr[current]=True
    for i in range(len(adj[current])):
        curr=adj[current][i]
        if arr[curr]==False:
            dfs(adj, curr, arr)

# Cycle Detection for Undirected Graphs

def cycleDetection(adj:list[list[int]], current:int, arr:list[bool], parent:int) -> bool:
    arr[current]=True
    for i in range(len(adj[current])):
        curr=adj[current][i]
        if arr[curr]==True and curr!=parent:
            return True
        elif arr[curr]==False:
            if cycleDetection(adj, curr, arr, current)==True:
                return True            
    return False


def graph(vertices:int, edges:list[list[int]], noOfEdges:int) -> None:
    adj=[[] for i in range(vertices)]

    for i in range(noOfEdges):
        addEdge(adj, edges[i][0], edges[i][1])
    
    arr=[False]*vertices
    for i in range(vertices):
        if arr[i]==False:
            dfs(adj, i, arr)

    arr=[False]*vertices
    print()
    print(cycleDetection(adj, 0, arr, -1))


if __name__=="__main__":
    graph(vertices, edges, noOfEdges)