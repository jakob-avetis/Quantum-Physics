#initialize variables
L = 10
dx = 0.01
x = np.arange(0,L,dx)
t = np.arange(0,100)
psi = qw.pib_superposition(x, t, L,1,2)
p_array = np.zeros(len(t))
x_array = np.zeros(len(t))
# iterate over t
for indt in range(len(t)):
    # calculate operators and evaluate expectation values
    psi_x = psi[:,indt]
    p_psi = qw.momentum_operator(psi_x, dx)
    p_array[indt]=qw.eval_expectation(x,psi_x,p_psi)
    x_array[indt]=qw.eval_expectation(x,psi_x,x*psi_x)
# plot momentum
plt.plot(t, p_array)
plt.xlabel('time')
plt.ylabel('<p>')
plt.title('Expectation of p vs. time')
plt.show()
# plot position
plt.clf()
plt.plot(t, x_array)
plt.xlabel('time')
plt.ylabel('<x>')
plt.title('Expectation of x vs. time')
plt.show()