import numpy as np
import matplotlib.pyplot as plt
# define your function
def harmonic_time_independent(x,n,l):
    return np.sin(n*np.pi*x/l)
# create variables
l = 10 
x = np.linspace(0,l,1000)
y = np.zeros((3,len(x)))
# use a for loop for the multiple harmonics
for n in range(1,4):
    # plot stuff
    y[n-1] = harmonic_time_independent(x,n,l)
    plt.plot(y[n-1])
plt.legend()
plt.show()