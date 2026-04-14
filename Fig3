import numpy as np
import matplotlib.pyplot as plt#for presentation in Fig3
resol = 1000
x = np.array(range(0,resol))/resol
y =  ((x - 1/3)**2 + 1*10**-3)* ((x - 4/5)**2 + 5*10**-3)/2
plt.plot(x,np.log10(y))
plt.show()

resol = 10000
x = np.array(range(0,resol))/resol
y =  ((x - 1/3)**2 + 1*10**-3)* ((x - 4/5)**2 + 5*10**-3)/2
z = 0.101/y
z2 = z**2 
tot = np.sum(z2)
zz = z2/tot
wid_bin = 100
z_dens = np.zeros(wid_bin)
wid = resol//wid_bin
for i in range(wid_bin):
    z_dens[i] = np.sum(zz[wid *i : wid * (i+1)]) * wid_bin
plt.plot(z_dens)
