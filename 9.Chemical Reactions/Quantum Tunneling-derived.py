# square barrier function
def square_barrier(x, l = 1, h=9, x0 = 4):
    a = x<x0 
    b = x>x0+l
    return h*~(a+b)
#def square_barrier(x, l = 1, h=9, x0 = 4):
#    v_x = np.zeros_like(x)
#    for i in range(len(x)):
#        if  x[i]<x0:
#            v_x[i] = 0
#        elif x[i] <= x0+l:
#            v_x[i] = h
#        else:
#            v_x[i] = 0
#    return v_x

# tunnel function
def tunnel_findiff_propagate(x,psi_x,v_x,E):
    dx = x[1]-x[0]
    psi_new = np.copy(psi_x)
    # iterate over 1 to len(x)-1
    for i in range(1, len(x)-1):   
        psi_new[i+1] = (2 + 2*(v_x[i] - E)*dx**2)*psi_new[i] - psi_new[i-1]
    # return time-propagated psi
    return psi_new
# initialize variables
dx = 0.01
x = np.arange(0, 10, dx)
energy = 10
psi_x = qw.plane_wave(x, energy)
barrier = square_barrier(x)
# calculate psi_tunnel and the pdf
psi_tunnel = tunnel_findiff_propagate(x, psi_x, barrier, energy)
pdf = qw.prob_density(psi_tunnel)
# plot
plt.plot(x,barrier,label='barrier')
plt.plot(x,psi_tunnel.real,label='real')
plt.plot(x,psi_tunnel.imag,label='imag')
plt.plot(x,pdf,label='pdf')
plt.xlabel('x')
plt.legend()
plt.show()