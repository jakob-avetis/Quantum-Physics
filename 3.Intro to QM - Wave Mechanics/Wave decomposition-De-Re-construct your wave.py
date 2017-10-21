# initial variables
l=10.0
x = np.arange(0,l,0.01)
y = np.array([square_function(xi, l) for xi in x])
square_approx = np.zeros(len(x))
# for loop over n
for n in range(0,10):
    # project amplitudes, sum components
    c_n,_ = quad(projection_integrand, 0,l,args=(n,l))
    square_approx = square_approx + c_n * np.sqrt(2.0/l)*np.sin((n*np.pi*x)/l)
# plot
plt.plot(x,y)
plt.plot(x,square_approx)
plt.title('Square wave')
plt.show()