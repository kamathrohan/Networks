# -*- coding: utf-8 -*-
"""
Created on Wed Mar 20 11:00:48 2019

@author: rkk216
"""

import numpy as np
import matplotlib.pyplot as plt
import networks as nw


x = nw.ranetsimulator(3,100,smooth = 1000, logbinning = True,scale = 1.2)
np.savetxt("ra_3_100_logbin_1.2.txt",x)
x = nw.ranetsimulator(3,1000,smooth = 100, logbinning = True, scale = 1.2)
np.savetxt("ra_3_1000_logbin_1.2.txt",x)
x = nw.ranetsimulator(3,10000, logbinning = True, scale  =1.2)
np.savetxt("ra_3_10000_logbin_1.2.txt",x)
x = nw.ranetsimulator(3,100000, logbinning = True, scale = 1.2)
np.savetxt("ra_3_100000_logbin_1.2.txt",x)

