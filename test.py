def addEdge(adj: list[list[int]], src: int, dest: int, weight: int) -> None:

    """Parameters:
    adj (list[list[int]]): The adjacency list of the graph.
    src (int): The source vertex.
    dest (int): The destination vertex.
    weight(int): The Weight from source to destination
    """

    adj[src].append([dest, weight])

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
        addEdge(adj, edge[0], edge[1], edge[2])

    return adj

def bellmanford(adj: list[list[list[int, int]]], source: int, vertices: int) -> list[int]:
    """
    Implements the Bellman-Ford algorithm to find the shortest paths from a source vertex.

    Parameters:
    adj (list[list[list[int]]]): The adjacency list of the graph.
    source (int): The source vertex.
    vertices (int): The number of vertices in the graph.

    Returns:
    list[int]: The shortest distances from the source vertex to each other vertex.
    """
    distances = [float('inf')] * vertices
    distances[source] = 0
    for i in range(vertices - 1):
        for src in range(vertices):
            for neighbour, weight in adj[src]:
                if distances[src] != float('inf') and distances[neighbour] > distances[src] + weight:
                    distances[neighbour] = distances[src] + weight
    for src in range(vertices):
        for neighbour, weight in adj[src]:
                if distances[src] != float('inf') and distances[neighbour] > distances[src] + weight:
                    print('Negative Cycle Detection')
                    return []
    return distances

if __name__ == "__main__":
    vertices = 5
    edges = [[0, 1, 2], [0, 2, 4], [1, 2, -4], [2, 3, 2], [3, 4, 4], [4, 1, -1]]
    adjacency_list = createGraph(vertices, edges)
    distances = bellmanford(adjacency_list, 0, vertices)
    if distances:
        print(f'Shortest Distance from Vertex 0 is {distances}')

   
    
