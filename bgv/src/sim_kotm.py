import numpy as np
from scipy.integrate import odeint


def fun(x, t, v):  # x_dot = f(x,t)
    x, y, psi = x

    par_l = 2.
    delta = 0

    x_dot = v*np.cos(psi)
    y_dot = v*np.sin(psi)
    psi_dot = v*np.tan(delta)/par_l

    dxdt = [x_dot, y_dot, psi_dot]
    return dxdt


def simulate(x0, v, ti):
    sol = odeint(fun, x0, ti, args=(v,))
    return sol
