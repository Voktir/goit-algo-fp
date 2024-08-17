import heapq

class Graph:
    def __init__(self, num_vertices):
        self.V = num_vertices
        self.graph = [[] for _ in range(num_vertices)]

    def add_edge(self, u, v, w):
        self.graph[u].append((v, w))

def dijkstra(graph, start):
    # Ініціалізація відстаней та купи
    dist = [float('inf')] * graph.V
    dist[start] = 0
    heap = [(0, start)]

    while heap:
        (d, u) = heapq.heappop(heap)
        for v, w in graph.graph[u]:
            if dist[v] > dist[u] + w:
                dist[v] = dist[u] + w
                heapq.heappush(heap, (dist[v], v))

    return dist

# Приклад використання
g = Graph(9)
g.add_edge(0, 6, 1)
g.add_edge(0, 1, 4)
g.add_edge(1, 2, 1)
g.add_edge(2, 3, 1)
g.add_edge(3, 4, 3)
g.add_edge(4, 5, 5)
g.add_edge(5, 6, 2)
g.add_edge(6, 7, 4)
g.add_edge(7, 8, 7)

# Знаходження найкоротших шляхів від вершини 0
shortest_distances = dijkstra(g, 0)
print(shortest_distances)