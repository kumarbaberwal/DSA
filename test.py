def addEdge(adj: list[list[int]], src: int, dest: int) -> None:
    adj[src].append(dest)
    adj[dest].append(src)

def graph(vertices: int, edges: list[list[int]], noOfEdges: int) -> None:
    adj = [[] for _ in range(vertices)]

    for i in range(noOfEdges):
        addEdge(adj, edges[i][0], edges[i][1])

    bfs(adj, vertices)

def bfs(adj: list[list[int]], vertices: int) -> None:
    queue = [0]
    vis = [False]*vertices
    while queue:
        cursor = queue.pop(0)
        if vis[cursor] == False:
            vis[cursor] = True
            print(cursor, end=' ')
            for i in adj[cursor]:
                queue.append(i)

if __name__ == "__main__":
    vertices = 7
    edges = [[0,1],[0,2],[1,3],[2,4],[3,4],[3,5],[4,5],[5,6]]
    noOfEdges = len(edges)
    graph(vertices, edges, noOfEdges)