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

def isCyclicDirectedGraph(adj: list[list[int]], current_vertex: int, visited: list[bool], stack: list[bool]) -> bool:
    """
    Checks if there is a cycle in the directed graph using DFS.

    Parameters:
    adj (list[list[int]]): The adjacency list of the graph.
    current_vertex (int): The current vertex being explored.
    visited (list[bool]): A list indicating whether each vertex has been visited.
    stack (list[bool]): A list indicating the recursion stack for each vertex.

    Returns:
    bool: True if a cycle is detected, False otherwise.
    """
    visited[current_vertex] = True
    stack[current_vertex] = True
    for neighbour in adj[current_vertex]:
        if stack[neighbour]:
            return True
        elif not visited[neighbour]:
            if isCyclicDirectedGraph(adj, neighbour, visited, stack):
                return True
    stack[current_vertex] = False
    return False

if __name__ == "__main__":
    vertices = 4
    edges = [[0, 2], [1, 0], [2, 3], [3, 0]]
    # edges = [[0, 1], [0, 2], [1, 3], [2, 3]]
    adjacency_list = createGraph(vertices, edges)
    visited = [False] * vertices
    stack = [False] * vertices

    """
    To Reach all the Vertices of the Graph
    """

    for i in range(vertices):
        if not visited[i]:
            print("The graph is Cyclic" if isCyclicDirectedGraph(adjacency_list, 0, visited, stack) else "The Graph is not Cyclic")
            break
