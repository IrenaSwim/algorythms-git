from collections import defaultdict

def adjacency_list_graph(edges, indirected=False):
    adj_list = defaultdict(list)
    
    for u, v in edges:
        adj_list[u].append(v)
        if indirected:    
            adj_list[v].append(u) 
    print('Список смежности:')  
    for vertex in sorted(adj_list.keys()):
        print(f'вершина {vertex}: {sorted(adj_list[vertex])}') 
    return adj_list
    
def add_vertex(graph, vertex):
    graph[vertex] = []  
    return graph
    
def add_edge(graph, edge, indirected=False):
    u,v = edge
    graph[u].append(v) 
    if indirected:
        graph[v].append(u)
    return graph
    
edges1 = [('A', 'B'), ('A', 'C'), ('B', 'C'), ('B', 'D'), ('D','A')]    
list_graph = adjacency_list_graph(edges1, True)
add_vertex(list_graph, 'F')
print(list_graph)
add_edge(list_graph, ('G', 'A'), True)
print(list_graph)