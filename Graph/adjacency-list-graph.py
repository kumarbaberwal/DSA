def addEdge(adj: list[list[int]], src: int, dest: int) -> None:

    # Parameters:
    # adj (list[list[int]]): The adjacency list of the graph.
    # src (int): The source vertex.
    # dest (int): The destination vertex.

    adj[src].append(dest)

def createGraph(vertices: int, edges: list[list[int]]) -> list[list[int]]:
    adj = [[] for _ in range(vertices)]

    for edge in edges:
        addEdge(adj, edge[0], edge[1])

    return adj

def printGraph(adj: list[list[int]], vertices: int) -> None:
    for i in range(vertices):
        print(i, '-->', end='  ')
        for j in adj[i]:
            print(j, end='  ')
        print()

if __name__ == "__main__":
    vertices = 4
    edges = [[0, 2], [1, 2], [1, 3], [2, 0], [2, 1], [2, 3], [3, 1], [3, 2]]
    adjancency_list = createGraph(vertices, edges)
    printGraph(adjancency_list, vertices)