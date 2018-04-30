import numpy as np
import pseudo_projection as pro
import sim_kotm as kotm


def feedback_law(d, psi, theta_r, kappa_r):
    axis_distance = 2.9680
    k_0 = 0.2
    k_1 = 1.

    # Stabilization
    u = kappa_r - k_0 * d - k_1 * normalize_angle(psi-theta_r)

    # Re-substitution
    delta = np.arctan(axis_distance*u)
    return delta


def normalize_angle(angle):
    return (angle+np.pi) % (2*np.pi) - np.pi


def f_closed_loop(x_, t, curve):
    x, y, psi = x_
    _, _, _, d, theta_r, kappa_r = \
        pro.project2curve(curve['s'], curve['x'], curve['y'], curve['theta'], curve['kappa'],
                          x, y)
    delta = feedback_law(d, psi, theta_r, kappa_r)
    v = 1  # const velocity
    x_dot_ = kotm.fun(x_, t, v, delta)
    return x_dot_

