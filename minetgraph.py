import matplotlib.pyplot as plt
import networks as nw

import numpy as np
"""

x3,y3,ytho3 = nw.miplotter("mi_3_10000.txt",3)
x9,y9,ytho9 = nw.miplotter("mi_9_10000.txt",9)
x27,y27,ytho27 = nw.miplotter("mi_27_10000.txt",27)
x81,y81,ytho81 = nw.miplotter("mi_81_10000.txt",81)
x243,y243,ytho243 = nw.miplotter("mi_243_1000.txt",243)
x729,y729,ytho729 = nw.miplotter("mi_729_1000.txt",729)


plt.scatter(x3,y3,s=1,label= "m = 3")
plt.scatter(x3,ytho3, s = 1)
plt.scatter(x9,y9,s=1)
plt.scatter(x9,ytho9, s = 1,label = "m = 9")
plt.scatter(x27,y27,s=1)
plt.scatter(x27,ytho27, s = 1, label = "m = 27")
plt.scatter(x81,y81,s=1)
plt.scatter(x81,ytho81, s = 1, label = "m = 81")
plt.scatter(x243,y243,s=1)
plt.scatter(x243,ytho243, s = 1, label = "m = 243")
plt.scatter(x729,y729,s=1)
plt.scatter(x729,ytho729, s = 1, label = "m = 729")
plt.legend()
plt.xlabel("log(k)")
plt.ylabel("log(p(k)")
plt.show()
"""
x,y = nw.minetsimulator(8,1000,smooth = 100)
ytheo1 = nw.theominet2(x,8)
plt.scatter(np.log(x),ytheo1,label = "T")
plt.scatter(np.log(x),np.log(y), label = "sim")
plt.legend()
plt.show()