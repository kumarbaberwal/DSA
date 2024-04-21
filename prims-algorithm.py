def addEdge(adj: list[list[list[int]]], src: int, dest: int, weight: int) -> None:
    adj[src].append([dest, weight])
    adj[dest].append([src, weight])
    print(adj)

def graph(vertices: int, edges: list[list[int]], noOfEdges: int) -> None:
    adj = [[] for _ in range(vertices)]
    for i in range(noOfEdges):
        addEdge(adj, edges[i][0], edges[i][1], edges[i][2])

    prims(adj, vertices)

def prims(adj:list[list[list[int]]], vertices:int) -> None:
    import heapq
    queue=[(0,0)]
    vis=[False]*vertices
    mstCost=0
    while queue:
        current_weight, current_node = heapq.heappop(queue)
        if not vis[current_node]:
            vis[current_node]=True
            mstCost += current_weight

            for i in adj[current_node]:
                weight = i[1]
                if not vis[i[0]]:
                    heapq.heappush(queue, (weight, i[0]))    
    print()
    print("Minimum Cost of MST :- ", mstCost)
    

if __name__ == "__main__":
    vertices = 4
    edges = [[0, 1, 10], [0, 2, 15], [0, 3, 30], [1, 3, 40], [2, 3, 50]]
    noOfEdges = len(edges)
    graph(vertices, edges, noOfEdges)
