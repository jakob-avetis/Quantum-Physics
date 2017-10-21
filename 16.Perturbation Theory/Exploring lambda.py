import matplotlib.pyplot as plt
import numpy as np
from quantumworldX.helium import H_lambda
hartree2ev = 27.211399

lambdas = np.linspace(0,1,100)
c_g = np.zeros_like(lambdas)
c_e = np.zeros_like(lambdas)
e_ground = np.zeros_like(lambdas)

for i,lam in enumerate(lambdas):
    H = H_lambda(lam)
    eigvals, eigvecs = np.linalg.eigh(H)
    c_g[i] = eigvecs[0,0]
    c_e[i] = eigvecs[1,0]
    e_ground[i] = eigvals[0]
###################
plt.plot(lambdas, c_g**2, lw=4)
plt.plot(lambdas, c_e**2, lw = 4)
plt.legend(('$\psi_0$ (ground)','$\psi_1$ (singlet excited)'))
plt.ylim((0, 1.5))
plt.xlabel('$\lambda$ parameter (electron interaction strength)')
plt.ylabel('$c_1$ and $c_2$ coefficients')
plt.title('Contributions from ground and singlet excited vs. $\lambda$')
plt.show()
plt.axhline(-79,label="$E_{Exact}$")
plt.plot(lambdas, e_ground*hartree2ev, lw=4,label='$E_{CI}(\lambda)$')
plt.xlabel('$\lambda$ parameter (electron interaction strength)')
plt.ylabel('Ground State energy')
plt.title('CI ground state energy estimate vs. $\lambda$')
plt.legend(loc='best')
plt.show()    