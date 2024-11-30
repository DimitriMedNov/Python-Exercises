# -*- coding: utf-8 -*-
"""
Created on Sat Nov 27 23:24:39 2021

@author: MedNo
"""

from queue import PriorityQueue

class Graph():

    def __init__(self, num_of_vertices):
        self.v = num_of_vertices
        self.edges = [[-1 for i in range(num_of_vertices)] for j in range(num_of_vertices)]
        self.visited = []
        
    def add_edge(self, u, v, weight):
        self.edges[u][v] = weight
        self.edges[v][u] = weight
        
    def dijkstra(self, start_vertex):
        D = {v:float('inf') for v in range(self.v)}
        D[start_vertex] = 0
        
        pq = PriorityQueue()
        pq.put((0, start_vertex))
        
        while not pq.empty():
            (dist, current_vertex) = pq.get()
            self.visited.append(current_vertex)
            
            for neighbor in range(self.v):
                if self.edges[current_vertex][neighbor] != -1:
                    distance = self.edges[current_vertex][neighbor]
                    if neighbor not in self.visited:
                        old_cost = D[neighbor]
                        new_cost = D[current_vertex] + distance
                        if new_cost < old_cost:
                            pq.put((new_cost, neighbor))
                            D[neighbor] = new_cost                            
        return D
     
     
v = Graph(9)
v.add_edge(0, 1, 4)
v.add_edge(0, 6, 7)
v.add_edge(1, 6, 11)
v.add_edge(1, 7, 20)
v.add_edge(1, 2, 9)
v.add_edge(2, 3, 6)
v.add_edge(2, 4, 2)
v.add_edge(3, 4, 10)
v.add_edge(3, 5, 5)
v.add_edge(4, 5, 15)
v.add_edge(4, 7, 1)
v.add_edge(4, 8, 5)
v.add_edge(5, 8, 12)
v.add_edge(6, 7, 1)
v.add_edge(7, 8, 3) 
    
D = v.dijkstra(1)
print ("Usted ha elegido la opcion: 9\n")
print ('------Grafos------'. center(30))
print("\n")
for vertex in range(len(D)):
    print("La Distancia de vertice 0 al vertice", vertex, "es", D[vertex])
    
print("\n")

    