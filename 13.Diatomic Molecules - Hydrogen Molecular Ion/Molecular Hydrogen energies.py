import numpy as np
from quantumworldX.hydrogen import *
import matplotlib.pyplot as plt
#exercise
def E_ground(R):
    return 2*(H11(R)+H12(R))/(1+S12(R))+J11(R)+V(R)

def E_excited(R):
    return  2*(H11(R)- H12(R))/(1-S12(R))+J22(R)+V(R)

r = np.linspace(0.2, 10.0, 100)

e_ground = E_ground(r)
e_excited = E_excited(r)
r_min = r[np.argmin(e_ground)]
e_min = np.min(e_ground )
print('Ground minima at %2.2f Bohr with E=%f Hartrees'%(r_min,e_min))
plt.plot(r,e_ground,label='$E_{ground}$')
plt.plot(r,e_excited,label='$E_{excited}$')
plt.ylabel('$PES$')
plt.xlabel('R')
plt.ylim(-1.3,1)
plt.legend(loc='best')
plt.show()
# Plot J11, H11, and H12 as a function of R on the same plot
plt.clf()
plt.plot(r,J11(r),label='$J_{11}$')
plt.plot(r,H11(r),label='$H_{11}$')
plt.plot(r,H12(r),label='$H_{12}$')
plt.ylabel('$PES$')
plt.xlabel('R')
plt.legend(loc='best')
plt.show()
# Plot the 4 integrals, _1111, _1122, _1212, and _1112 as a function of R on the same plot.
plt.clf()
plt.plot(r,int_1111(r),label='$Int_{1111}$')
plt.plot(r,int_1122(r),label='$Int_{1122}$')
plt.plot(r,int_1212(r),label='$Int_{1212}$')
plt.plot(r,int_1112(r),label='$Int_{1112}$')
plt.ylabel('$Integral(R)$')
plt.xlabel('R')
plt.legend(loc='best',ncol=2)
plt.show()