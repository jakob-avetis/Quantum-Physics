# function definition
def HO_wigner(x, p, w, m = 1.0, hbar = 1.0):
    position = np.exp(-(m*w* (x**2))/hbar)
    momentum = np.exp(-(p**2)/(m*w*hbar))
    return position*momentum/(np.pi*hbar)
# initialize variables
omega = 1.0
x = np.linspace(-3.0, 3.0, 50)
p = np.linspace(-3.0, 3.0, 50)
# get meshgrid, use function
xx, pp = np.meshgrid(x, p)
wxp = HO_wigner(xx, pp, omega)
# plotting
qw.plot_contours(xx,pp,wxp)
plt.show()