# repul array to store values
repul = np.zeros(len(t))
# create force function here
def repulsion(r1, r2):
    return 5.0/(np.abs(r1 - r2))

t = np.arange(0,1+dt,dt)
#iterate over t array
for i in range(1,len(t)):
    # calculate repulsion, positive for particle1, negative for particle2
    repul[i] = repulsion(x1[i-1], x2[i-1])
    # particle 1: velocity > position > boundary
    v1 = v1 + dt*repul[i]
    x1[i] = x1[i-1] + dt * v1
    v1 = boundary_1d(x1[i], v1, l)
    # particle 2: velocity > position > boundary
    v2 = v2 - dt*repul[i]
    x2[i] = x2[i-1] + dt * v2
    v2 = boundary_1d(x2[i], v2, l)
# plot stuff
qw.time_plot1D([x1,x2],t,t_step=30)
plt.clf()
plt.plot(t, repul)
plt.show()