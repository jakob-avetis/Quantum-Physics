# initialize variables
L = 1.0
dx =0.05
x = np.arange(0,L+dx,dx)
v_x = linear_ramp(x)
# build and solve system
H = qw.build_hamiltonian(x,v_x)
eigenvalues, eigenvectors = np.linalg.eigh(H)
# get the first eigenvector
psi0 = eigenvectors[:,0]
# get the norm, should we normalize? get the pdf
psi0_norm = qw.wfn_norm(x, psi0)
print(psi0_norm)
psi0 = qw.normalize_wfn(x, psi0)
pdf = qw.prob_density(psi0)
#plot
plt.plot(x, psi0, linewidth=4,label='psi0' )
plt.plot(x, pdf, linewidth=4,label='pdf')
plt.xlabel('x')
plt.ylabel('f(x)')
plt.legend()    
plt.show()