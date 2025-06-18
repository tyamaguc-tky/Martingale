#Two cell populations change the numbers by stochastic increase and decrease.
import numpy as np
n = 1
t_ind = 5
data_n = np.zeros((n,t_ind+1))
for j in range(n):
    amp = 0.1#0 in CSC
    if amp != 0:
        add = 0.001#0.1 in CSC
    else:
        add = 0.1
    qa = 1 * amp
    dec_min = 10**(-4)#10**(-7) * qa #for Fig3D
    xAxB = np.array([1, 1], dtype=int)#[6*6/qa*a/2, 6*6/qa*a/2]#initial values of x_a and x_b
    target = np.array([1, 2])
    target_ratio = target/np.sum(target)#Target ratio is [1/3, 2/3]
    tmax = 10**t_ind#10**5#the number of repetitions
    data_all = np.zeros((2, tmax + 1), int)#for recording
    xratio = xAxB/np.sum(xAxB)#initial value = [0.5, 0.5]

    def WGM(x=xratio,y=target_ratio):
        B = x!=0
        return   np.product(((y[B])/(x[B]))**(x[B]))
    
    for t in range(tmax):#repeat for tmax times
        data_all[:, t] = xAxB#record
        if np.random.rand() < amp:#competitive amplification
            if np.sum(xAxB) > 0:#xa + xb > 0
                rc = np.random.choice((0, 1), p=(xAxB)/np.sum(xAxB))#current ratio
                xAxB[rc] += 1#the selected xa or xb increases by one
        if np.random.rand() < add:#additive increase
            if amp != 0:#regulation with reinforcement learning
                rc = np.random.choice((0, 1), p=(0.5, 0.5))# 1:1 ratio
            else:#determinstic regulation
                rc = np.random.choice((0, 1), p=target_ratio)#correct 1:2 ratio
            xAxB[rc] += 1
        if np.sum(xAxB) > 0:#decay
            xratio = xAxB/np.sum(xAxB)#current ratio
            if amp != 0:#regulation with reinforcement learning
                dec = np.max([np.sum((xratio - target_ratio)**2)/2*qa, dec_min])#MSE/10
                #dec = np.max([np.abs(xratio - target_ratio)[0]*(amp/6), dec_min])#abs
                #dec = np.max([1 - WGM(x=xratio,y=target_ratio)**(2*np.log(1-0.1/36)/np.log(8/9)), dec_min])#0.047
                """
                #For stepwise decay 
                mse01 = np.sum((xratio - target_ratio)**2)/2/10
                if mse01 <= dec_min:
                    dec = dec_min
                elif mse01 <= dec_min*2:
                    dec = dec_min*2
                elif mse01 <= dec_min*20:
                    dec = dec_min*20
                else:
                    dec = dec_min*200
                """
            else:#CSC
                dec = dec_min
            xAxB = np.random.binomial(xAxB, 1 - dec)#binomial distribution with the probability of 1-dec
            if add == 0:
                xAxB[xAxB==0] = 1
    data_all[:, -1] = xAxB#record the last numbers
    for tt in range(t_ind +1):
        data_n[j,tt] = data_all[0,10**tt]/np.sum(data_all[:,10**tt])
d = data_all.T
import matplotlib.pyplot as plt#for presentation as figure
plt.plot(data_all[0,:])#xA
plt.plot(data_all[1,:])#xB
plt.show()