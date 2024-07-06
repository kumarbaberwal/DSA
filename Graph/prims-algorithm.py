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

def prims(adj: list[list[list[int, int]]], vertices :int) -> int:
    """
    Implements Prim's algorithm to find the cost of the Minimum Spanning Tree (MST).

    Parameters:
    adj (List[List[Tuple[int, int]]]): The adjacency list of the graph.
    vertices (int): The number of vertices in the graph.

    Returns:
    int: The total cost of the MST.
    """
    import heapq
    queue = [(0, 0)]
    visited = [False] * vertices
    mstCost = 0
    while queue:
        current_weight, current_vertex = heapq.heappop(queue)
        if not visited[current_vertex]:
            visited[current_vertex] = True
            mstCost += current_weight

            for neighbour, weight in adj[current_vertex]:
                if not visited[neighbour]:
                    heapq.heappush(queue, (weight, neighbour))
    return mstCost

if __name__ == "__main__":
    vertices = 5
    edges = [[0, 1, 10], [0, 2, 15], [0, 3, 30], [1, 0, 10], [1, 3, 40], [2, 0, 15], [2, 3, 50], [3, 0, 30], [3, 1, 40], [3, 2, 50]]
    adjacency_list = createGraph(vertices, edges)
    print(f'The Minimum cost of MST is : {prims(adjacency_list, vertices)}')