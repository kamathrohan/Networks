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
        self.vertices.append(self.vertices[-1] + 1)
        self.edges.append([])
        connections = [self.vertices[-1]]
        i = 0
        r = np.int(self.m/2)
        while i < (self.m-r):
            pos = random.choice(self.attachmentlist)
            if pos in connections:
                pass
            else:
                self.edges[pos].append(self.vertices[-1])
                self.edges[self.vertices[-1]].append(pos)
                self.attachmentlist.append(pos)
                self.attachmentlist.append(self.vertices[-1])
                i = i + 1
        i = 0

        while i < r:
            pos1 = random.choice(self.vertices)
            pos2 = random.choice(self.vertices)
            if pos1 == pos2:
                pass
            else:
                self.edges[pos1].append(pos2)
                self.edges[pos2].append(pos1)
                self.attachmentlist.append(pos1)
                self.attachmentlist.append(pos2)
                i = i + 1

def theoranet(data, m):
    pk = []
    for k in data:
        numer = (k - m)*np.log(m)
        denom =  (1 + k - m)*np.log((1 + m))
        pki = numer - denom
        pk.append(pki)
        #print(type(pki))
    return pk

def theobanet(data, m):
    pk = []
    for k in data:
        numer = np.log(2 * m * (m + 1))
        denom = np.log((k + 2) * (k + 1) * k)
        pki = numer - denom
        pk.append(pki)
    return pk

def theominet(data,m):
    pk = []
    for k in data:
        numer = np.log((9/4)*m*((9*m)+2)*((9*m)+4)*((9*m) +6))
        denom = np.log((k + (4*m) +4)*(k + (4*m) +3)*(k+(4*m)+2)*(k +(4*m) +1)*(k+4*m))
        pki = numer - denom
        pk.append(pki)
    return pk

def theominet2(data,m):
    pk = []
    for k in data:
        numer = np.log(12*m*(3*m+1)*((3*m)+2)*((3*m) +3))
        denom = np.log((k + (2*m) +4)*(k + (2*m) +3)*(k+(2*m)+2)*(k +(2*m) +1)*(k+2*m))
        pki = numer - denom
        pk.append(pki)
    return pk

def ranetcutoff(m, N):
    numer = np.log(N)
    denom = np.log(m) - np.log(m+1)
    k1 = m - (numer/denom)
    return np.log(k1)

def banetcutoff(m, N):
    a = 1 + (4*N*m*(m+1))
    numer = np.sqrt(a)- 1
    return np.log(numer/2)

def banetsimulator(m, N, smooth=100,logbinning = False, scale = 1.3):
    b = banet(m)
    numbers = []
    for j in range(smooth):
        for i in range(N):
            b.add_node()
        n = b.probabilitydist()
        for i in n:
            numbers.append(i)

    numbers.sort()
    if logbinning == True:
        x,y = logbin.logbin(numbers, scale = scale)
        return x ,y
    else:
        prob = collections.Counter(numbers)
        x, y = zip(*prob.items())
        y = y / np.sum(y)
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

def minetsimulator(m, N, smooth=100, logbinning = False, scale = 1.3):
    b = minet(m)
    numbers = []
    for j in tqdm(range(smooth)):
        for i in range(N):
            b.add_node()
        n = b.probabilitydist()
        for i in n:
            numbers.append(i)

    numbers.sort()
    if logbinning == True:
        x,y, ystddv = logbin.logbin2(numbers, scale = scale)
        return x, y
    else:
        prob = collections.Counter(numbers)
        x, y = zip(*prob.items())
        y = y/ (np.sum(y))
        return x, y

def baplotter(data,m):
    a = np.genfromtxt(data)
    x = a[0]
    y = a[1]
    ytho = theobanet(x,m)
    return np.log(x),np.log(y),ytho

def raplotter(data,m):
    a = np.genfromtxt(data)
    x = a[0]
    y = a[1]
    ytho = theoranet(x,m)
    return np.log(x),np.log(y),ytho

def miplotter(data,m):
    a = np.genfromtxt(data)
    x = a[0]
    y = a[1]
    ytho = theoranet(x,m)
    return np.log(x),np.log(y),ytho

def racutoffsimulator(m, N, smooth=100):
    b = ranet(m)
    maximum = []
    for j in tqdm(range(smooth)):
        for i in range(N):
            b.add_node()
        n = b.probabilitydist()
        prob = collections.Counter(n)
        x, y = zip(*prob.items())
        maximum.append(max(x))
    return maximum

def bacutoffsimulator(m, N, smooth=100):
    b = banet(m)
    maximum = []
    for j in tqdm(range(smooth)):
        for i in range(N):
            b.add_node()
        n = b.probabilitydist()
        prob = collections.Counter(n)
        x, y = zip(*prob.items())
        maximum.append(max(x))
    return maximum

def baerrors(m,N,smooth):
    ymas = []
    xmas = []
    for i in tqdm(range(smooth)):
        x, y = banetsimulator(m, N, smooth=1, logbinning=True, scale=1.2)
        ymas.append(y)
        xmas.append(x)
    lengths = [len(i) for i in ymas]
    l = max(lengths)
    argmax = np.argmax(lengths)
    xnew = xmas[argmax]
    b = len(ymas)

    ymasnew = np.zeros((b, l))
    for i in range(len(ymas)):
        for j in range(len(ymas[i])):
            ymasnew[i][j] = ymas[i][j]
    ymean = np.mean(ymasnew, axis=0)
    ystddv = np.std(ymasnew, axis=0)
    ytheo = theobanet(xnew,m)
    yerr = [(ystddv[i] / ymean[i]) for i in range(len(xnew))]
    return [xnew,ymean,yerr,ytheo]

def leastsq(data, theory):
    residue = 0
    totalsumsq = 0
    mean = np.average(data)
    for i in range(len(data)):
        rs = (data[i] - theory[i])**2
        sumsq = (data[i] - mean)**2
        residue = residue + rs
        totalsumsq = totalsumsq + sumsq
    rsq = 1 - (residue/totalsumsq)
    return rsq

def weightedlqs(data, theory, error):
    residue = 0
    totalsumsq = 0
    mean = np.average(data)
    for i in range(len(data)):
        rs = (data[i] - theory[i])**2
        sumsq = ((data[i] - mean)/error[i])**2
        residue = residue + rs
        totalsumsq = totalsumsq + sumsq
    rsq = 1 - (residue/totalsumsq)
    return rsq
