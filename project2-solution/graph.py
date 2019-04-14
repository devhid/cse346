from util import to_adjlist
from math import inf
from collections import deque

class Graph:
    def __init__(self, matrix):
        self.graph = to_adjlist(matrix)
        self.vertices = list(self.graph.keys())

    def add_edge(self, src, dst, cost):
        self.graph[src].append((dst, cost))
        self.graph[dst].append((src, cost))

    def remove_edge(self, src, dst):
        src_remove = -1
        dst_remove = -1

        for edge in self.graph[src]:
            if edge[0] == dst:
                src_remove = edge
                break

        for edge in self.graph[dst]:
            if edge[0] == src:
                dst_remove = edge
                break

        if src_remove != -1:
            self.graph[src].remove(src_remove)
        
        if dst_remove != -1:
            self.graph[dst].remove(dst_remove)

    def djikstra(self, src, dst):
        # set distances to be inf for all vertices.
        distances = {vertex: inf for vertex in self.vertices}

        # keeps track of the path
        previous = {vertex: None for vertex in self.vertices}

        # set distance for starting vertex to 0
        distances[src] = 0

        # keep track of unvisited vertices
        vertices = self.vertices.copy()

        while vertices:
            # get an unvisited node with the smallest distance
            current_vertex = min(vertices, key=lambda vertex: distances[vertex])

            # remove current vertex since it is now visited
            vertices.remove(current_vertex)

            # stop traversing once the distance of the current vertex is inf
            if distances[current_vertex] == inf:
                break

            # for each unvisited neighbor, calculate its distance from current node
            for neighbor in self.graph[current_vertex]:
                vertex = neighbor[0]
                cost = neighbor[1]

                new_distance = distances[current_vertex] + cost

                # save the smaller distance between the two compared ones
                if vertex in distances and new_distance < distances[vertex]:
                    distances[vertex] = new_distance
                    previous[vertex] = current_vertex

        # build path from src to dst
        path, current_vertex = deque(), dst
        while previous[current_vertex] is not None:
            path.appendleft(current_vertex)
            current_vertex = previous[current_vertex]

        if path:
            path.appendleft(current_vertex)
        
        return list(path)
    
    def remove_links(self, path):
        for i in range(len(path) - 1):
            self.remove_edge(path[i], path[i + 1])

    def get_total_distance(self, path):
        total_distance = 0

        for i in range(len(path) - 1):
            vertex = path[i]
            for edge in self.graph[vertex]:
                if edge[0] == path[i + 1]:
                    total_distance += edge[1]
                    break
        
        return total_distance

        

    