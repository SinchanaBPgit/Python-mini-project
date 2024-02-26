import random

class Graph:
    def _init_(self):
        self.vertices = {}

    def add_vertex(self, vertex):
        if vertex not in self.vertices:
            self.vertices[vertex] = []

    def add_edge(self, vertex_from, vertex_to):
        self.add_vertex(vertex_from)
        self.add_vertex(vertex_to)
        self.vertices[vertex_from].append(vertex_to)

    def get_random_neighbor(self, vertex):
        if vertex in self.vertices:
            neighbors = self.vertices[vertex]
            return random.choice(neighbors)
        else:
            return None
