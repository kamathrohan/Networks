import numpy as np
import networkx as nx
import matplotlib.pyplot as plt
import random
from tqdm import tqdm
import pandas as pd
import logbin230119 as logbin
import collections
from decimal import *

class network():
    def __init__(self, m):
        """

        :param m: number of edges added for every node
        """
        self.m = m
        self.vertices = list(range(m + 1))
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

    def probabilitydist(self, norm=False):
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
                graph.add_edge(i, j)
        plt.plot()
        nx.draw(graph)
        plt.show()
        return


class banet(network):
    def __init__(self, m):
        network.__init__(self, m)

    def add_node(self):
        self.vertices.append(self.vertices[-1] + 1)
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
                # self.plot()
                i = i + 1


class ranet(network):
    def __init__(self, m):
        network.__init__(self, m)

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
                # connections.append(pos)
                self.edges[pos].append(self.vertices[-1])
                self.edges[self.vertices[-1]].append(pos)
                self.attachmentlist.append(pos)
                self.attachmentlist.append(self.vertices[-1])
                # self.plot()
                i = i + 1
        return


class minet(network):
    def __init__(self, m):
        network.__init__(self, m)

    def add_node(self):
        i = 0
        while i < (self.m / 2):
            pos1 = random.choice(self.vertices)
            pos2 = random.choice(self.vertices)
            if pos1 == pos2:
                pass
            else:
                self.edges[pos1].append(pos2)
                self.edges[pos2].append(pos1)
                i = i + 1

        self.vertices.append(self.vertices[-1] + 1)
        self.edges.append([])
        connections = [self.vertices[-1]]
        i = 0
        while i < (self.m / 2):
            pos = random.choice(self.attachmentlist)
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


def theoranet(data, m):
    pk = []
    for k in data:
        k = np.float64(k)
        m = np.float64(m)
        numer = np.float64(m ** (k - m))
        denom = np.float64((1 + m) ** (1 + k - m))
        pki = numer / denom
        pk.append(pki)
    return pk


def theobanet(data, m):
    pk = []
    for k in data:
        numer = 2 * m * (m + 1)
        denom = (k + 2) * (k + 1) * k
        pki = numer / denom
        pk.append(pki)
    return pk

def theominet(data,m):
    pk = []
    for k in data:
        numer = np.log(12*m) + np.log(3*m+1) + np.log(3*m+2) + np.log(3*m +3)
        denom = np.log(k + 2*m +4) + np.log(k + 2*m +3 )+ np.log(k+2*m+2) + np.log(k +2*m +1)+np.log(k+2*m)
        pki = numer - denom
        pk.append(pki)
    return pk


def ranetcutoff(m, N):
    numer = np.log(N)
    denom = np.log(m) - np.log(m+1)
    k1 = m - (numer/denom)
    return k1



def banetsimulator(m, N, smooth=100,logbinning = False, scale = 1.3):
    b = banet(m)
    numbers = []
    for j in tqdm(range(smooth)):
        for i in range(N):
            b.add_node()
        n = b.probabilitydist()
        for i in n:
            numbers.append(i)

    numbers.sort()
    if logbinning == True:
        x,y = logbin.logbin(numbers, scale = scale)
    else:
        prob = collections.Counter(numbers)
        x, y = zip(*prob.items())
        y = y / np.sum(y)
    return x, y
    return x, y


def ranetsimulator(m, N, smooth=100, logbinning = False, scale = 1.3):
    b = ranet(m)
    numbers = []
    for j in tqdm(range(smooth)):
        for i in range(N):
            b.add_node()
        n = b.probabilitydist()
        for i in n:
            numbers.append(i)
    numbers.sort()
    if logbinning == True:
        x,y = logbin.logbin(numbers, scale = scale)
    else:
        prob = collections.Counter(numbers)
        x, y = zip(*prob.items())
        y = y / np.sum(y)
    return x, y

def minetsimulator(m, N, smooth=100):
    b = minet(m)
    numbers = []
    for j in tqdm(range(smooth)):
        for i in range(N):
            b.add_node()
        n = b.probabilitydist()
        for i in n:
            numbers.append(i)

    numbers.sort()
    prob = collections.Counter(numbers)
    x, y = zip(*prob.items())
    y = y / np.sum(y)
    return x, y

#x2,y2 =ranetsimulator(3,10000)
#np.savetxt("ra_3_10000.txt",[x2,y2])