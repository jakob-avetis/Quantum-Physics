# define momentum operator function
def momentum_operator(psi_x, dx, hbar = 1):
    prefactor = -1j * hbar
    derivative = qw.finite_diff(psi_x, dx)
    return prefactor * derivative
# initialize variables
L = 10
dx = 0.01
x = np.arange(0,L,dx)
c1 = 1.0/np.sqrt(2)
c2 = 1.0/np.sqrt(2)
psi1_x = qw.pib_eigenfunction(x,L,1)
psi2_x = qw.pib_eigenfunction(x,L,2)
psi0 = c1*psi1_x + c2*psi2_x
# Expectation of position operator
x_integrand = np.conjugate(psi0)*x*psi0
exp_position = qw.complex_simps(x_integrand, x)
print('Expectation of position is', exp_position)
# Expectation of momentum operator
p_integrand = np.conjugate(psi0)*momentum_operator(psi0, dx)
exp_momentum = qw.complex_simps(p_integrand, x)
print('Expectation of momentum is', exp_momentum)