def J(R):
    return np.exp(-2*R)*(1+1.0/R)

def S(R):
    return np.exp(-R)*(1+R + (R**2)/3)

def K(R):
    return S(R)/R -np.exp(-R)*(1+R)

def E_plus(R):
    return  -1/2.0 + ( (J(R) + K(R))/(1.0-S(R)) )

def E_minus(R):
    return -1/2.0 + ( (J(R) - K(R))/(1.0-S(R)) )