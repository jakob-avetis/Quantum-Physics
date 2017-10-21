# t_p function
def transmission_probability(pdf,n_cutoff=300):
    p_avg = np.mean(pdf[-n_cutoff:])
    t_p = 2.0/(1+p_avg)
    return t_p
#initial variables
x = np.arange(0, 10, 0.01)
barrier = qw.square_barrier(x)
m=1
energies = np.arange(0, 25, 0.1)
transmission = np.zeros_like(energies)
# iterate over energies
for indx,e in enumerate(energies):
    psi_x = qw.plane_wave(x, e)
    psi_tunnel = qw.tunnel_findiff_propagate(x,psi_x,barrier,e)
    pdf = qw.prob_density(psi_tunnel)
    transmission[indx]=transmission_probability(pdf)
# plot
plt.plot(energies,transmission)
plt.title('Transmission vs. Energy')
plt.xlabel(' Energy')
plt.ylabel('Transmission probability')
plt.show()