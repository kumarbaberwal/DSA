def addEdge(adj: list[list[int]], src: int, dest: int) -> None:
    adj[src].append(dest)
    adj[dest].append(src)

def graph(vertices: int, edges: list[list[int]], noOfEdges: int) -> None:
    adj = [[] for _ in range(vertices)]

    for i in range(noOfEdges):
        addEdge(adj, edges[i][0], edges[i][1])

    vis = [False]*vertices

    for i in range(vertices):
        if vis[i] == False:
            dfs(adj, i, vis)

def dfs(adj: list[list[int]], curr: int, vis: list[bool]) -> None:
    print(curr, end=' ')
    vis[curr] = True
    
    for i in adj[curr]:
        if vis[i] == False:
            dfs(adj, i, vis)

if __name__ == "__main__":
    vertices = 7
    edges = [[0,1],[0,2],[1,3],[2,4],[3,4],[3,5],[4,5],[5,6]]
    noOfEdges = len(edges)
    graph(vertices, edges, noOfEdges)