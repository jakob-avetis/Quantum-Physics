#initialize variables
L = 10
x = np.arange(0,L,0.01)
t = np.linspace(0,50,100)
psi = np.zeros((len(x),len(t)))
# construct first state
c1_0 = 1/np.sqrt(2)
psi1_x = qw.pib_eigenfunction(x,L,1)
E1 = qw.pib_energy(1, L)
# construct second state
c2_0 = 1/np.sqrt(2)
psi2_x = qw.pib_eigenfunction(x,L,2)
E2 = qw.pib_energy(2, L)
# iterate over time
for indt,ti in enumerate(t):
    # time evolve coefficients
    c1 = qw.cnt_evolve(c1_0, ti, E1)
    c2 = qw.cnt_evolve(c2_0, ti, E2)
    # save snapshot of psi
    psi[:,indt]= c1*psi1_x + c2*psi2_x
# time-plot
qw.time_plot(x,psi,t,t_step=2)
plt.show()