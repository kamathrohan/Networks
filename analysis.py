# -*- coding: utf-8 -*-
"""
Created on Wed Mar 20 11:00:48 2019

@author: rkk216
"""
import numpy as np
import matplotlib.pyplot as plt
import networks as nw
"""
a = np.genfromtxt("ra_3_100.txt")
x1 = a[0]
y1 = a[1]
xcut1 = nw.ranetcutoff(3,100)

a = np.genfromtxt("ra_3_1000.txt")
x3 = a[0]
y3 = a[1]
xcut3 = nw.ranetcutoff(3,1000)


a = np.genfromtxt("ra_3_10000.txt")
x9 = a[0]
y9 = a[1]
xcut9 = nw.ranetcutoff(3,10000)

a = np.genfromtxt("ra_3_100000.txt")
x27 = a[0]
y27 = a[1]
xcut27 = nw.ranetcutoff(3,100000)



yrat1 = []
xrat1 = []
for i in range(len(x1)):
    xrat1.append(x1[i]/xcut1)
    yrat1.append(y1[i]/nw.theoranet([x1[i]],3))
    

yrat3 = []
xrat3 = []
for i in range(len(x3)):
    xrat3.append(x3[i]/xcut3)
    yrat3.append(y3[i]/nw.theoranet([x3[i]],3))
    
    
yrat9 = []
xrat9 = []
for i in range(len(x9)):
    xrat9.append(x9[i]/xcut9)
    yrat9.append(y9[i]/nw.theoranet([x9[i]],3))
xrat27 = []    
    
yrat27 = []

for i in range(len(x27)):
    xrat27.append(x27[i]/xcut27)
    yrat27.append(y27[i]/nw.theoranet([x27[i]],3))
    


fig = plt.figure()
ax = plt.gca()
#ax.scatter(xrat1,yrat1)
#ax.scatter(xrat3,yrat3)
#ax.scatter(xrat9,yrat9)
ax.scatter(xrat27,yrat27)
ax.set_yscale('log')
ax.set_xscale('log')


plt.show()
x = nw.ranetsimulator(3,100,logbin = True)
np.savetxt("ra_3_100_num.txt",x)
x = nw.ranetsimulator(3,1000, logbin = True)
np.savetxt("ra_3_1000_num.txt",x)
x = nw.ranetsimulator(3,10000, logbin = True)
np.savetxt("ra_3_10000_num.txt",x)
"""
x = nw.ranetsimulator(3,100000, logbin = True)
np.savetxt("ra_3_100000_num.txt",x)
"""
x,y = nw.minetsimulator(3,100)
np.savetxt("mi_3_100.txt",[x,y])
x,y = nw.minetsimulator(3,1000)
np.savetxt("mi_3_1000.txt",[x,y])
x,y = nw.minetsimulator(3,10000)
np.savetxt("mi_3_10000.txt",[x,y])
x,y = nw.minetsimulator(3,100000)
np.savetxt("mi_3_100000.txt",[x,y])

"""