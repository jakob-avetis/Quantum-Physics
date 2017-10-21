# initial conditions
B=4.82671733*10**(-5)
mu=0.425
l1,l2 = 0,1
t = np.linspace(0,70000,50)
dipole_moments_1=np.zeros(len(t))
dipole_moments_2=np.zeros(len(t))
dipole_moments_3=np.zeros(len(t))
# mixing coefficients (equal superposition)
c1_0 = 1.0/np.sqrt(2)
c2_0 = 1.0/np.sqrt(2)
# Assign the energy values
E1 = B*l1*(l1+1)
E2 = B*l2*(l2+1)
# iterate over time
for indt,ti in enumerate(t):
    # get the time-evolved coeficients
    c1_t = qw.cnt_evolve(c1_0, ti, E1)
    c2_t = qw.cnt_evolve(c2_0, ti, E2)
    # compute dipole moments for psi1, get value and store the value
    dp,_ = nquad(qw.dipole_moment_superposition_integrand, [[0,2*np.pi],[0,np.pi]], args=[mu,c1_t,c2_t,l1,0,l2,0])
    dipole_moments_1[indt] = dp
    # compute dipole moments for psi2, get value and store the value
    dp,_ = nquad(qw.dipole_moment_superposition_integrand, [[0,2*np.pi],[0,np.pi]], args=[mu,c1_t,c2_t,l1,0,l2,1])
    dipole_moments_2[indt] = dp
    # compute dipole moments for psi3, get value and store the value
    dp,_ = nquad(qw.dipole_moment_superposition_integrand, [[0,2*np.pi],[0,np.pi]], args=[mu,c1_t,c2_t,l1,0,l2,-1])
    dipole_moments_3[indt] = dp
# plot
plt.plot(t,dipole_moments_1,'-bo',label='$<\psi_1|\hat{\mu}|\psi_1>$')
plt.plot(t,dipole_moments_2,'-ro',label='$<\psi_2|\hat{\mu}|\psi_2>$')
plt.plot(t,dipole_moments_3,'-go',label='$<\psi_3|\hat{\mu}|\psi_3>$')
plt.title("Electric field of the rotor in time",fontsize=14)
plt.ylabel('$<\mu>$')
plt.xlabel('time')
plt.legend(loc='best')
plt.show()