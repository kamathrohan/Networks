import numpy as np
import matplotlib.pyplot as plt
import networks as nw
from scipy.optimize import curve_fit


def linfit(x,a,b):
    return a*x + b
a = np.genfromtxt("ba_3_100.txt")

x100 = np.log(a[0])
xcut100 = nw.banetcutoff(3,100)

"""
1000 is 853.33 29.795298471403164
100 is 636.822 21.810021622180937
10000 is 2623.65 90.90450195122352
100000 is 6013.63 206.87642429962867



a = np.genfromtxt("ba_3_1000.txt")
x1000 = np.log(a[0])
xcut1000 = nw.banetcutoff(3,1000)



a = np.genfromtxt("ba_3_10000.txt")
x10000 = np.log(a[0])
xcut10000 = nw.banetcutoff(3,10000)

a = np.genfromtxt("ba_3_100000.txt")
x100000 = np.log(a[0])
xcut100000 = nw.banetcutoff(3,100000)
y = [max(x100),max(x1000),max(x10000),max(x100000)]
x = [2,3,4,5]
popt, pcov = curve_fit(linfit,x,y)
print(popt/2.303)


plt.scatter([2,3,4,5],y)
plt.scatter([2,3,4,5],[xcut100,xcut1000,xcut10000,xcut100000])
plt.show()

"""

x = nw.racutoffsimulator(3,100,1000)
print("100 is",np.mean(x),(np.std(x)/10))
x = nw.racutoffsimulator(3,1000,100)
print("1000 is",np.mean(x),(np.std(x)/10))
x = nw.racutoffsimulator(3,10000,100)
print("10000 is",np.mean(x),(np.std(x)/10))
x = nw.racutoffsimulator(3,100000,100)
print("100000 is",np.mean(x),(np.std(x)/10))


