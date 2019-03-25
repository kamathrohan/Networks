import numpy as np
from scipy.stats import *
import matplotlib.pyplot as plt
import networks as nw
from tqdm import tqdm


"""
plt.errorbar(np.log(x[0]),np.log(x[1]), yerr =x[2])
plt.plot(np.log(x[0]),x[3])
x = baerrors(9,1000,100)
plt.errorbar(np.log(x[0]),np.log(x[1]), yerr =x[2])
plt.plot(np.log(x[0]),x[3])
x = baerrors(27,1000,100)
plt.errorbar(np.log(x[0]),np.log(x[1]), yerr =x[2])
plt.plot(np.log(x[0]),x[3])
x = baerrors(1,1000,100)
plt.errorbar(np.log(x[0]),np.log(x[1]), yerr =x[2])
plt.plot(np.log(x[0]),x[3])
plt.show()
"""


x = nw.baerrors(3,1000,100)

#print(nw.weightedlqs(np.log(x[1]),x[3],x[2]))
print(ks_2samp(np.log(x[1]),x[3]))
#print(chisquare(np.log(x[1]),x[3]))


