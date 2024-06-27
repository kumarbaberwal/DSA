def addEdge(adj: list[list[int]], src: int, dest: int, weight: int) -> None:

    # Parameters:
    # adj (list[list[int]]): The adjacency list of the graph.
    # src (int): The source vertex.
    # dest (int): The destination vertex.
    # weight (int): The Edge weight from source to destination vertex.

    adj[src].append([dest,weight])

def createGraph(vertices: int, edges: list[list[int]]) -> list[list[int]]:
    adj = [[] for _ in range(vertices)]

    for edge in edges:
        addEdge(adj, edge[0], edge[1], edge[2])

    return adj

def printGraph(adj: list[list[int]], vertices: int) -> None:
    for src in range(vertices):
        print('Node', src, 'Makes an edge with')
        for dest, weight in adj[src]:
            print('\tNode', dest, 'with edge weight', weight)
        print()

if __name__ == "__main__":
    vertices = 4
    edges = [[0, 2, 2], [1, 2, 10], [1, 3, 0], [2, 0, 2], [2, 1, 10], [2, 3, -1], [3, 1, 0], [3, 2, -1]]
    adjancency_list = createGraph(vertices, edges)
    printGraph(adjancency_list, vertices)