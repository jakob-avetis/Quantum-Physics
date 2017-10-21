# function defintion
def HO_wigner_01(x, p, t):
    u = p**2 + x**2
    wf = np.exp(-u)*(u + np.sqrt(2)*x*np.cos(t) - np.sqrt(2)*p*np.sin(t))
    return wf
# initial variables
x = np.linspace(-3.0, 3.0, 40)
p = np.linspace(-3.0, 3.0, 40)
xx, pp = np.meshgrid(x, p)
t = np.linspace(0,5, 80)
wxpt = np.zeros((len(t),xx.shape[0],xx.shape[1]))
# iterate over time
for indx,ti in enumerate(t):
    wxpt[indx] = HO_wigner_01(xx, pp, ti)
# calculate min,max
z_min,z_max = np.min(wxpt),np.max(wxpt)
# plotting several frames
for i in [1,20,40,60,80]:
    plt.clf()
    qw.plot_contours(xx,pp,wxpt[i-1],z_min,z_max)
    plt.show()