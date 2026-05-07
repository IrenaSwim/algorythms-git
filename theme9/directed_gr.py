from collections import deque 

class DirectedGraph:
    def __init__(self):
        self.graph = {}
    
    def add_vertex(self, vertex):
        if vertex not in self.graph:
            self.graph[vertex] = []
    
    def add_edge(self, u, v):
        if u not in self.graph:
            self.add_vertex(u)
        self.graph[u].append(v)
        
    def print_graph(self):
        for key,value in self.graph.items():
            print(f'{key} --> {value}')
            
gr = DirectedGraph()
gr.add_edge('A', 'B')  
gr.add_edge('A', 'C')   
gr.add_edge('B', 'C') 
gr.add_vertex('D')
gr.print_graph() 
print(gr.graph)
gr.add_edge('D','C')
gr.add_edge('D', 'E')
print(gr.graph)
print()

def breadth_first_search(graph, start):
    visited = set()
    queue = deque([start]) 
    #vertex_l = [] если нужно сохранить вершины в списке
    visited.add(start)
    while queue:
        vertex = queue.popleft()
        print(f'вершина {vertex}', end='---')
        #vertex_l.append(vertex)
        if vertex in graph.graph:
            for neighbour in graph.graph[vertex]:
                if neighbour not in visited:
                    visited.add(neighbour)
                    queue.append(neighbour)
        elif visited != set([key for key in graph.graph.keys()]):
            for key in graph.graph.keys():
                if key not in visited:          
                    visited.add(key)  
                    queue.append(key)
                    break
        else:
            break            
    #return vertex_l 
    
breadth_first_search(gr, 'D')
print() 
breadth_first_search(gr, 'A')
print()
breadth_first_search(gr, 'E') 
print()