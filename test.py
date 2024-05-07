def addEdge(adj: list[list[list[int]]], src: int, dest: int, weight: int) -> None:
    adj[src].append([dest, weight])
    # print(adj)

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
    vertices = 9
    edges = [[0,1,7],[0,8,15],
             [1,0,7],[1,2,5],
             [2,1,5],[2,3,4],[2,4,2],[2,6,3],
             [3,2,4],[3,4,1],[3,5,9],
             [4,2,2],[4,3,1],
             [5,3,9],[3,7,12],[5,6,5],
             [6,2,3],[6,5,5],[6,8,6],
             [7,5,12],[7,8,10],
             [8,0,15],[8,6,6],[8,7,10]]
    noOfEdges = len(edges)
    graph(vertices, edges, noOfEdges)
