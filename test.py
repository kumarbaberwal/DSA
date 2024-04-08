# Python3 program to represent undirected 
# and weighted graph. The program basically 
# prints adjacency list representation of graph

# To add an edge
def addEdge(adj, u, v, wt):
	
	adj[u].append([v, wt])
	adj[v].append([u, wt])
	return adj

# Print adjacency list representation of graph
def printGraph(adj, V):
	
	v, w = 0, 0
	for u in range(V):
		print("Node", u, "makes an edge with")

		for it in adj[u]:
			v = it[0]
			w = it[1]
			print("\tNode", v, "with edge weight =", w)
			
		print()

# Driver code
if __name__ == '__main__':
	
	V = 5
	adj = [[] for i in range(V)]

	adj = addEdge(adj, 0, 1, 10)
	adj = addEdge(adj, 0, 4, 20)
	adj = addEdge(adj, 1, 2, 30)
	adj = addEdge(adj, 1, 3, 40)
	adj = addEdge(adj, 1, 4, 50)
	adj = addEdge(adj, 2, 3, 60)
	adj = addEdge(adj, 3, 4, 70)

	printGraph(adj, V)

# This code is contributed by mohit kumar 29
