edges=[[0,1,2], [0,2,4], [1,3,7], [1,2,1], [2,4,3], [3,5,1], [4,3,2], [4,5,5]]
noOfEdges=len(edges)

def addEdge(adj:list[list[list[int]]], src:int, dest:int, weight:int) -> None:
    adj[src].append([dest,weight])
    adj[dest].append([src,weight])
    print(adj)

def printGraph(adj:list[list[list[int]]], v:int):

    for i in range(v):
        print('Node',i , 'makes an edge with')

        for j in adj[i]:
            print('\tNode', j[0], 'with edge weight = ', j[1])
        print()

v=6
adj=[[] for i in range(v)]

import heapq

def dijkstra(adj:list[list[int]], src:int, vertices:int):
    arr=[False]*vertices
    distance=[float('inf')]*vertices
    distance[src]=0
    queue=[(0,src)]
    while queue:
        current_weight, current_node= heapq.heappop(queue)
        if current_weight > distance[current_node]:
            continue
        for neighbor, weight in adj[current_node]:
            if distance[current_node] + weight < distance[neighbor]:
                distance[neighbor] = distance[current_node] + weight
                heapq.heappush(queue, (distance[neighbor], neighbor))
    return distance


def graph(v, edges, noOfEdges):

    for i in range(noOfEdges):
        addEdge(adj,edges[i][0],edges[i][1],edges[i][2])
    

graph(v, edges, noOfEdges)
printGraph(adj,v)

start_node = 0
distances = dijkstra(adj, start_node, v)
print("\nShortest distances from node", start_node, "to other nodes:")
print(distances)