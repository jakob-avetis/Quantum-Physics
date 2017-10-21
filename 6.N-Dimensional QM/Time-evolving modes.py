# initialize variables
t = np.linspace(0,4,80)
psit = np.zeros((len(t),xx.shape[0],xx.shape[1]))
# iterate over time
for indx,ti in enumerate(t):
    # time evolve and build snapshots
    c1_t = qw.cnt_evolve(c1, ti, E1)
    c2_t = qw.cnt_evolve(c2, ti, E2)
    psit[indx] = c1_t* psi1_xy + c2_t*psi2_xy
# get min and max values
z_min,z_max = np.min(psit),np.max(psit)
# plot several frames
for i in [1,20,40,60,80]:
    plt.clf()
    qw.plot_contours(xx,yy,psit[i-1],z_min,z_max)
    plt.show()