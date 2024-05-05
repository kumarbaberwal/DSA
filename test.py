def addEdge(adj: list[list[int]], src: int, dest: int, weight: int) -> None:
    adj[src].append([dest,weight])

def dijkstra(adj: list[list[int]], src: int, vertices: int) -> None:
    distances = [float('inf')] * vertices
    distances[src] = 0
    import heapq
    queue = [(0, src)]
    while queue:
        current_weight, current_node = heapq.heappop(queue)
        for neighbour, weight in adj[current_node]:
            if current_weight + weight < distances[neighbour]:
                distances[neighbour] = current_weight + weight
                heapq.heappush(queue,(distances[neighbour],neighbour))

    return distances

def graph(vertices: int, edges: list[list[int]], noOfEdges: int) -> None:
    adj = [[] for _ in range(vertices)]
    for i in range(noOfEdges):
        addEdge(adj, edges[i][0], edges[i][1], edges[i][2])
    # print(adj)
    print("Shortest Distance from the node 0: ", dijkstra(adj, 0, vertices))

if __name__ == "__main__" :
    vertices = 6
    edges = [[0,1,2],[0,2,4],[1,0,2],[1,2,1],[1,3,7],[2,0,4],[2,1,1],[2,4,3],[3,1,7],[3,4,2],[3,5,1],[4,2,3],[4,3,2],[4,5,5],[5,3,1],[5,4,5]]
    noOfEdges = len(edges)
    graph(vertices, edges, noOfEdges)
