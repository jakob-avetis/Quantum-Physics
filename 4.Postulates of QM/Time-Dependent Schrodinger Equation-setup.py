# cnt evolve funtion
def cnt_evolve(cn_0, t, E_n, hbar = 1.0):
    exponent = (-1j*E_n*t) / hbar
    cn_t = cn_0 * np.exp(exponent)
    return cn_t
#initialize variables
L = 10
x = np.arange(0,L,0.01)
# construct first state
c1 = 1/np.sqrt(2)
psi1_x = qw.pib_eigenfunction(x,L,1)
E1 = qw.pib_energy(1, L)
# construct second state
c2 = 1/np.sqrt(2)
psi1_x = qw.pib_eigenfunction(x,L,1)
psi2_x = qw.pib_eigenfunction(x,L,2)
E1 = qw.pib_energy(1, L)
E2 = qw.pib_energy(2, L)
# superposition
psi0 = c1*psi1_x + c2*psi2_x
# norm
psi0_norm = qw.wfn_norm(x,psi0)
print('Norm is ',psi0_norm)
#plot
plt.plot(x, psi0)
plt.title('Psi at time = 0')
plt.xlabel('x (position)')
plt.ylabel('Psi(0)')
plt.show()