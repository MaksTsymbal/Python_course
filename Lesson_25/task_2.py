# Using breadth-first search write an algorithm that can determine the shortest path
# from each vertex to every other vertex. This is called the all-pairs shortest path problem.

from typing import List

def all_pairs_shortest_path(graph: List[List[int]]) -> List[List[int]]:
    n = len(graph)
    dist = [[float('inf') for _ in range(n)] for _ in range(n)]

    # Initialize distances with the given graph
    for i in range(n):
        for j in range(n):
            dist[i][j] = graph[i][j]

    # Perform breadth-first search for all pairs of vertices
    for k in range(n):
        for i in range(n):
            for j in range(n):
                if dist[i][k] != float('inf') and dist[k][j] != float('inf') and dist[i][k] + dist[k][j] < dist[i][j]:
                    dist[i][j] = dist[i][k] + dist[k][j]

    return dist

graph = [
    [0, 3, 8, float('inf')],
    [float('inf'), 0, float('inf'), 1],
    [float('inf'), 4, 0, float('inf')],
    [2, float('inf'), -5, 0]
]

shortest_paths = all_pairs_shortest_path(graph)
for row in shortest_paths:
    print(row)
