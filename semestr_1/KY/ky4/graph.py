from collections import defaultdict


class Graph:
    def __init__(self, vertices_num):
        self.graph = defaultdict(list)
        self.numberOfVertices = vertices_num

    def addEdge(self, vertex, edge):
        self.graph.setdefault(edge, [])
        self.graph[edge].append(vertex)

    def topogologicalSortUtil(self, v, visited, stack):
        visited.append(v)

        for i in self.graph[v]:
            if i not in visited:
                self.topogologicalSortUtil(i, visited, stack)

        stack.insert(0, v)

    def topologicalSort(self):
        visited = []
        stack = []
        print(self.graph)
        for k in list(self.graph):
            if k not in visited:
                self.topogologicalSortUtil(k, visited, stack)

        return stack