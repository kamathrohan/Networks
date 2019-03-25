import numpy as np
from scipy.stats import *
import matplotlib.pyplot as plt
import networks as nw
from tqdm import tqdm
x = nw.baerrors(1,10000,50)
plt.errorbar(np.log(x[0]),np.log(x[1]), yerr =x[2], label = "m =1")
print(nw.weightedlqs(np.log(x[1]),x[3],x[2]))
print(ks_2samp(np.log(x[1]),x[3]))
plt.plot(np.log(x[0]),x[3])
x = nw.baerrors(3,10000,50)
print(nw.weightedlqs(np.log(x[1]),x[3],x[2]))
print(ks_2samp(np.log(x[1]),x[3]))
plt.errorbar(np.log(x[0]),np.log(x[1]), yerr =x[2],label = "m =3")
plt.plot(np.log(x[0]),x[3])
x = nw.baerrors(9,10000,50)
print(nw.weightedlqs(np.log(x[1]),x[3],x[2]))
print(ks_2samp(np.log(x[1]),x[3]))
plt.errorbar(np.log(x[0])[1:],np.log(x[1][1:]), yerr =x[2][1:], label = "m =9")
plt.plot(np.log(x[0]),x[3])
x = nw.baerrors(27,10000,50)
print(nw.weightedlqs(np.log(x[1]),x[3],x[2]))
print(ks_2samp(np.log(x[1]),x[3]))
plt.errorbar(np.log(x[0])[1:],np.log(x[1][1:]), yerr =x[2][1:], label = "m =27")
plt.plot(np.log(x[0]),x[3])
x = nw.baerrors(81,10000,50)
print(nw.weightedlqs(np.log(x[1]),x[3],x[2]))
print(ks_2samp(np.log(x[1]),x[3]))
plt.errorbar(np.log(x[0])[1:],np.log(x[1][1:]), yerr =x[2][1:], label = "m =81")
plt.plot(np.log(x[0]),x[3])

plt.xlabel("$log(k)$",fontsize = 12)
plt.ylabel("$log(p(k)$", fontsize = 12)
plt.legend()
plt.grid()
plt.show()

"""


#print(nw.weightedlqs(np.log(x[1]),x[3],x[2]))
print(ks_2samp(np.log(x[1]),x[3]))
#print(chisquare(np.log(x[1]),x[3]))

"""




