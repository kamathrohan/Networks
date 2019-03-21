# -*- coding: utf-8 -*-
"""
Created on Wed Mar 20 16:26:42 2019

@author: rkk216
"""
import numpy as np
import matplotlib.pyplot as plt
import networks as nw
import logbin230119 as logbin

a = np.genfromtxt("ra_3_100_logbin.txt")

x100 = a[0]
y100 = a[1]
xcut100 = nw.ranetcutoff(3,100)


a = np.genfromtxt("ra_3_1000_logbin.txt")
x1000 = a[0]
y1000 = a[1]
xcut1000 = nw.ranetcutoff(3,1000)

a = np.genfromtxt("ra_3_10000_logbin.txt")
x10000 = a[0]
y10000 = a[1]
xcut10000 = nw.ranetcutoff(3,10000)

a = np.genfromtxt("ra_3_100000_logbin.txt")
x100000 = a[0]
x100000 = a[1]
xcut100000 = nw.ranetcutoff(3,100000)



yrat100 = []
xrat100 = []
for i in range(len(x100)):
    xrat100.append(x100[i]/xcut100)
    yrat100.append(y100[i]/nw.theoranet([x100[i]],3))
plt.loglog(xrat100,yrat100)
    

yrat1000 = []
xrat1000 = []
for i in range(len(x1000)):
    xrat1000.append(x1000[i]/xcut1000)
    yrat1000.append(y1000[i]/nw.theoranet([x1000[i]],3))
    
    
yrat10000 = []
xrat10000 = []
for i in range(len(x10000)):
    xrat10000.append(x10000[i]/xcut10000)
    yrat10000.append(y10000[i]/nw.theoranet([x10000[i]],3))

fig = plt.figure()
ax = plt.gca()
ax.scatter(xrat100,yrat100)
ax.scatter(xrat1000,yrat1000)
ax.scatter(xrat10000,yrat10000)

ax.set_yscale('log')
ax.set_xscale('log')


plt.show()
