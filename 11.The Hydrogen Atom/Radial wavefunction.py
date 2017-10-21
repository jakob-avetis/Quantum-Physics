# inital variables
r=np.linspace(0.0, 30.0, 500)
l_m_list = [(1,0),(2,1),(3,0),(3,1),(5,2)]
ns = list(range(1,10))
r_wfn = np.zeros((len(l_m_list),len(r)))
r_exp = np.zeros(len(ns))
# iterate over the l/m list
for indx, i in enumerate(l_m_list):
    # get radial wfn, pdf and plot
    rad = r*qw.hydrogen.radial_wfn(r, i[0], i[1])
    r_wfn[indx]= qw.prob_density(rad)
    plt.plot(r,r_wfn[indx],label=str(i))
# extra plot stuff
plt.title('Radial Wfn. of H Atom')
plt.xlabel('Position')
plt.ylabel('$\psi$')
plt.legend()
plt.show()
plt.clf()
# iterate over 1 to 9
for indx,n  in enumerate(ns):
    # get radial expectation value and plot
    r_exp[indx], error = quad(qw.hydrogen.r_expectation_integrand, 0, np.inf, args=(n,0))
    plt.axvline(r_exp[indx])
# extra plot stuff
plt.xlabel('$ \langle r \\rangle$')
plt.ylabel('')
plt.show()