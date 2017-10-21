# initialize variabales
L = 3
r=1.21
x = np.linspace(-L,L,500)
v_x = qw.coulomb_double_well(x,r)
# build and solve system
H = qw.build_hamiltonian(x,v_x)
eigenvalues, eigenvectors = np.linalg.eigh(H)
# plot the first 2 eigenstates
for i in range(2):
    plt.plot(x, eigenvectors[:,i], linewidth=4,label='psi_'+str(i) )
plt.xlabel('x')
plt.ylabel('f(x)')
plt.legend()    
plt.show()
# build and solve system
H_one = qw.build_hamiltonian(x,qw.coulomb_well(x,r))
eigenvalues_one, eigenvectors_one = np.linalg.eigh(H_one)