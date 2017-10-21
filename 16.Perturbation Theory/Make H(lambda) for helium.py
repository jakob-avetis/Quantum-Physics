import numpy as np
from quantumworldX.helium import H11_pm, H12_pm, H22_pm, J22_pm, K22_pm

def H0():
    H = np.zeros((2,2))
    H[0,0] = H11_pm()-5.0/4.0
    H[1,1] = -5.0/2.0
    return H

def H1(lam):
    H = np.zeros((2,2))
    H[0,0] = 5.0/4.0*lam
    H[0,1] = H12_pm()*lam
    H[1,0] = H12_pm()*lam
    H[1,1] = 2*(J22_pm()+5.0/2.0) + 2*K22_pm()
    return H

def H_lambda(lam):
    return H0()+H1(lam)

test1=H0()
test2=H1(0.5)
test3=H_lambda(0.75)