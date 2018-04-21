import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt
import sim_kotm as kotm
import kinematic_control as kc


def f_closed_loop(x_, t):
    x, y, psi = x_
    v = 1

    # projection stub
    d = y
    theta_r = 0
    kappa_r = 0

    delta = kc.feedback_law(d, psi, theta_r, kappa_r)
    x_dot_ = kotm.fun(x_, t, v, delta)
    return x_dot_


def main():
    print('Running simulation...')
    x0 = [0, 0.2, 0]
    ti = np.arange(0, 20, 0.1)
    sol = odeint(f_closed_loop, x0, ti)
    x = sol[:, 0]
    y = sol[:, 1]
    psi = sol[:, 2]
    print(y)
    plt.plot(x, y, 'r-')
    plt.axis('equal')
    plt.show()

if __name__ == "__main__":
    main()