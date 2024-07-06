def addEdge(adj: list[list[list[int, int]]], src: int, dest: int, weight: int) -> None:

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

def floydWarshall(adj: list[list[list[int, int]]], vertices: int) -> list[list[int]]:
    """
    Implements the Floyd-Warshall algorithm to find the shortest paths between all pairs of vertices.

    Parameters:
    adj (List[List[List[int]]]): The adjacency list of the graph.
    vertices (int): The number of vertices in the graph.

    Returns:
    List[List[int]]: A 2D list representing the shortest distances between every pair of vertices.
    """
    distance = [[float('inf') for _ in range(vertices)] for _ in range(vertices)]
    
    # Set initial distances based on direct edges
    for i in range(vertices):
        for j, weight in adj[i]:
            distance[i][j] = weight
    
    # Set distance to self as 0
    for i in range(vertices):
        distance[i][i] = 0

    # Update distances using Floyd-Warshall algorithm
    for k in range(vertices):
        for i in range(vertices):
            for j in range(vertices):
                distance[i][j] = min(distance[i][j], distance[i][k] + distance[k][j])

    return distance

if __name__ == "__main__":
    vertices = 4
    edges = [[0,1,8],[0,3,1],
             [1,2,1],
             [2,0,4],
             [3,1,2],[3,2,9]]
    adjacency_list = createGraph(vertices, edges)
    distances = floydWarshall(adjacency_list, vertices)
    
    print('The shortest distances between every pair of vertices:')
    for row in distances:
        print(row)
    
