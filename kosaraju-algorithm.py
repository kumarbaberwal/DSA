def addEdge(adj: list[list[int]], src: int, dest: int) -> None:
    adj[src].append(dest)
    print(adj)

def graph(vertices: int, edges: list[list[int]], noOfEdges: int) -> None:
    adj = [[] for _ in range(vertices)]
    for i in range(noOfEdges):
        addEdge(adj, edges[i][0], edges[i][1])

    kosaraju(adj, vertices)

def dfs(adj:list[list[int]], curr:int, vis:list[bool]) -> None:
    vis[curr]=True
    print(curr, end=' ')
    for i in adj[curr]:
        if not vis[i]:
            dfs(adj, i, vis)

def topSort(adj: list[list[int]], curr:int, vis:list[bool], stack:list) -> None:
    vis[curr]=True
    for i in adj[curr]:
        if not vis[i]:
            topSort(adj, i, vis, stack)

    stack.append(curr)

def kosaraju(adj: list[list[int]], vertices: int) -> None:
    #step=1
    stack=[]
    vis=[False]*vertices
    for i in range(vertices):
        if not vis[i]:
            topSort(adj, i, vis, stack)
    
    # step=2
    transAdj=[[] for _ in range(len(adj))]
    for i in range(len(adj)):
        for j in adj[i]:
            transAdj[j].append(i)

    print(transAdj)

    # step=3
    vis=[False]*vertices
    while stack:
        curr=stack.pop()
        if not vis[curr]:
            dfs(transAdj, curr, vis)
            print()

if __name__ == "__main__":
    vertices = 5
    edges = [[0, 2], [0, 3], [1, 0], [2, 1], [3, 4]]
    noOfEdges = len(edges)
    graph(vertices, edges, noOfEdges)
