# initial variables
x = np.linspace(-3.0, 3.0, 40)
p = np.linspace(-3.0, 3.0, 40)
xx, pp = np.meshgrid(x, p)
omega = 1.5
t = np.linspace(0,2*np.pi, 80)
wxpt = np.zeros((len(t),xx.shape[0],xx.shape[1]))
# iterate over t
for indx,ti in enumerate(t):
    x_t = np.cos(omega*ti)
    p_t = np.sin(omega*ti)
    wxpt[indx] = qw.HO_wigner(xx-x_t, pp-p_t, omega)
# calculate min, max
z_min, z_max = np.min(wxpt),np.max(wxpt)
# plotting several frames
for i in [1,20,40,60,80]:
    plt.clf()
    qw.plot_contours(xx,pp,wxpt[i-1],z_min,z_max)
    plt.show()