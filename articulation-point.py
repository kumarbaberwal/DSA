# Finding Articulation Points in a Graph Using Tarjans Algorithm

def addEdge(adj: list[list[int]], src: int, dest: int) -> None:
    adj[src].append(dest)
    adj[dest].append(src)
    print(adj)

def dfs(adj: list[list[int]], curr: int, par: int, dt: list[bool], low: list[bool], vis: list[bool], time: list[int], ap : list[bool]) -> None:
    vis[curr] = True
    time[0] += 1
    dt[curr], low[curr] = time[0], time[0]
    children = 0
    for i in adj[curr]:
        if par == i:
            continue
        elif vis[i]:
            low[curr] = min(low[curr], dt[i])
        else:
            dfs(adj, i, curr, dt, low, vis, time, ap)
            low[curr] = min(low[curr], low[i])
            if dt[curr] <= low[i] and par != -1:
                ap[curr] = True
            
            children+=1
    
    if par == -1 and children >= 1:
        ap[curr] = True

def getAP(adj: list[list[int]], vertices: int) -> None:
    dt = [-1] * vertices
    low = [-1] * vertices
    time = [0]
    vis = [False] * vertices
    ap = [False] * vertices
    for i in range(vertices):
        if not vis[i]:
            dfs(adj, i, -1, dt, low, vis, time, ap)

    print()

    for i in range(vertices):
        if ap[i]:
            print('Articulation Point: ', i)


def graph(vertices: int, edges: list[list[int]], noOfEdges: int) -> None:
    adj=[[] for _ in range(vertices)]

    for i in range(noOfEdges):
        addEdge(adj, edges[i][0], edges[i][1])

    getAP(adj, vertices)

if __name__ == "__main__":
    vertices = 5
    edges = [[0,1],[0,2],[0,3],[1,2],[3,4]]
    noOfEdges = len(edges)
    graph(vertices, edges, noOfEdges)