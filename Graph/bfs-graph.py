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

def bfs(adj: list[list[int]], src: int, vertices: int) -> None:
    visited = [False] * vertices
    queue = [src]
    while queue:
        current_node = queue.pop(0)
        if not visited[current_node]:
            visited[current_node] = True
            print(current_node, end='  ')
            for neighbour in adj[current_node]:
                queue.append(neighbour)

if __name__ == "__main__":
    vertices = 7
    edges = [[0, 1], [0, 2],
             [1, 0], [1, 3],
             [2, 0], [2, 4],
             [3, 1], [3, 4], [3, 5],
             [4, 2], [4, 3], [4, 5],
             [5, 3], [5, 4], [5, 6],
             [6, 5]]
    adjacency_list = createGraph(vertices, edges)
    bfs(adjacency_list, 0, vertices)
