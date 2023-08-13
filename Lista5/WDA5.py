import sys
import networkx as nx
import matplotlib.pyplot as plt
import random

class Graph:
    def __init__(self, edges):
        self.edges = edges
        self.graph_dict = {}
        for start, end, weight in edges:
            if start in self.graph_dict:
                self.graph_dict[start].append((end, weight))
            else:
                self.graph_dict[start] = [(end, weight)]
            if end not in self.graph_dict:
                self.graph_dict[end] = []
            if end in self.graph_dict:
                self.graph_dict[end].append((start, weight))
            else:
                self.graph_dict[end] = [(start, weight)]
            if start not in self.graph_dict:
                self.graph_dict[start] = []
        print("Przypisanie wierzchołków do poszczególnych składowych - 1 element krotki to wierzchołek, a 2 to waga krawędzi:", self.graph_dict)

        self.vertices = set(self.graph_dict.keys())
    def visualize_graph(self):
        graph = nx.Graph()
        edges = [(start, end) for start, end, _ in self.edges]
        graph.add_edges_from(edges)
        nx.draw(graph, with_labels=True)
        plt.show()

    def split_into_connected_components(self):
        graph = nx.Graph()
        edges_without_weights = [(start, end) for start, end, _ in self.edges]
        graph.add_edges_from(edges_without_weights)
        components = list(nx.connected_components(graph))

        components_dict = {}
        for i, component in enumerate(components):
            components_dict[i] = list(component)

        # Add entries for all vertices in the graph
        for vertex in self.vertices:
            if vertex not in components_dict:
                components_dict[vertex] = [vertex]

        return components_dict

    def dijkstra(self, start, end):
        distances = {vertex: sys.maxsize for vertex in self.graph_dict}
        distances[start] = 0
        visited = set()

        while visited != set(distances):
            current_vertex = min(
                set(distances) - visited, key=lambda vertex: distances[vertex]
            )
            visited.add(current_vertex)

            for neighbor, weight in self.graph_dict[current_vertex]:
                if neighbor not in visited:
                    new_distance = distances[current_vertex] + weight
                    if new_distance < distances[neighbor]:
                        distances[neighbor] = new_distance

        shortest_distance = distances[end]
        shortest_path = self.get_shortest_path(start, end, distances)

        return shortest_path, shortest_distance

    def get_shortest_path(self, start, end, distances):
        if start == end:
            return [start]

        shortest_path = []
        current_vertex = end

        while current_vertex != start:
            shortest_path.insert(0, current_vertex)

            for neighbor, _ in self.graph_dict[current_vertex]:
                if distances[current_vertex] == distances[neighbor] + self.get_weight(
                    current_vertex, neighbor
                ):
                    current_vertex = neighbor
                    break

        shortest_path.insert(0, start)
        return shortest_path

    def get_weight(self, start, end):
        for neighbor, weight in self.graph_dict[start]:
            if neighbor == end:
                return weight

        return sys.maxsize

    def kruskal(self):
        minimum_spanning_tree = []
        edges = sorted(self.edges, key=lambda x: x[2])  # Sortuj krawędzie rosnąco po wadze
        parent = {v: v for v in self.vertices}

        def find(v):
            if parent[v] != v:
                parent[v] = find(parent[v])
            return parent[v]

        def union(v1, v2):
            root1 = find(v1)
            root2 = find(v2)
            parent[root1] = root2

        for edge in edges:
            v1, v2, weight = edge
            if find(v1) != find(v2):
                minimum_spanning_tree.append(edge)
                union(v1, v2)

        return minimum_spanning_tree

    def prim(self):
        minimum_spanning_tree = []
        start_vertex = next(iter(self.vertices))
        visited = {start_vertex}
        candidates = []

        def add_edges(vertex):
            for neighbor, weight in self.graph_dict[vertex]:
                if neighbor not in visited:
                    candidates.append((vertex, neighbor, weight))

        add_edges(start_vertex)

        while candidates:
            v1, v2, weight = min(candidates, key=lambda x: x[2])
            candidates.remove((v1, v2, weight))
            if v2 not in visited:
                minimum_spanning_tree.append((v1, v2, weight))
                visited.add(v2)
                add_edges(v2)

        return minimum_spanning_tree
edges = [(random.randint(0, 9), random.randint(0, 9), random.randint(0, 9)) for _ in range(10)]
my_graph = Graph(edges)

minimum_spanning_tree_kruskal = my_graph.kruskal()
print("Algorytm Kruskala:")
for edge in minimum_spanning_tree_kruskal:
    print(f"{edge[0]} -- {edge[1]} : {edge[2]}")


minimum_spanning_tree_prima = my_graph.prim()
print("Algorytm Prima:")
for edge in minimum_spanning_tree_prima:
    print(f"{edge[0]} -- {edge[1]} : {edge[2]}")


my_graph.visualize_graph()