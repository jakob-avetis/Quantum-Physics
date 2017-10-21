dt = 0.001
t = np.arange(0,1+dt,dt)
v1, v2 = 2.0,-2.0
m1, m2 = 1,1
x1, x2 = np.zeros(len(t)), np.zeros(len(t))
x1[0],x2[0] = 0.1,-0.1
dt = 0.001
t = np.arange(0,1+dt,dt)
l = 0.5
for i in range(1,len(t)):
    # particle 1: update velocity then position
    v1 = v1 + dt*5*np.sin(2*t[i])/m
    x1[i]=x1[i-1]+dt*v1
    # particle 1: boundary condition
    if x1[i] >= l:
        v1=-v1
    if x1[i] < -l:
        v1=-v1
    # particle 2: update velocity than position

    # particle 2: boundary conditions

