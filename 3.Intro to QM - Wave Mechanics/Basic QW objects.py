import numpy as np
# first three functions
def pib_eigenfunction(x, l, n):
    psi_x = np.sqrt(2.0 / l) * np.sin( (n * np.pi * x)/ l)
    return psi_x

def prob_density(psi_x):
    prob = np.conjugate(psi_x) * psi_x
    return prob

def pib_energy(n,l, hbar=1, m=1):
    E_n = (n * hbar * np.pi) ** 2 / (2.0 * m * l ** 2)
    return E_n

# finite diff function
def finite_diff(y, dx):
    # create variables
    n = len(y)
    grad = np.zeros(len(y))
    # edge case i=0
    grad[0] = (y[1] - y[0]) / dx
    # iterate over 'middle points"
    for i in range(1, n - 1):
        grad[i] = (y[i + 1] - y[i - 1]) / (2 * dx)
    # edge case i=n-1
    grad[n - 1] = (y[n - 1] - y[n - 2]) / dx
    return grad
