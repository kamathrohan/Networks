# -*- coding: utf-8 -*-
"""
Created on Wed Mar 20 16:26:42 2019

@author: rkk216
"""
import numpy as np
import matplotlib.pyplot as plt
import networks as nw
import logbin230119 as logbin

a = np.genfromtxt("ba_3_100_logbin_1.3.txt")

x100 = np.log(a[0])
y100 = np.log(a[1])
xcut100 = nw.banetcutoff(3,100)


a = np.genfromtxt("ba_3_1000_logbin_1.3.txt")
x1000 = np.log(a[0])
y1000 = np.log(a[1])
xcut1000 = nw.banetcutoff(3,1000)



a = np.genfromtxt("ba_3_10000_logbin_1.3.txt")
x10000 = np.log(a[0])
y10000 = np.log(a[1])
xcut10000 = nw.banetcutoff(3,10000)

a = np.genfromtxt("ba_3_100000_logbin_1.3.txt")
x100000 = np.log(a[0])
y100000 = np.log(a[1])
xcut100000 = nw.banetcutoff(3,100000)



yrat100 = []
xrat100 = []
for i in range(len(x100)):
    xrat100.append(x100[i] - xcut100 -1 )
    yrat100.append(y100[i] - nw.theobanet([np.exp(x100[i])],3))
    

yrat1000 = []
xrat1000 = []
for i in range(len(x1000)):
    xrat1000.append(x1000[i] - xcut1000 -1 )
    yrat1000.append(y1000[i] - nw.theobanet([np.exp(x1000[i])],3))
    
    
yrat10000 = []
xrat10000 = []
for i in range(len(x10000)):
    xrat10000.append(x10000[i] - xcut10000 -1 )
    yrat10000.append(y10000[i] - nw.theobanet([np.exp(x10000[i])],3))
    
yrat100000 = []
xrat100000 = []
for i in range(len(x100000)):
    xrat100000.append(x100000[i] - xcut100000 - 1)
    yrat100000.append(y100000[i] - nw.theobanet([np.exp(x100000[i])],3))


plt.scatter(xrat100,yrat100,label = "n = 100")
plt.scatter(xrat1000,yrat1000,label = "n = 1000")
plt.scatter(xrat10000,yrat10000, label = "n = 10000")
plt.scatter(xrat100000,yrat100000, label = "n = 100000")
plt.legend()
plt.grid()
plt.xlabel('$log(k/k_1)$')
plt.ylabel('$log(p/p_\infty)$')
plt.savefig("Datacollapse.png")
plt.show()
