def addEdge(adj: list[list[int]], src: int, dest: int, weight: int) -> None:
    adj[src].append([dest,weight])
    # print(adj)

def dijkstra(adj: list[list[int]], src: int, vertices: int) -> None:
    distances = [float('inf')] * vertices
    distances[src] = 0
    import heapq
    queue = [(0, src)]
    while queue:
        # print(distances)
        current_weight, current_node = heapq.heappop(queue)
        for neighbour, weight in adj[current_node]:
            if distances[current_node] + weight < distances[neighbour]:
                distances[neighbour] = current_weight + weight
                heapq.heappush(queue,(distances[neighbour],neighbour))
                print(queue)

    return distances

def graph(vertices: int, edges: list[list[int]], noOfEdges: int) -> None:
    adj = [[] for _ in range(vertices)]
    for i in range(noOfEdges):
        addEdge(adj, edges[i][0], edges[i][1], edges[i][2])
    # print(adj)
    print("Shortest Distance from the node 0: ", dijkstra(adj, 0, vertices))

if __name__ == "__main__" :
    vertices = 9
    edges = [[0,1,4],[0,4,3],
             [1,0,4],[1,2,8],[1,4,11],
             [2,1,8],[2,3,7],[2,6,4],[2,8,2],
             [3,2,7],[3,6,14],[3,7,9],
             [4,0,3],[4,1,11],[4,5,1],[4,8,7],
             [5,4,1],[5,6,2],[5,8,6],
             [6,2,4],[6,3,14],[6,5,2],[6,7,10],
             [7,3,9],[7,6,10],
             [8,2,2],[8,4,7],[8,5,6]]
    noOfEdges = len(edges)
    graph(vertices, edges, noOfEdges)
