import numpy as np
import quantumworldX as qw
H = qw.helium.ci_hamiltonian()
hartree_to_ev = 27.211399 # conversion factor
eigvals, eigvecs = np.linalg.eigh(H)
# retrieve ground state info
ci_g =eigvals[0]*hartree_to_ev
c0_g =eigvecs[0,0]
c1_g = eigvecs[1,0]
print('The c0 and c1 coefficients are --> ', eigvecs[:,0] )
# calculate error
exact_g = -79
verypoor_g = -108.8
rel_error = np.abs(exact_g - ci_g)/np.abs(exact_g)*100
print('Exact Energy -->',exact_g,'eV')
print('Very Poor Mans approx. --> ',verypoor_g,'eV')
print('Our Configuration interaction estimate --> ', ci_g,'eV')
print('With a relative error of ',rel_error,'%')