edges=[[0,1],[0,2],[1,0],[1,3],[2,0],[2,4],[3,1],[3,4],[3,5],[4,2],[4,3],[4,5],[5,3],[5,4],[5,6],[6,5]]
noOfEdges=len(edges)
vertices=7

def addEdge(adj, src, desc):
    adj[src].append(desc)
    print(adj)


def graph(vertices, edges, noOfEdges):
    adj=[[] for i in range(vertices)]

    for i in range(noOfEdges):
        addEdge(adj, edges[i][0], edges[i][1])


graph(vertices, edges, noOfEdges)

def dfs(adj, current, arr):
    