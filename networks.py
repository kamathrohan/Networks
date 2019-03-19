import numpy as np
import networkx as nx
import matplotlib.pyplot as plt
import random
from tqdm import tqdm
import pandas as pd
import logbin230119 as logbin
import collections

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
        self.attachmentlist = []
        for i in range(len(self.edges)):
            for j in self.edges[i]:
                self.attachmentlist.append(i)

    def probabilitydist(self, norm = False):
        """

        :return: x,y of distributions
        """

        numbers = []
        for i in self.vertices:
            numbers.append(len(self.edges[i]))


        return numbers


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

class ranet(network):
    def __init__(self,m):
        network.__init__(self,m)


    def add_node(self):
        self.vertices.append(self.vertices[-1] + 1)
        self.edges.append([])
        connections = [self.vertices[-1]]
        i = 0
        while i < self.m:
            pos = random.choice(self.vertices)
            if pos in connections:
                pass
            else:
                connections.append(pos)
                self.edges[pos].append(self.vertices[-1])
                self.edges[self.vertices[-1]].append(pos)
                self.attachmentlist.append(pos)
                self.attachmentlist.append(self.vertices[-1])
                # self.plot()
                i = i + 1
        return

class minet(network):
    def __init__(self,m):
        network.__init__(self,m)

    def add_node(self):
        i = 0
        while i < (self.m/2):
            pos1 = random.choice(self.vertices)
            pos2 = random.choice(self.vertices)
            if pos1 == pos2:
                pass
            else:
                self.edges[pos1].append(pos2)
                self.edges[pos2].append(pos1)
                i = i + 1

        self.vertices.append(self.vertices[-1]+1)
        self.edges.append([])
        connections = [self.vertices[-1]]
        i = 0
        while i < (self.m/2):
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


b = banet(1)
numbers = []

for j in tqdm(range(2000)):
    for i in range(10000):
        b.add_node()
    n = b.probabilitydist()
    for i in n:
        numbers.append(i)


numbers.sort()
prob = collections.Counter(numbers)
x, y = zip(*prob.items())
plt.loglog(x,y)
plt.show()



np.savetxt('2e3_1e4.csv',numbers)

#TODO implement scatter plot instead of plt.plot
