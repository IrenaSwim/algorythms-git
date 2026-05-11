def floyd_warshall(graph):
    n = len(graph)
    dist = [[float('inf')] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if i == j:
                dist[i][j] = 0
            elif graph[i][j] != 0:
                dist[i][j] = graph[i][j]
                
    for k in range(n):
        for i in range(n):
            for j in range(n):
                if dist[i][k] + dist[k][j] < dist[i][j]:
                    dist[i][j] = dist[i][k] + dist[k][j]
                    
    return dist               
                

mdw_graph = [
    [0, 3, 8, 0, 0],
    [3, 0, 4, 2, 0],
    [8, 4, 0, 1, 5],
    [0, 2, 1, 0, 3],
    [0, 0, 5, 3, 0]
]

short_paths = floyd_warshall(mdw_graph)   

for row in short_paths:
    print(row)