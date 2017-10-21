import numpy as np
import matplotlib.pyplot as plt
import quantumworldX as qw
# initalize variables
omegas = np.linspace(0,3,95)
t = np.arange(0,30,0.1)
#exercise
ir_spectrum = np.zeros_like(omegas)
# iterate over omegas
for indx, omega_f in enumerate(omegas):
    # calculate overlaps, integrate, save result
    c1_t = qw.excited_overlap(t, omega_f)
    transition_amplitude = qw.complex_simps(c1_t,t)
    ir_spectrum[indx] = np.abs(transition_amplitude)**2
#plot
plt.plot(omegas, ir_spectrum)
plt.xlabel('$\omega_f$')
plt.ylabel('Absorption intensity')
plt.title('IR Spectrum')
plt.show()