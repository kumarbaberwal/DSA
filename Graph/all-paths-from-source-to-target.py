def addEdge(adj: list[list[int]], src: int, dest: int) -> None:
    
    # Parameters:
    # adj (list[list[int]]): The adjacency list of the graph.
    # src (int): The source vertex.
    # dest (int): The destination vertex.

    adj[src].append(dest)

def createGraph(edges: list[list[int]], vertices: int) -> list[list[int]]:
    
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

def allPaths(adj: list[list[int]], current_vertex: int, target: int, visited: list[bool], path: str) -> None:
    """
    Finds and prints all paths from current_vertex to target in the graph.

    Parameters:
    adj (list[list[int]]): The adjacency list of the graph.
    current_vertex (int): The current vertex in the path.
    target (int): The target vertex.
    visited (list[bool]): A list indicating whether each vertex has been visited.
    path : The current path being explored.
    """
    visited[current_vertex] = True
    if current_vertex == target:
        print(path)
    
    for neighbour in adj[current_vertex]:
        if not visited[neighbour]:
            allPaths(adj, neighbour, target, visited, path + ' ' + str(neighbour))
    visited[current_vertex] = False

if __name__ == "__main__":
    vertices = 7
    edges = [[0, 1], [0, 2],
             [1, 0], [1, 3],
             [2, 0], [2, 4],
             [3, 1], [3, 4], [3, 5],
             [4, 2], [4, 3], [4, 5],
             [5, 3], [5, 4], [5, 6],
             [6, 5]]
    adjacency_list = createGraph(edges, vertices)
    visited = [False] * vertices
    allPaths(adjacency_list, 0, 5, visited, '0')