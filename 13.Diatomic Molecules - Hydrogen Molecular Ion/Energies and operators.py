import numpy as np
import matplotlib.pyplot as plt
def J(r):
    return np.exp(-2*r)*(1+1.0/r)
def S(r):
    return np.exp(-r)*(1+r + (r**2)/3)
def K(r):
    return S(r)/r -np.exp(-r)*(1+r)
def E_plus(r):
    return  -1/2.0 + ( (J(r) + K(r))/(1.0-S(r)) )
def E_minus(r):
    return -1/2.0 + ( (J(r) - K(r))/(1.0-S(r)) )

r = np.linspace(0.2, 6.0, 100)
# Plot E_minus and E_plus as a function of R on the same plot
plt.plot(r,E_plus(r),label='$E_+$')
plt.plot(r,E_minus(r),label='$E_-$')
plt.ylabel('$E_+,\; E_-$')
plt.xlabel('r')
plt.legend(loc='best')
plt.ylim(-0.75,0)
plt.show()
plt.clf()
plt.plot(r,S(r),label='$S$')
plt.plot(r,J(r)-S(r)/r,label='$J$')
plt.plot(r,K(r)-S(r)/r,label='$K$')
plt.ylabel('$S,\; J,\;K$')
plt.xlabel('R')
plt.legend()
plt.show()