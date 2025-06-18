# -*- coding: utf-8 -*-
"""
Created on Mon May 19 16:56:02 2025

@author: tyama
"""

import numpy as np
#For 1-dimensional s-rw in Fig 3B
#Change init_pos and tmax 
def random_walk_1D(init_pos=10, tmax=100):
    sl_p = 0.1
    target = 0
    rand_d = 1 - np.random.rand(tmax) * 2 
    xt = init_pos
    traj = np.ones(tmax, dtype=float)
    traj[0] = xt
    for t in range(tmax - 1):
        if np.abs(xt) < 10**20:
            step_length = np.abs(xt - target) * sl_p
            xt += step_length * rand_d[t]            
        else:
            break
        traj[t + 1] = xt
    return xt#traj

test_n = 10**6
result = np.zeros(test_n , dtype=float)
for test in range(test_n):
    result[test] = random_walk_1D(init_pos=10, tmax=1000)#Fig 3B. init_pos=1,10,or 100, tmax=100 or 1000
print([np.mean(result),np.median(result)])

import matplotlib.pyplot as plt
loghist=plt.hist(np.log10(result),bins=1000, range=(-2,3))