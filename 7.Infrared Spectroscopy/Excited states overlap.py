# function definition
def excited_overlap(t, omega_f, omega_0 = 1, lam = 1, E_0 = 1.0, m=1, hbar=1):
    energy_term= 1j*E_0*( (2*np.pi)/lam)
    denom_term = 2*np.sqrt(2*hbar*omega_0)
    term1 = (np.exp(-1j*(omega_0-omega_f)*t)-1) / (omega_0-omega_f)
    term2 = (np.exp(1j*(omega_0+omega_f)*t)-1 ) / (omega_0+omega_f)
    value = (energy_term/denom_term) *(term1+term2)
    return value
# initialize variables
t = np.arange(0,10,0.01)
omegas = [3.0,5.0,8.0,10.0]
prob_excited_state = np.zeros((len(omegas),len(t)))
# iterate over omegas
for indx, omega_f in enumerate(omegas):
    c1_t = excited_overlap(t, omega_f)
    prob_excited_state[indx,:] = np.abs(c1_t**2)
    plt.plot(t, prob_excited_state[indx,:],label='omega={}'.format(omega_f))
# plot
plt.xlabel('$t$')
plt.legend()
plt.ylabel('$|C_1(t)|^2$')
plt.show()