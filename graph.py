# row,column=3,3
# graph=[[0]*column]*row

# print(graph)
# graph[0][0]=1
# print(graph)

# Graphs using adjacency list 

def edge(graph, src, dest):
    graph[src].append(dest)

v=4

def graph