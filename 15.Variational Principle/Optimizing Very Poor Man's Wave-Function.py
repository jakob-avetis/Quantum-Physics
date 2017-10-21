import numpy as np
from scipy.integrate import tplquad
from quantumworldX.helium import phi1
zeta = 2

def H11_vpm(t, u, s, zeta=1.6875, Z=2):
    return np.exp(-2*s*zeta)*(s*s - t*t - 4.0*s*u*Z + (s - t)*(s + t)*u*zeta*zeta)
def S11_vpm(t, u, s, zeta=1.6875, Z=2):
    return u*(s*s - t*t)*phi1(s, t, u, zeta)*phi1(s, t, u, zeta)

def expected_phi1(zeta):
    # this is how we 3-d integrate
    S11_int, error = tplquad( S11_vpm  ,
                                0.0, np.inf,
                                lambda x: 0.0, lambda x: x,
                                lambda x, y: 0.0, lambda x, y: y,
                                args=(zeta, 2.0))
    H11_int, error = tplquad(  H11_vpm    ,
                                0.0, 50.0,
                                lambda x: 0.0, lambda x: x,
                                lambda x, y: 0.0, lambda x, y: y,
                                args=(zeta, 2.0))
    return H11_int/S11_int

e = expected_phi1(zeta)
print(e)