import numpy as np

def adj_matrix_graph(vertex_num, edges, indirected=False):
    matrix = [[0] * vertex_num for _ in range(vertex_num)]
    
    for u, v in edges:
        matrix[u][v] = 1
        if indirected:
            matrix[u][v] = 1
            
    return matrix    
          
def insert_vertex(graph):
    graph.append([0]*len(graph))
    for row in graph:
        row.append(0)
    return graph
    
def insert_edage(graph, edge, indirected=False):
    u, v = edge
    graph[u][v] = 1
    if indirected:
        graph[v][u] = 1
    
    return graph  
        
edges2 = [(0, 2), (2, 3), (3, 1)]
m_graph = adj_matrix_graph(4, edges2)  
insert_vertex(m_graph)
for row in m_graph:
    print(row)
print()    
insert_edage(m_graph, (4, 1))  
for row in m_graph:
    print(row)

# вариант с библиотекой numpy
# def adj_matrix(v_num, edges):
#     matrix = np.zeros((v_num, v_num))
    
#     for edge in edges:
#         u,v = edge
#         matrix[u][v] = 1
#     for row in matrix:
#         print(row)   
#     return matrix 
    
# eds = [(0, 3), (2, 2), (3, 1)]  

# mgraph = adj_matrix(4, eds)
    
# def add_edge(graph, edge):
#     u,v = edge
#     graph[u][v] = 1
#     return graph

# def add_vertex(graph): 
#     colomn = np.zeros(len(graph))
#     graph = np.insert(graph, len(graph), colomn, axis=1)
#     row = np.zeros((len(graph) + 1))
#     graph = np.insert(graph, len(graph), row, axis=0)
#     return graph

# add_edge(mgraph, (3,0))   
# print() 
# print(mgraph)
# print()
# mgraph = add_vertex(mgraph)
# for row in mgraph:
#     print(row)