import numpy as np
from scipy.integrate import odeint


def fun(x,t,v): # x_dot = f(x,t)

    psi = 0
    beta = 0
    theta = psi + beta
    dxdt = [v*np.cos(theta), #x
            v*np.sin(theta), #y
            0, #psi
            0, #r
            0] #beta
    return dxdt


def simulate(x0, v, ti):
    sol = odeint(fun, x0, ti, args=(v,))
    return sol
