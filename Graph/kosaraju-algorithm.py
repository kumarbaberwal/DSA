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

def topSort(adj: list[list[int]], current_vertex: int, visited: list[bool], stack: list[int]) -> None:
    """
    Performs a topological sort on the graph and stores the vertices in a stack.

    Parameters:
    adj (List[List[int]]): The adjacency list of the graph.
    current_vertex (int): The current vertex being explored.
    visited (List[bool]): A list indicating whether each vertex has been visited.
    stack (List[int]): A stack to store the topologically sorted vertices.
    """
    visited[current_vertex] = True
    for neighbour in adj[current_vertex]:
        if not visited[neighbour]:
            topSort(adj, neighbour, visited, stack)
    stack.append(current_vertex)

def kosaraju(adj: list[list[int]], vertices: int) -> None:
    """
    Implements Kosaraju's algorithm to find and print strongly connected components (SCCs) of the graph.

    Parameters:
    adj (List[List[int]]): The adjacency list of the graph.
    vertices (int): The number of vertices in the graph.
    """
    # Step 1: Perform topological sort and store vertices in a stack
    stack = []
    visited = [False] * vertices
    for vertex in range(vertices):
        if not visited[vertex]:
            topSort(adj, vertex, visited, stack)
    
    # Step 2: Create a transposed graph
    transAdj = [[] for _ in range(vertices)]
    for source in range(vertices):
        for dest in adj[source]:
            transAdj[dest].append(source)

    # Step 3: Perform DFS on the transposed graph using the order in the stack
    visited = [False] * vertices
    while stack:
        current_vertex = stack.pop()
        if not visited[current_vertex]:
            dfs(transAdj, current_vertex, visited)
            print()

if __name__ == "__main__":
    vertices = 5
    edges = [[0, 2], [0, 3], [1, 0], [2, 1], [3, 4]]
    adjacency_list = createGraph(vertices, edges)
    kosaraju(adjacency_list, vertices) 