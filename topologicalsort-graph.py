edges=[[0,1],[0,2],[1,0],[1,3],[2,0],[2,4],[3,1],[3,4],[3,5],[4,2],[4,3],[4,5],[5,3],[5,4],[5,6],[6,5]]
noOfEdges=len(edges)
vertices=7

def addEdge(adj:list[list], src:int, desc:int):
    adj[src].append(desc)
    # print(adj)

def dfs(adj:list[list], current:int, arr:list[bool]):
    print(current,end=' ')
    arr[current]=True
    
    for i in range(len(adj[current])):
        curr=adj[current][i]
        if arr[curr]==False:
            dfs(adj, curr, arr)
            
def topsort(adj:list[list], current:int, arr:list[bool], stack:list[int]):
    arr[current]=True
    for i in range(len(adj[current])):
        curr=adj[current][i]
        if arr[curr]==False:
            topsort(adj, curr, arr, stack)
    stack.append(current)

def graph(vertices:int, edges:list[list], noOfEdges:int):
    adj=[[] for i in range(vertices)]

    for i in range(noOfEdges):
        addEdge(adj, edges[i][0], edges[i][1])


    arr=[False]*7
    for i in range(vertices):
        if arr[i]==False:
            dfs(adj, i, arr)
    print()
    arr=[False]*7
    stack=[]
    for i in range(vertices):
        if arr[i]==False:
            topsort(adj, i, arr, stack)

    for i in range(len(stack)):
        print(stack.pop())

graph(vertices, edges, noOfEdges)
