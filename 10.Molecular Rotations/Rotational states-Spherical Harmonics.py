from scipy.special import sph_harm
# define the function
def sph_harm_real(m, l, phi, theta):
    Y_lm = sph_harm(m, l, phi, theta)
    if m < 0:
        Y_lm_real = np.sqrt(2.0) * (-1.0)**m * Y_lm.imag
    elif m > 0:
        Y_lm_real = np.sqrt(2.0) * (-1.0)**m * Y_lm.real
    else:
        Y_lm_real = Y_lm
    return Y_lm_real

# plot one spherical harmonics, m=2,l=2
qw.plot_spherical_harmonics(2,2)
plt.show()
# plot one spherical harmonics, m=1,l=2
plt.clf()
qw.plot_spherical_harmonics(1,2)
plt.show()
plt.clf()