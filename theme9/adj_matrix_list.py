import numpy as np

def adj_matrix(v_num, edges):
    matrix = np.zeros((v_num, v_num))
    
    for edge in edges:
        u,v = edge
        matrix[u][v] = 1
    for row in matrix:
        print(row)   
    return matrix 
    
eds = [(0, 3), (2, 2), (3, 1)]  

mgraph = adj_matrix(4, eds)
    
def add_edge(graph, edge):
    u,v = edge
    graph[u][v] = 1
    return graph

def add_vertex(graph): 
    colomn = np.zeros(len(graph))
    graph = np.insert(graph, len(graph), colomn, axis=1)
    row = np.zeros((len(graph) + 1))
    graph = np.insert(graph, len(graph), row, axis=0)
    return graph

add_edge(mgraph, (3,0))   
print() 
print(mgraph)
print()
mgraph = add_vertex(mgraph)
for row in mgraph:
    print(row)