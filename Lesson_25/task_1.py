# Modify the `depth-first search` to produce strongly connected components (Strongly Connected Components ).

from collections import defaultdict


class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.graph = defaultdict(list)

    def add_edge(self, u, v):
        self.graph[u].append(v)

    def dfs(self, v, visited, stack):
        visited[v] = True

        for neighbor in self.graph[v]:
            if not visited[neighbor]:
                self.dfs(neighbor, visited, stack)

        stack.append(v)

    def get_transpose(self):
        transpose = Graph(self.V)

        for vertex in self.graph:
            for neighbor in self.graph[vertex]:
                transpose.add_edge(neighbor, vertex)

        return transpose

    def fill_order(self, v, visited, stack):
        visited[v] = True

        for neighbor in self.graph[v]:
            if not visited[neighbor]:
                self.fill_order(neighbor, visited, stack)

        stack.append(v)

    def get_scc(self):
        visited = [False] * (self.V)
        stack = []

        # Fill vertices in stack according to their finishing times
        for i in range(self.V):
            if not visited[i]:
                self.dfs(i, visited, stack)

        # Create the transpose graph
        transpose = self.get_transpose()

        # Reset visited array
        visited = [False] * (self.V)

        # Perform DFS on the transpose graph in the order defined by stack
        scc = []
        while stack:
            v = stack.pop()

            if not visited[v]:
                component = []
                transpose.fill_order(v, visited, component)
                scc.append(component)

        return scc


g = Graph(5)
g.add_edge(0, 1)
g.add_edge(1, 2)
g.add_edge(2, 0)
g.add_edge(1, 3)
g.add_edge(3, 4)

scc = g.get_scc()
print(scc)  # Output: [[4], [3], [1, 2, 0]]
