# define the function first
def dipole_moment_integrand(phi, theta, mu, l1, m1, l2, m2 ):
    mu_operator=mu*(np.sin(theta)*np.cos(phi) + np.sin(theta)*np.sin(phi) + np.cos(theta))
    Y_lm_1 = sph_harm(m1, l1, phi, theta)
    Y_lm_2 = sph_harm(m2, l2, phi, theta)
    dV=np.sin(theta)
    integrand=np.conjugate(Y_lm_1)*mu_operator*Y_lm_2*dV
    return integrand
# starting variables
mu=0.425
# example of how to compute the expectation for the dipole moment Y_0^0
dipole_m_00,_ = nquad(dipole_moment_integrand, [[0,2.0*np.pi],[0,np.pi]], args=[mu,0,0,0,0])
print("The dipole moment for Y^0_0 is: ",dipole_m_00)
# compute the expectation for the dipole moment Y_1^1
dipole_m_11,_ = nquad(dipole_moment_integrand, [[0,2.0*np.pi],[0,np.pi]], args=[mu,1,1,1,1])
print("The dipole moment for Y^1_1 is: ",dipole_m_11)