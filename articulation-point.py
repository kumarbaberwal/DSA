# Finding Articulation Points in a Graph Using Tarjans Algorithm

def addEdge(adj: list[list[int]], src: int, dest: int) -> None:
    adj[src].append(dest)
    adj[dest].append(src)
    print(adj)

def graph(vertices: int, edges: list[list[int]], noOfEdges: int) -> None:
    adj=[[] for _ in range(vertices)]

    for i in range(noOfEdges):
        addEdge(adj, edges[i][0], edges[i][1])


if __name__ == "__main__":
    vertices = 5
    edges = [[0,1],[0,2],[0,3],[1,2],[3,4]]
    noOfEdges = len(edges)
    graph(vertices, edges, noOfEdges)