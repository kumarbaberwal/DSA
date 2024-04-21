def addEdge(adj: list[list[list[int]]], src: int, dest: int, weight: int) -> None:
    adj[src].append([dest, weight])
    print(adj)

def graph(vertices: int, edges: list[list[int]], noOfEdges: int) -> None:
    adj = [[] for _ in range(vertices)]
    for i in range(noOfEdges):
        addEdge(adj, edges[i][0], edges[i][1], edges[i][2])

    bellmanfold(adj, 0, vertices)

def bellmanfold(adj: list[list[list[int]]], src: int, vertices: int) -> None:
    distance = [float('inf')] * vertices
    distance[src] = 0
    for i in range(vertices - 1):
        for j in range(vertices):
            for edge in adj[j]:
                u = j
                v = edge[0]
                weight = edge[1]
                if distance[u] != float('inf') and distance[u] + weight < distance[v]:
                    distance[v] = distance[u] + weight
    
    for j in range(vertices):
            for edge in adj[j]:
                u = j
                v = edge[0]
                weight = edge[1]
                if distance[u] != float('inf') and distance[u] + weight < distance[v]:
                    print('Negative weight cycle!')
    
    print(distance)

if __name__ == "__main__":
    vertices = 5
    edges = [[0, 1, 2], [0, 2, 4], [1, 2, -4], [2, 3, 2], [3, 4, 4], [4, 1, -1]]
    noOfEdges = len(edges)
    graph(vertices, edges, noOfEdges)
