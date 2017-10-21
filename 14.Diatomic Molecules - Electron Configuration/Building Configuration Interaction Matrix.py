import numpy as np
import matplotlib.pyplot as plt
from quantumworldX.hydrogen import *

def energy_CI(R):
    H = np.array([[ E_ground(R)-V(R) , K12(R)  ],
                  [ K12(R) , E_excited(R)-V(R)  ]])
    E, psi = numpy.linalg.eigh(H)
    return E[0],E[1]

r = np.linspace(0.2, 10.0, 100)
e_ground = E_ground(r)
e_excited = E_excited(r)
ci_ground = np.zeros_like(r)
ci_excited = np.zeros_like(r)
for i in range(len(r)):
    ci_g, ci_e =  energy_CI(r[i])
    ci_ground[i] = ci_g + V(r[i])
    ci_excited[i] = ci_e + V(r[i])

# Plot E_ground(r) vs the ci_groundstate, what do you notice?
plt.plot(r,e_ground ,label='$E_{0}$')
plt.plot(r,ci_ground,label='$CI_{0}$')
plt.legend()
# Plot E_excited(r) vs the ci_excitedstate, what do you notice?
plt.plot(r,e_excited,label='$E_{1}$')
plt.plot(r,ci_excited,label='$CI_{1}$')
plt.legend(ncol=2)
plt.show()