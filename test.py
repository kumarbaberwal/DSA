def addEdge(adj: list[list[int]], src: int, dest: int, weight: int) -> None:
    adj[src].append([dest,weight])
    # print(adj)

def distances(adj: list[list[int]], vertices: int) -> None:
    distance=[[float('inf') for _ in range(vertices)] for _ in range(vertices)]
    # Set initial distances based on direct edges
    for i in range(vertices):
        for j, weight in adj[i]:
            distance[i][j] = weight
    
    # Set distance to self as 0
    for i in range(vertices):
        distance[i][i] = 0

    for k in range(vertices):
        for i in range(vertices):
            for j in range(vertices):
                distance[i][j]=min(distance[i][j],distance[i][k] + distance[k][j])

    print(distance)

def graph(vertices: int, edges: list[list[int]], noOfEdges: int) -> None:
    adj = [[] for _ in range(vertices)]
    for i in range(noOfEdges):
        addEdge(adj, edges[i][0], edges[i][1], edges[i][2])
    distances(adj, vertices)

if __name__ == "__main__" :
    vertices = 4
    edges = [[0,1,8],[0,3,1],
             [1,2,1],
             [2,3,1],
             [3,1,2],[3,2,9]]
    noOfEdges = len(edges)
    graph(vertices, edges, noOfEdges)
