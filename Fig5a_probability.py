import numpy as np
import matplotlib.pyplot as plt#for Fig5a
target = 1/3
x0 = 1/2
X0= np.abs(x0-target)
A = 0.1
t = 10
SS = 2*A*target*(1-target)
k = 1
def prob2(x=0.5,t=10):
    return X0/(x**3 * k* (2*t*SS*np.pi)**0.5) * (np.exp(-(1/x-1/X0)**2 /2/t/SS/k**2)-np.exp(-(1/x+1/X0)**2 /2/t/SS/k**2))
test_t = 10**3#1,10,100,10**3,10**4,10**5, or 10**6
xx = np.linspace(0.001,1,1000)
y = prob2(x=xx, t=test_t)
plt.plot(xx,y)
plt.show()
print(xx[np.argmax(y)])

Lx = np.linspace(-4,0,1000)
Zy = prob2(x=10**Lx, t=test_t) * 10**Lx *np.log(10) 
plt.plot(Lx,Zy)
plt.show()
