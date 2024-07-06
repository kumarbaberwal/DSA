def addEdge(adj: list[list[int]], src: int, dest: int) -> None:

    """Parameters:
    adj (list[list[int]]): The adjacency list of the graph.
    src (int): The source vertex.
    dest (int): The destination vertex.
    weight(int): The Weight from source to destination
    """

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

def topologicalSort(adj: list[list], current_vertex: int, visited: list[bool], stack: list[int]):
    """
    Performs a depth-first search (DFS) based topological sort on the graph.

    Parameters:
    adj (List[List[int]]): The adjacency list of the graph.
    current_vertex (int): The current vertex being explored.
    visited (List[bool]): A list indicating whether each vertex has been visited.
    stack (List[int]): A stack to store the topologically sorted vertices.
    """
    visited[current_vertex] = True
    for neighbour in adj[current_vertex]:
        if not visited[neighbour]:
            topologicalSort(adj, neighbour, visited, stack)

    stack.append(current_vertex)

if __name__ == "__main__":
    vertices = 6
    edges = [[2, 3] ,[3 ,1] ,[4 ,0] ,[4 ,1] ,[5 ,0] ,[5, 2]]
    adjacency_list = createGraph(vertices, edges)
    visited = [False] * vertices
    stack = []
    for source in range(vertices):
        if not visited[source]:
            topologicalSort(adjacency_list, source, visited, stack)

    print("Topological Sort of the given graph:")
    while stack:
        print(stack.pop(), end=' ')
