def addEdge(adj: list[list[int]], src: int, dest: int) -> None:

    # Parameters:
    # adj (list[list[int]]): The adjacency list of the graph.
    # src (int): The source vertex.
    # dest (int): The destination vertex.

    adj[src].append(dest)

def createGraph(vertices: int, edges: list[list[int]]) -> list[list[int]]:

    """
    Creates an adjacency list for a graph with the given vertices and edges.

    Parameters:
    vertices (int): The number of vertices in the graph.
    edges (list[list[int]]): The edges of the graph, where each edge is a list [src, dest].

    Returns:
    list[list[int]]: The adjacency list of the graph.
    """

    adj = [[] for _ in range(vertices)]

    for edge in edges:
        addEdge(adj, edge[0], edge[1])

    return adj

def dfs(adj: list[list[int]], src: int, visited: int) -> None:

    """
    Performs a depth-first search (DFS) traversal of the graph starting from the source vertex.

    Parameters:
    adj (list[list[int]]): The adjacency list of the graph.
    src (int): The source vertex.
    visited (list[bool]): A list indicating whether each vertex has been visited.
    """

    print(src, end='  ')
    visited[src] = True
    for neighbour in adj[src]:
        if not visited[neighbour]:
            dfs(adj, neighbour, visited)

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
    visited = [False] * vertices
    dfs(adjacency_list, 0, visited)
