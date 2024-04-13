edges = [[0,1],[0,2],[1,0],[1,3],[2,0],[2,4],[3,1],[3,4],[3,5],[4,2],[4,3],[4,5],[5,3],[5,4],[5,6],[6,5]]
noOfEdges = len(edges)
vertices = 7

def addEdge(adj, src, desc):
    adj[src].append(desc)

def dfs(adj, current, arr):
    arr[current] = True
    for neighbor in adj[current]:
        if not arr[neighbor]:
            dfs(adj, neighbor, arr)

def printAllPaths(adj, current, arr, pathstring, target):
    if current == target:
        print(pathstring)
        return
    arr[current] = True
    for neighbor in adj[current]:
        if not arr[neighbor]:
            printAllPaths(adj, neighbor, arr, pathstring + str(neighbor), target)
    arr[current] = False

def graph(vertices, edges, noOfEdges):
    adj = [[] for _ in range(vertices)]

    for edge in edges:
        addEdge(adj, edge[0], edge[1])

    arr = [False] * vertices

    for i in range(vertices):
        if not arr[i]:
            dfs(adj, i, arr)
    print()
    arr = [False] * vertices  # Reset arr for path finding
    printAllPaths(adj, 0, arr, '0', 5)

graph(vertices, edges, noOfEdges)