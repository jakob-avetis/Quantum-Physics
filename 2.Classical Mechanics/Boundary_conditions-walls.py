v = 1.75
dt = 0.001
m = 1
t = np.arange(0,1+dt,dt)
x = np.zeros(len(t))
x[0] = 0.0
l = 0.5
# start your for loop here
for i in range(1, len(t)):
    # update position
    x[i] = x[i-1] + dt*v
    # code the 2 boundaries
    if x[i] >= l or x[i] < -l:
        v = -v
# plot stuff
qw.time_plot1D(x, t, t_step=10)
plt.show()