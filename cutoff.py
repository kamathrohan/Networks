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


plt.errorbar([2,3,4,5],y, yerr= [0.5349011910709605, 0.4317803494143086, 0.3686752343480782, 0.24390243902439025]
,fmt = 'o',label = "Sim")
plt.plot([2,3,4,5],[xcut100  + 2.303,xcut1000 + 2.303,xcut10000 + 2.303,xcut100000 + 2.303], label = "Observed")
plt.grid()
plt.xlabel("$log(N)$")
plt.ylabel("$log(k_1)$")

plt.show()




k1 =[]
kerr = []



x = nw.bacutoffsimulator(1,100,1000)
k1.append(np.mean(x))
kerr.append(np.std(x))

x = nw.bacutoffsimulator(1,1000,100)
k1.append(np.mean(x))
kerr.append(np.std(x))

x = nw.bacutoffsimulator(1,10000,10)
k1.append(np.mean(x))
kerr.append(np.std(x))

x = nw.bacutoffsimulator(1,100000,2)
k1.append(np.mean(x))
kerr.append(np.std(x))

print(k1)
print(kerr)

k1 =[]
kerr = []



x = nw.bacutoffsimulator(3,100,1000)
k1.append(np.mean(x))
kerr.append(np.std(x))

x = nw.bacutoffsimulator(3,1000,100)
k1.append(np.mean(x))
kerr.append(np.std(x))

x = nw.bacutoffsimulator(3,10000,10)
k1.append(np.mean(x))
kerr.append(np.std(x))

x = nw.bacutoffsimulator(3,100000,2)
k1.append(np.mean(x))
kerr.append(np.std(x))

print(k1)
print(kerr)

k1 =[]
kerr = []



x = nw.bacutoffsimulator(9,100,1000)
k1.append(np.mean(x))
kerr.append(np.std(x))

x = nw.bacutoffsimulator(9,1000,100)
k1.append(np.mean(x))
kerr.append(np.std(x))

x = nw.bacutoffsimulator(9,10000,10)
k1.append(np.mean(x))
kerr.append(np.std(x))

x = nw.bacutoffsimulator(9,100000,2)
k1.append(np.mean(x))
kerr.append(np.std(x))

print(k1)
print(kerr)


"""

theocutoff = [nw.ranetcutoff(1,i) for i in [100,1000,10000,100000]]
k1 = [16.822, 18.03, 19.4, 20.5]
kerr = [1.2362507836195697, 1.4996999699939986, 1.6852299546352716, 0.5]
logk1 = np.log(k1)
logkerr = [kerr[i]/k1[i] for i in range(len(kerr))]

plt.errorbar([2,3,4,5],logk1,yerr = logkerr,label = "m = 1 (sim)")
plt.plot([2,3,4,5],theocutoff, label =  "m = 1 (theo)")

theocutoff = [nw.ranetcutoff(3,i) for i in [100,1000,10000,100000]]
k1 = [38.824, 43.78, 46.2, 48.0]
kerr = [3.488126144507965, 3.545645216318181, 1.98997487421324, 1.0]

logk1 = np.log(k1)
logkerr = [kerr[i]/k1[i] for i in range(len(kerr))]

plt.errorbar([2,3,4,5],logk1,yerr = logkerr, label = "m = 3 (sim)")
plt.plot([2,3,4,5],theocutoff, label = "m = 3 (theo)")

theocutoff = [nw.ranetcutoff(9,i) for i in [100,1000,10000,100000]]
k1 = [102.882, 110.01, 120.3, 130.0]
kerr = [10.992819292610971, 10.979521847512306, 8.46226919921601, 4.0]
logk1 = np.log(k1)
logkerr = [kerr[i]/k1[i] for i in range(len(kerr))]

plt.errorbar([2,3,4,5],logk1,yerr = logkerr,label = "m = 6 (sim)")
plt.plot([2,3,4,5],theocutoff, label =  "m = 6 (theo)")



plt.grid()
plt.xlabel("$log(N)$")
plt.ylabel("$log(k_1)$")
plt.ylim(1,5)
plt.legend()
plt.show()


"""


theocutoff = [nw.banetcutoff(1,i) for i in [100,1000,10000,100000]]
k1 = [189.994, 296.16, 430.3, 661.0]

kerr = [62.91465669368446, 99.11455190838528, 141.35278561103775, 111.0]
logk1 = np.log(k1)*2.303 - 9
logkerr = [kerr[i]/k1[i] for i in range(len(kerr))]

plt.errorbar([2,3,4,5],logk1,yerr = logkerr,label = "m = 1 (sim)")
plt.plot([2,3,4,5],theocutoff, label =  "m = 1 (theo)")

theocutoff = [nw.banetcutoff(3,i) for i in [100,1000,10000,100000]]
k1 = [418.668, 561.24, 797.4, 1106.5]
kerr = [175.97975956342253, 199.56648616438585, 237.38753126480756, 198.5]

logk1 = np.log(k1)*2.303 -9
logkerr = [kerr[i]/k1[i] for i in range(len(kerr))]

plt.errorbar([2,3,4,5],logk1,yerr = logkerr, label = "m = 3 (sim)")
plt.plot([2,3,4,5],theocutoff, label = "m = 3 (theo)")

theocutoff = [nw.banetcutoff(9,i) for i in [100,1000,10000,100000]]
k1 = [845.856, 1065.83, 1273.9, 1836.0]
kerr = [395.12126906052526, 373.7574094248835, 395.85463240942374, 317.0]
logk1 = np.log(k1)*2.303 -9
logkerr = [kerr[i]/k1[i] for i in range(len(kerr))]

plt.errorbar([2,3,4,5],logk1,yerr = logkerr,label = "m = 9 (sim)")
plt.plot([2,3,4,5],theocutoff, label =  "m = 9 (theo)")



plt.grid()
plt.xlabel("$log(N)")
plt.ylabel("$log(k_1)$")
plt.legend()
plt.show()
"""