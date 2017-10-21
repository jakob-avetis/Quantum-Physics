import numpy as np
from scipy.special import expi
# Basically the formulas above
def T11(R):
    return 0.5

def T12(R):
    return -0.5*(S12(R) - 2.0*(1.0+R)*np.exp(-R))

def V11A(R):
    return -1.0

def V11B(R):
    return -1.0/R + (1.0 + 1.0/R)*np.exp(-2.0*R)

def V12A(R):
    return -(1.0 + R)*np.exp(-R)

def V12B(R):
    return -(1.0 + R)*np.exp(-R)

def H11(R):
    return T11(R) + V11A(R) + V11B(R)

def H12(R):
    return T12(R) + V12A(R) + V12B(R)

def S12(R):
    return (1 + R + R**2/3.0)*np.exp(-R)

# Two electron integrals
def int_1111(R):
    asdf = np.ones_like(R)
    return 5.0/8.0*asdf

def int_1122(R):
    return (1.0 - (1.0 + 11.0/8.0*R + 3.0/4.0*R*R + 1.0/6.0*R**3 )*np.exp(-2.0*R))/R

def int_1112(R):
    return (R + (1.0/8.0 + 5.0/(16.0*R))*(1.0 - np.exp(-2.0*R)) )*np.exp(-R)

def int_1212(R):
    A = (1.0 - R + R*R/3.0)*np.exp(R)
    return 1.0/5.0*((25.0/8.0 - 23.0/4.0*R - 3.0*R*R - R**3.0/3.0)*np.exp(-2.0*R) +
                    6.0/R*((0.57722 + np.log(R))*S12(R)**2.0 + A*A*expi(-4.0*R) - 2.0*A*S12(R)*expi(-2.0*R)))     

def J11(R):
    return 1.0/(1.0+S12(R))**2*(0.5*int_1111(R) + 0.5*int_1122(R) + int_1212(R) + 2.0*int_1112(R))

def V(R):
    return 1.0/R

def J12(R):
    return 1.0/(1.0-S12(R)**2)*(0.5*int_1111(R) + 0.5*int_1122(R) - int_1212(R))

def J22(R):
    return (0.5*int_1111(R) + 0.5*int_1122(R) + int_1212(R) - 2.0*int_1112(R))/(1.0 - S12(R))**2

def K12(R):
    return 1.0/(2.0*(1.0-S12(R)**2))*(int_1111(R) - int_1122(R))