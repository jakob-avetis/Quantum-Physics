# create functions
def gaussian_x(x, sigma):
    u = x**2/(2.0*sigma**2)
    return np.exp(-u)/np.sqrt(sigma*np.sqrt(np.pi))

def gaussian_p(p, sigma):
    u  = ((p**2)*(sigma**2))/(2.0)
    return np.sqrt(sigma)*np.exp(-u)/np.sqrt(np.sqrt(np.pi))

def x_int(x, sigma):
    return gaussian_x(x, sigma)*x*gaussian_x(x, sigma)

def x2_int(x, sigma):
    return gaussian_x(x, sigma)*(x**2)*gaussian_x(x, sigma)

def p_int(p, sigma):
    return gaussian_p(p, sigma)*p*gaussian_p(p, sigma)

def p2_int(p, sigma):
    return gaussian_p(p, sigma)*(p**2)*gaussian_p(p, sigma)

# initialize variables
sigma=0.1
# calculate position part
exp_x = quad(x_int, -np.inf, np.inf, args=(sigma))[0]
exp_x2 = quad(x2_int, -np.inf, np.inf, args=(sigma))[0]
delta_x = np.sqrt(exp_x2 - exp_x**2)
# calculate momentum part
exp_p = quad(p_int, -np.inf, np.inf, args=(sigma))[0]
exp_p2 = quad(p2_int, -np.inf, np.inf, args=(sigma))[0]
delta_p = np.sqrt(exp_p2 - exp_p**2)
# calculate uncertainty
uncertainty = delta_x*delta_p
print(uncertainty)
print(uncertainty<=1)
#plot
grid = np.linspace(-10.0, 10.0,1000) # grid used for plotting
plt.plot(grid,gaussian_x(grid, sigma),label='position')
plt.plot(grid,gaussian_p(grid, sigma),label='momentum')
plt.legend()
plt.show()