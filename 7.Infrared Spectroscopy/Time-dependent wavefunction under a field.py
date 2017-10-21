# function code
def time_dependent_psi(x, t, omega_f, omega_0 = 1, lam = 1, E_0 = 1, m=1, hbar=1):
    psi_0 = qw.harmonic_oscillator_wfn(x,0)
    term1 = 1j*E_0*(2*np.pi/lam) / (2*np.sqrt(2*m*hbar*omega_0))
    term2 = (np.exp(-1j*(omega_0-omega_f)*t)-1) / (omega_0-omega_f) + (np.exp(1j*(omega_0+omega_f)*t)-1) / (omega_0+omega_f)
    psi_1 = qw.harmonic_oscillator_wfn(x, 1)
    psi_x_t = psi_0 + term1 * term2*psi_1
    return psi_x_t

# initialized variables
dx = 0.01
x = np.arange(-3, 3+dx, dx)
ti=0.0
omega_f =3.0
# testing code
test = qw.time_dependent_psi(x, ti, omega_f)