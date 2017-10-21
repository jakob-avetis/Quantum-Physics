import quantumworldX as qw
import numpy as np
import matplotlib.pyplot as plt
v = 1.
dt = 0.001
m = 1
t = np.arange(0, 1.000000001, dt)
x = np.arange(0, 1.000000001, dt)
x[0] = 0

for time in range(1, len(t)):
    x[time] = x[time-1] + dt*v

qw.time_plot1D(x, t, t_step=30)
plt.show()