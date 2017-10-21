# initial variables
dx = 0.01
x = np.arange(0, 10, dx)
barrier = qw.square_barrier(x)
energies = np.linspace(1,25,20)
masses = np.linspace(0.5, 5, 20)
ee, mm = np.meshgrid(energies,masses)
transmission = np.zeros_like(ee)
# iterate over energies
for inde,e in enumerate(energies):
    # iterate over masses
    for indm,m in enumerate(masses):
        # operate over each combination
        psi_x = qw.plane_wave(x, e,m)
        psi_tunnel = qw.tunnel_findiff_propagate(x,psi_x,barrier,e)
        pdf = qw.prob_density(psi_tunnel)
        transmission[indm,inde]=qw.transmission_probability(pdf)
# plot contours
qw.plot_contours(ee,mm,transmission)
plt.xlabel('Energy')
plt.ylabel('Mass')
plt.title('Transmission probability')
plt.show()