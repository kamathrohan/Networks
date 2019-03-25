import matplotlib.pyplot as plt
import networks as nw
from scipy.stats import *


x1,y1,ytho1 = nw.raplotter("ra_3_100.txt",1)
x3,y3,ytho3 = nw.raplotter("ra_3_1000.txt",3)
x9,y9,ytho9 = nw.raplotter("ra_3_10000.txt",9)
x27,y27,ytho27 = nw.raplotter("ra_3_100000.txt",27)
#x81,y81,ytho81 = nw.raplotter("ra_3_1000000.txt",81)
"""


x81,y81,ytho81 = nw.raplotter("ra_3_10000.txt",81)
x243,y243,ytho243 = nw.raplotter("ra_243_1000.txt",243)
x729,y729,ytho729 = nw.raplotter("ra_729_1000.txt",729)

"""


plt.scatter(x1,y1,s= 5,label = "m = 1")
#plt.plot(x1,ytho1)
plt.scatter(x3,y3,s=5,label= "m = 3")
#plt.plot(x3,ytho3)
plt.scatter(x9,y9, s = 5,label = "m = 9")
#plt.plot(x9,ytho9)
plt.scatter(x27,y27, s = 5, label = "m = 27")
#plt.plot(x27,ytho27)
#plt.scatter(x81,y81, s = 2, label = "m = 81")
#plt.plot(x81,ytho81)
"""
plt.scatter(x243,y243, s = 2, label = "m = 243")


plt.plot(x243,ytho243)
plt.scatter(x729,y729 , s = 2, label = "m = 729")
plt.plot(x729,ytho729)
"""

plt.legend()
plt.grid()
plt.xlabel("log(k)")
plt.ylabel("log(p(k)")
#plt.savefig("ragraph.png")
plt.show()


"""
print(ks_2samp(y1,ytho1))
print(ks_2samp(y3,ytho3))
print(ks_2samp(y9,ytho9))
print(ks_2samp(y27,ytho27))
print(ks_2samp(y81,ytho81))

RA 
Ks_2sampResult(statistic=0.08, pvalue=0.9999941144269683)
Ks_2sampResult(statistic=0.03921568627450982, pvalue=0.9999999999985419)
Ks_2sampResult(statistic=0.05511811023622047, pvalue=0.9884443937359166)
Ks_2sampResult(statistic=0.06382978723404256, pvalue=0.5011033480033485)
Ks_2sampResult(statistic=0.07151370679380215, pvalue=0.02598158285127465)


BA
/Library/Frameworks/Python.framework/Versions/3.6/bin/python3.6 "/Users/rohankamath/Documents/Year 3/Complexity and Networks/Networks/logbinning_errors.py"
100%|███████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████| 50/50 [00:01<00:00, 28.63it/s]
0.9999994804037249
Ks_2sampResult(statistic=0.0434782608695653, pvalue=1.0)
100%|███████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████| 50/50 [00:03<00:00, 12.70it/s]
0.9999987097927363
Ks_2sampResult(statistic=0.040000000000000036, pvalue=1.0)
100%|███████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████| 50/50 [00:11<00:00,  4.46it/s]
0.9999617985591269
Ks_2sampResult(statistic=0.08333333333333334, pvalue=0.9999895542039052)
100%|███████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████| 50/50 [00:35<00:00,  1.41it/s]
0.9999843847221427
Ks_2sampResult(statistic=0.1, pvalue=0.9998979506885493)
100%|███████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████| 50/50 [02:30<00:00,  2.74s/it]
0.999996324564526
Ks_2sampResult(statistic=0.125, pvalue=0.999035232339821)

"""

