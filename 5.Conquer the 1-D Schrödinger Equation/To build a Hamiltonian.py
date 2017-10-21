# initial variables
L=10.0
x = np.arange(0,L,0.01)
dx = x[1] - x[0]
v_x = v(x)
# define kinetic operator function
def kinetic_operator(x, m=1, h_bar=1):
    # precalculate variables like dx, t and intialize T
    dx = x[1]-x[0]
    t = -(h_bar**2) / (2.0 * m*dx**2)
    T = np.zeros((len(x), len(x)))
    # iterate over x
    for i in range(len(x)):
        # consider first diagonal elements
        T[i][i] = -2 * t
        # then side diagonal elements, consider edge cases (i=0) or (i=n-1)
        if i == 0:
            T[i][i + 1] = t
        elif i == len(x) - 1:
            T[i][i - 1] = t
        else:
            T[i][i + 1] = t
            T[i][i - 1] = t
    return T
# get T, then V and then H
T = kinetic_operator(x)
V = np.diag(v_x)
H = T + V