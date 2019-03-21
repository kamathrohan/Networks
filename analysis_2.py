import numpy as np
import matplotlib.pyplot as plt
import networks as nw

a = np.genfromtxt("ra_3_10000.txt")
x1 = a[0]
y1 = a[1]

theo1 = nw.theoranet(x1,3)
x1log = np.log(x1)
y1log = np.log(y1)
plt.plot(x1log,y1log)
plt.plot(x1log,theo1)
plt.show()