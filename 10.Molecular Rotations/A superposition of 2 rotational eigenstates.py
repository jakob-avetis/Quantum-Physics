# superposition function
def dipole_moment_superposition_integrand(phi, theta, mu, c1, c2, l1, m1, l2, m2):
    mu_operator = mu * (np.sin(theta) * np.cos(phi) +
                        np.sin(theta) * np.sin(phi) + np.cos(theta))
    Y_lm_1 = sph_harm(m1, l1, phi, theta)
    Y_lm_2 = sph_harm(m2, l2, phi, theta)
    # create superposition
    Y_lm = c1 * Y_lm_1 + c2 * Y_lm_2
    dV = np.sin(theta)
    integrand = np.conjugate(Y_lm) * mu_operator * Y_lm * dV
    return integrand
# initial conditions
B=4.82671733*10**(-5)
mu=0.425
# mixing coefficients (equal superposition)
c1_0 = 1.0/np.sqrt(2)
c2_0 = 1.0/np.sqrt(2)
# dipole one
dipole_moment_1, error = nquad(dipole_moment_superposition_integrand, [[0,2*np.pi],[0,np.pi]], args=[mu,c1_0,c2_0,0,0,1,0])
print("The dipole moment between Y_0^0 and Y_1^0 is: ",dipole_moment_1)
# dipole two
dipole_moment_2, error = nquad(dipole_moment_superposition_integrand, [[0,2*np.pi],[0,np.pi]], args=[mu,c1_0,c2_0,0,0,1,1])
print("The dipole moment between Y_0^0 and Y_1^1 is: ",dipole_moment_2)
# dipole three
dipole_moment_3, error = nquad(dipole_moment_superposition_integrand, [[0,2*np.pi],[0,np.pi]], args=[mu,c1_0,c2_0,0,0,1,-1])
print("The dipole moment between Y_0^0 and Y_1^-1 is: ",dipole_moment_3)