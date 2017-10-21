import numpy as np
import matplotlib.pyplot as plt
import quantumworldX as qw
v = 2.0
dt = 0.001
m = 1
t = np.arange(0,2+dt,dt)
x = np.zeros(len(t))
x[0] = 0.0
l = 0.5
## update for-loop
for i in range(1,len(t)):
    # update velocity and then position
    v = v + dt*5*np.sin(2*t[i])/m
    x[i]=x[i-1]+dt*v
    # consider both boundary conditions
    if x[i] >= l or x[i] < -l:
        v=-v
## plotting code
qw.time_plot1D(x,t,t_step=30)
plt.show()