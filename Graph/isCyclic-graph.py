# edges=[[0,2],[1,0],[2,3],[3,0]]
edges=[[0,2],[1,0],[2,3]]
noOfEdges=len(edges)
vertices=4

def addEdge(adj:list[list], src:int, desc:int):
    adj[src].append(desc)
    print(adj)

def dfs(adj:list[list], current:int, arr:list[bool]):
    print(current,end=' ')
    arr[current]=True
    
    for i in range(len(adj[current])):
        curr=adj[current][i]
        if arr[curr]==False:
            dfs(adj, curr, arr)
            
def cyclic(adj: list[list], current:int, arr:list[bool], arr2:list[bool]):
    arr[current]=True
    arr2[current]=True

    for i in range(len(adj[current])):
        curr=adj[current][i]
        if arr2[curr]==True:
            return True
        
        elif arr[curr]==False:
            if cyclic(adj, curr, arr, arr2):
                return True
    arr2[current]=False
    return False
def graph(vertices:int, edges:list[list], noOfEdges:int):
    adj=[[] for i in range(vertices)]

    for i in range(noOfEdges):
        addEdge(adj, edges[i][0], edges[i][1])


    arr=[False]*4
    # print(arr)
    # print(adj)
    for i in range(vertices):
        if arr[i]==False:
            dfs(adj, i, arr)
    print()
    arr=[False]*4
    arr2=[False]*4
    for i in range(vertices):
        if arr[i]==False:
            isCycle=cyclic(adj, i, arr, arr2)
            if isCycle:
                print(isCycle)
                break

graph(vertices, edges, noOfEdges)
