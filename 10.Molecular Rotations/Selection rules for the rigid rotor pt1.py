# initialize variables
mu=0.425
l1_arr = np.arange(0,6)
l2_arr = np.arange(0,6)
trans_moment_l= np.zeros((len(l1_arr),len(l2_arr)))
# iterate over l1
for ind1,l1 in enumerate(l1_arr):
    # iterate over l2
    for ind2,l2 in enumerate(l2_arr):
        # calculate the trans_moment_l, store the absolute value
        dp,_ = nquad(qw.dipole_moment_integrand, [[0,2.0*np.pi],[0,np.pi]], args=[mu,l1,0,l2,0])
        trans_moment_l[ind1,ind2] = dp
# plot with imshow
plt.imshow(trans_moment_l, interpolation='nearest')
plt.colorbar()
plt.xlabel('$l_1$')
plt.ylabel('$l_2$')
plt.title('Transition Moment Integrals')
plt.show()