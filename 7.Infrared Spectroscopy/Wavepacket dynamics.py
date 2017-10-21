#initialize variables
x = np.arange(-3, 3+0.01, 0.01)
t = np.linspace(0,4,250)
omega_f=3.0

psit = np.zeros((len(x),len(t)))
# iterate over time
for indt,ti in enumerate(t):
    psit[:,indt] =  qw.time_dependent_psi(x, ti, omega_f)
# time plot
qw.time_plot(x,psit,t,8)
plt.show()