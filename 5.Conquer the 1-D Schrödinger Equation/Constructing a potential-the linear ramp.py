# build x grid
dx =0.05
x = np.arange(0,5.0+dx,dx)
# define potential function
def linear_ramp(x):
    return 2.0*x
# evaluate function on x
vx = linear_ramp(x)
# plot
plt.plot(x,vx)
# show the plot
plt.show()