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

def dfs(adj: list[list[int]], current_vertex: int, visited: list[bool], dt: list[int], lt: list[int], time: list[int], parent_vertex: int, articulationPoint: list[bool]) -> None:
    """
    Depth-first search to find and print all articulation points in the graph.

    Parameters:
    adj (List[List[int]]): The adjacency list of the graph.
    current_vertex (int): The current vertex being explored.
    parent_vertex (int): The parent vertex of the current vertex in the DFS tree.
    dt (List[int]): Discovery times of visited vertices.
    lt (List[int]): Lowest discovery times reachable from the vertex.
    visited (List[bool]): A list indicating whether each vertex has been visited.
    time (List[int]): Current time counter.
    articulationPoint (List[bool]): A list indicating whether each vertex is an articulation point.
    """
    visited[current_vertex] = True
    dt[current_vertex] = lt[current_vertex] = time[0]
    time[0] += 1
    children = 0

    for neighbour in adj[current_vertex]:
        if neighbour == parent_vertex:
            continue
        if not visited[neighbour]:
            dfs(adj, neighbour, visited, dt, lt, time, current_vertex, articulationPoint)
            lt[current_vertex] = min(lt[current_vertex], lt[neighbour])

            if parent_vertex != -1 and dt[current_vertex] <= lt[neighbour]:
                articulationPoint[current_vertex] = True

            children += 1
        else:
            lt[current_vertex] = min(lt[current_vertex], dt[neighbour])

    if parent_vertex == -1 and children > 1:
        articulationPoint[current_vertex] = True

def getArticulationPoint(adj: list[list[int]], vertices: int) -> None:
    """
    Finds and prints all articulation points in the graph.

    Parameters:
    adj (List[List[int]]): The adjacency list of the graph.
    vertices (int): The number of vertices in the graph.
    """
    dt = [-1] * vertices
    lt = [-1] * vertices
    time = [0]
    visited = [False] * vertices
    articulationPoint = [False] * vertices

    for source in range(vertices):
        if not visited[source]:
            dfs(adj, source, visited, dt, lt, time, -1, articulationPoint)

    for vertex in range(vertices):
        if articulationPoint[vertex]:
            print('Articulation Point:', vertex)

if __name__ == "__main__":
    vertices = 5
    edges = [[0, 1], [0, 2], [0, 3], [1, 0], [1, 2], [2, 0], [2, 1], [3, 0], [3, 4], [4, 3]]
    adjacency_list = createGraph(vertices, edges)
    getArticulationPoint(adjacency_list, vertices)