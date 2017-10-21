l1,m1 = 0, 0
l2, m2 = 1, 2
# first eigenfunction
c1 = 1/np.sqrt(2)
E1 = (l1+m1+1)
psi1_xy = qw.harmonic_oscillator_2D(xx,yy,l1,m1)
#second eigenfunction
c2 = 1/np.sqrt(2)
psi2_xy = qw.harmonic_oscillator_2D(xx,yy,l2,m2)
E2 = (l2+m2+1)
# superposition
psi0 = c1* psi1_xy + c2*psi2_xy
# plot
qw.plot_contours(xx,yy,psi0)
plt.show()