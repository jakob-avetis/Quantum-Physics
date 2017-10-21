#initial variables
c = 0.1
l= 10
x = np.arange(0,l,0.01)
t = np.arange(0,30,0.1)
y = np.zeros((len(x),len(t)))
n = 3

# for loop over t
for i in range(len(t)):
    # calculate time dependent and independent parts
    for j in range(len(x)):
        y[j,i] = harmonic_time_dependent(t[i],c,n,l) * harmonic_time_independent(x[j],n,l)

# time-plot stuff
qw.time_plot(x,y,t,t_step=1)
plt.show()