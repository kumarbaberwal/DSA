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

def dfs(adj: list[list[int]], current_vertex: int, visited: list[bool], dt: list[int], lt: list[int], time: int, parent_vertex: int) -> None:
    """
    Depth-first search to find and print all bridges in the graph.

    Parameters:
    adj (List[List[int]]): The adjacency list of the graph.
    current_vertex (int): The current vertex being explored.
    visited (List[bool]): A list indicating whether each vertex has been visited.
    dt (List[int]): Discovery times of visited vertices.
    lt (List[int]): Lowest discovery times reachable from the vertex.
    time (List[int]): Current time counter.
    parent_vertex (int): The parent vertex of the current vertex in the DFS tree.
    """
    visited[current_vertex] = True
    dt[current_vertex] = lt[current_vertex] = time[0]
    time[0] += 1
    for neighbour in adj[current_vertex]:
        if neighbour == parent_vertex:
            continue
        elif not visited[neighbour]:
            dfs(adj, neighbour, visited, dt, lt, time, current_vertex)
            lt[current_vertex] = min(lt[current_vertex], lt[neighbour])
            if dt[current_vertex] < lt[neighbour]:
                print("Bridge is : ", current_vertex, "---->", neighbour)
        else:
            lt[current_vertex] = min(lt[current_vertex], dt[neighbour])

def getBridge(adj: list[list[int]], vertices: int) -> None:
    """
    Finds and prints all bridges in the graph.

    Parameters:
    adj (List[List[int]]): The adjacency list of the graph.
    vertices (int): The number of vertices in the graph.
    """
    dt = [-1] * vertices  # Discovery times of visited vertices
    lt = [-1] * vertices  # Lowest discovery times reachable from the vertex
    time = [0]  # Current time counter
    visited = [False] * vertices
    
    for source in range(vertices):
        if not visited[source]:
            dfs(adj, source, visited, dt, lt, time, -1)

if __name__ == "__main__":
    vertices = 6
    edges = [[0, 1], [0, 2], [0, 3], [1, 0], [1, 2], [2, 0], [3, 0], [3, 4], [3, 5], [4, 3], [4, 5], [5, 3], [5, 4]]
    adjacency_list = createGraph(vertices, edges)
    getBridge(adjacency_list, vertices) 