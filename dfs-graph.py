edges=[[0,1],[0,2],[1,0],[1,3],[2,0],[2,4],[3,1],[3,4],[3,5],[4,2],[4,3],[4,5],[5,3],[5,4],[5,6],[6,5]]
noOfEdges=len(edges)
vertices=7

def addEdge(adj, src, desc):
    adj[src].append(desc)
    # print(adj)

def dfs(adj, current, arr):
    print(current,end=' ')
    arr[current]=True
    
    for i in range(len(adj[current])):
        curr=adj[current][i]
        if arr[curr]==False:
            dfs(adj, curr, arr)
            
def printAllPaths(adj:list[list], current:int, arr:list[bool], pathstring:str, target:int):
    print(pathstring)
    if current==target:
        print(pathstring)
        return
    for i in range(len(adj[current])):
        curr=adj[current][i]
        if arr[curr]==False:
            arr[curr]=True
            printAllPaths(adj, curr, arr, pathstring=pathstring+str(curr), target=target)
            arr[curr]=False

def graph(vertices, edges, noOfEdges):
    adj=[[] for i in range(vertices)]

    for i in range(noOfEdges):
        addEdge(adj, edges[i][0], edges[i][1])


    arr=[False]*7
    # print(arr)
    # print(adj)
    for i in range(vertices):
        if arr[i]==False:
            dfs(adj, i, arr)
    print()
    printAllPaths(adj, 0, arr, "0", 5)

graph(vertices, edges, noOfEdges)
