import numpy as np
import networkx as nx
import matplotlib.pyplot as plt
import random
from tqdm import tqdm
class network():
    def __init__(self,m):
        """

        :param m: number of edges added for every node
        """
        self.m = m
        self.vertices = list(range(m+1))
        self.edges = []
        for i in self.vertices:
            edges_i = []
            for j in self.vertices:
                if i != j:
                    edges_i.append(j)
            self.edges.append(edges_i)

    def plot(self):
        """

        :return: a plot
        """
        graph = nx.Graph()
        graph.add_nodes_from(self.vertices)
        for i in range(len(self.edges)):
            for j in self.edges[i]:
                graph.add_edge(i,j)
        plt.plot()
        nx.draw(graph)
        plt.show()
        return

class banet(network):
    def __init__(self,m):
        network.__init__(self,m)
        self.attachmentlist = []
        for i in range(len(self.edges)):
            for j in self.edges[i]:
                self.attachmentlist.append(i)

    def add_node(self):
        self.vertices.append(self.vertices[-1]+1)
        self.edges.append([])
        connections = [self.vertices[-1]]
        i = 0
        while i < self.m:
            pos = random.choice(self.attachmentlist)
            if pos in connections:
                pass
            else:
                connections.append(pos)
                self.edges[pos].append(self.vertices[-1])
                self.edges[self.vertices[-1]].append(pos)
                self.attachmentlist.append(pos)
                self.attachmentlist.append(self.vertices[-1])
                #self.plot()
                i = i + 1

b = banet(5)

for i in tqdm(range(100)):
    b.add_node()
plt.hist(b.attachmentlist)
plt.show()