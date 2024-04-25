def addEdge(adj: list[list[int]], src: int, dest: int) -> None:
    adj[src].append(dest)
    adj[dest].append(src)
    print(adj)

def dfs(adj: list[list[int]], curr: int, vis: list[bool], dt: list[int], lt: list[int], time: int, parent: int) -> None:
    vis[curr]=True
    dt[curr] = lt[curr] = time[0]
    time[0]+=1
    for i in adj[curr]:
        if i==parent:
            continue
        elif not vis[i]:
            dfs(adj, i, vis, dt, lt, time, curr)
            lt[curr]=min(lt[curr],lt[i])
            if dt[curr] < lt[i]:
                print("Bridge is : ", curr, "---->", i)
        else:
            lt[curr]=min(lt[curr], dt[i])

def getBridge(adj: list[list[int]], vertices: int) -> None:
    dt=[-1]*vertices
    lt=[-1]*vertices
    time=[0]
    vis=[False]*vertices
    for i in range(vertices):
        if not vis[i]:
            dfs(adj, i, vis, dt, lt, time, -1)

def graph(vertices: int, edges: list[list[int]], noOfEdges: int) -> None:
    adj=[[] for _ in range(vertices)]

    for i in range(noOfEdges):
        addEdge(adj, edges[i][0], edges[i][1])

    getBridge(adj, vertices)

if __name__ == "__main__":
    edges=[[0,1],[0,2],[0,3],[1,2],[3,4],[3,5],[4,5]]
    vertices=6
    noOfEdges=len(edges)
    graph(vertices, edges, noOfEdges)