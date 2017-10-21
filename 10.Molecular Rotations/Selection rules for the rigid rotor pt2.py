# initialize variables
mu=0.425
l1,l2 = 5,6
m1_arr = np.arange(-5,6)
m2_arr = np.arange(-5,6)
trans_moment_m= np.zeros((len(m1_arr),len(m2_arr)))
# iterate over m1
for ind1,m1 in enumerate(m1_arr):
    # iterate over m2
    for ind2,m2 in enumerate(m2_arr):
        # calculate transition moment
        dp,_ = nquad(qw.dipole_moment_integrand, [[0,2.0*np.pi],[0,np.pi]], args=[mu,l1,m1,l2,m2])
        trans_moment_m[ind1,ind2] = dp
# plot
plt.imshow(np.abs(trans_moment_m), interpolation='nearest',extent=[-5,5,-5,5])
plt.colorbar()
plt.xlabel('$m_1$')
plt.ylabel('$m_2$')
plt.title('Transition Moment Integrals')
plt.show()