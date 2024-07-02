def addEdge(adj: list[list[int]], src: int, dest: int) -> None:

    """Parameters:
    adj (list[list[int]]): The adjacency list of the graph.
    src (int): The source vertex.
    dest (int): The destination vertex."""

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

def isCyclicUnDirectedGraph(adj: list[list[int]], current_vertex: int, visited: list[bool], parent_vertex: int) -> bool:
    """
    Checks if there is a cycle in the directed graph using DFS.

    Parameters:
    adj (list[list[int]]): The adjacency list of the graph.
    current_vertex (int): The current vertex being explored.
    visited (list[bool]): A list indicating whether each vertex has been visited.
    parent_vertex (int): The parent vertex of the current vertex.

    Returns:
    bool: True if a cycle is detected, False otherwise.
    """
    visited[current_vertex] = True
    for neighbour in adj[current_vertex]:
        if not visited[neighbour]:
            if isCyclicUnDirectedGraph(adj, neighbour, visited, current_vertex):
                return True
        elif neighbour != parent_vertex:
            return True
    return False

if __name__ == "__main__":
    vertices = 6
    # edges = [[0, 1], [0, 4], [1, 0], [1, 2], [1, 4], [2, 1], [2, 3], [3, 2], [4, 0], [4, 1], [4, 5], [5, 4]]
    edges = [[0, 1], [0, 4], [1, 0], [1, 2], [2, 1], [2, 3], [3, 2], [4, 0], [4, 5], [5, 4]]
    adjacency_list = createGraph(vertices, edges)
    visited = [False] * vertices

    # Check for cycles starting from each vertex
    for i in range(vertices):
        if not visited[i]:
            print("The graph is Cyclic" if isCyclicUnDirectedGraph(adjacency_list, 0, visited, -1) else "The Graph is not Cyclic")
            break