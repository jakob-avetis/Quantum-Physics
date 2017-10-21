# define your function
def harmonic_time_dependent(t,c,n,l):
    return np.cos(n*np.pi*c*t/l)
# create variables
l = 10.0
c = 0.1
t = np.linspace(0,100,1000)
y = np.zeros((4, len(t)))
# use a for loop for the multiple harmonics
for n in range(1, 5):
    # plot stuff
    y[n-1] = harmonic_time_dependent(t,c,n,l)
    plt.plot(y[n-1])
    plt.legend(y[n-1])
plt.show()