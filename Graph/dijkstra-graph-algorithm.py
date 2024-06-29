def addEdge(adj: list[list[list[int, int]]], src: int, dest: int, weight: int) -> None:

    # Parameters:
    # adj (list[list[int]]): The adjacency list of the graph.
    # src (int): The source vertex.
    # dest (int): The destination vertex.
    # weight(int): The Weight from the source vertex to the destination vertex.

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

def dijkstra(adj: list[list[list[int, int]]], src: int, vertices: int) -> list[int]:
    """
    Implements Dijkstra's algorithm to find the shortest path from the source vertex to all other vertices.

    Parameters:
    adj (list[list[list[int, int]]]): The adjacency list of the graph, where each entry is a list of lists [neighbour, weight].
    src (int): The source vertex.
    vertices (int): The number of vertices in the graph.

    Returns:
    list[int]: The list of shortest distances from the source vertex to each other vertex.
    """
    distance = [float('inf')] * vertices
    distance[src] = 0
    import heapq
    queue = [(0, src)]
    while queue:
        current_weight, current_vertex = heapq.heappop(queue)
        for neighbour, weight in adj[current_vertex]:
            if distance[current_vertex] + weight < distance[neighbour]:
                distance[neighbour] = current_weight + weight
                heapq.heappush(queue, (distance[neighbour], neighbour))
    return distance

if __name__ == "__main__":
    vertices = 6
    edges = [[0, 1, 2], [0, 2, 4],
             [1, 0, 2], [1, 2, 1], [1, 3, 7],
             [2, 0, 4], [2, 1, 1], [2, 4, 3],
             [3, 1, 7], [3, 4, 2], [3, 5, 1], 
             [4, 2, 3], [4, 3, 2], [4, 5, 5],
             [5, 3, 1], [5, 4, 5]]
    adjacency_list = createGraph(vertices, edges)
    print(f'The Shortest path from O is {dijkstra(adjacency_list, 0, vertices)}')
