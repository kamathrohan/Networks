# -*- coding: utf-8 -*-
"""
Created on Wed Mar 20 11:00:48 2019

@author: rkk216
"""

import numpy as np
import matplotlib.pyplot as plt
import networks as nw


x = nw.banetsimulator(3,100,smooth = 10000, logbinning = True, scale = 1.3)
np.savetxt("ba_3_100_logbin_1.3.txt",x)
x = nw.banetsimulator(3,1000,smooth = 1000, logbinning = True, scale = 1.3)
np.savetxt("ba_3_1000_logbin_1.3.txt",x)
x = nw.banetsimulator(3,10000,smooth = 100, logbinning = True, scale = 1.3)
np.savetxt("ba_3_10000_logbin_1.3.txt",x)
x = nw.banetsimulator(3,100000,smooth = 100, logbinning = True, scale = 1.3)
np.savetxt("ba_3_100000_logbin_1.3.txt",x)
