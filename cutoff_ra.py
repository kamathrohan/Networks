import numpy as np
import matplotlib.pyplot as plt
import networks as nw
from scipy.optimize import curve_fit

"""
100 is 38.597 0.30236717745152164
1000 is 36.3 0.28861739379323625
10000 is 50.5 0.47360320944858475
100000 is 58.46 0.22821919288263204
"""



def linfit(x,a,b):
    return a*x + b
a = np.genfromtxt("ra_3_100.txt")

x100 = np.log(a[0])
xcut100 = nw.ranetcutoff(3,100)



a = np.genfromtxt("ra_3_1000.txt")
x1000 = np.log(a[0])
xcut1000 = nw.ranetcutoff(3,1000)



a = np.genfromtxt("ra_3_10000.txt")
x10000 = np.log(a[0])
xcut10000 = nw.ranetcutoff(3,10000)

a = np.genfromtxt("ra_3_100000.txt")
x100000 = np.log(a[0])
xcut100000 = nw.ranetcutoff(3,100000)

"""
y = [max(x100),max(x1000),max(x10000),max(x100000)]
x = [xcut100,xcut1000,xcut1000,xcut100000]
print(x)
print(y)

"""
