# -*- coding: utf-8 -*-
"""
Created on Wed Mar 20 11:00:48 2019

@author: rkk216
"""

import numpy as np
import matplotlib.pyplot as plt
import networks as nw


x = nw.minetsimulator(729,1000,smooth = 10)
np.savetxt("mi_729_1000.txt",x)
#x = nw.banetsimulator(3,1000,smooth = 100, logbinning = True, scale = 1.2)
#np.savetxt("ra_3_1000_logbin_1.2.txt",x)
#x = nw.banetsimulator(3,10000, logbinning = True, scale  =1.2)
#np.savetxt("ra_3_10000_logbin_1.2.txt",x)
#x = nw.banetsimulator(3,100000, logbinning = True, scale = 1.2)
#np.savetxt("ra_3_100000_logbin_1.2.txt",x)

