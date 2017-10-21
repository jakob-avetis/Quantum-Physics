def square_function(x, l):
    if x <= l/3.0 or x >= l*2.0/3:
        y = 0
    else:
        y = 1
    return y

def projection_integrand(x,n,l):
    integrand = np.sqrt(2.0/l)*np.sin((n*np.pi*x)/l)*square_function(x,l)
    return integrand

l=10.0
x = np.arange(0,l,0.01)
c = np.zeros(10)

for n in range(0,10):
    c_n,_ = quad(projection_integrand, 0,l,args=(n,l))
    c[n] = c_n