import numpy as np
import networkx as nx
import matplotlib.pyplot as plt
class network():
    def __init__(self,m):
        self.vertices = range(m+1)
        self.edges = []
        for i in self.vertices:
            edges_i = []
            for j in self.vertices:
                if i != j:
                    edges_i.append(j)
            self.edges.append(edges_i)

    def plot(self):
        graph = nx.Graph()
        graph.add_nodes_from(self.vertices)
        for i in range(len(self.edges)):
            for j in self.edges[i]:
                graph.add_edge(i,j)
        plt.plot()
        nx.draw(graph)
        plt.show()
        return

